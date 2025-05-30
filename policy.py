import sys
import yaml
import json
import re

# Dicionário de mapeamento de pontuação para severidade textual
def get_severity_label(score):
    score = float(score)
    if score >= 9.0:
        return 'CRITICAL'
    elif score >= 7.0:
        return 'HIGH'
    elif score >= 4.0:
        return 'MEDIUM'
    elif score > 0:
        return 'LOW'
    else:
        return 'NONE'

# Carrega regras do YAML
def load_rules(yaml_path):
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

# Extrai as issues do arquivo txt e converte para JSON
def parse_issues(txt_path):
    issues = []
    with open(txt_path, 'r') as f:
        inside_issues = False
        for line in f:
            line = line.strip()
            if line.startswith("Issues"):
                inside_issues = True
                continue
            if inside_issues and line == "":
                break
            if inside_issues and re.match(r'^\d{9}', line):
                parts = line.split()
                issue_id = parts[0]
                issue_type = parts[1]
                severity_score = parts[2]
                rest = " ".join(parts[3:])
                lib_match = re.search(r' ([^ ]+) ([^ ]+)$', rest)
                if lib_match:
                    description = rest[:lib_match.start()].strip()
                    library = lib_match.group(0).strip()
                else:
                    description = rest
                    library = ""

                issues.append({
                    "issue_id": issue_id,
                    "issue_type": issue_type,
                    "severity_score": float(severity_score),
                    "severity_label": get_severity_label(severity_score),
                    "description": description,
                    "library": library
                })
    return issues

# Verifica se a issue deve ser ignorada por regra
def is_bypassed(issue, rules, sigla, componente):
    cve_id = issue["issue_id"]
    lib = issue["library"].split()[0]
    version = issue["library"].split()[1] if len(issue["library"].split()) > 1 else None
    severity = issue["severity_label"]

    # 1. Global bypass
    if cve_id in rules.get("bypass", {}).get("global", {}).get("cves", []):
        return True
    if lib in rules.get("bypass", {}).get("global", {}).get("libs", []):
        return True
    if severity in rules.get("bypass", {}).get("global", {}).get("severidades", []):
        return True

    # 2. Sigla
    if sigla in rules.get("bypass", {}).get("siglas", {}):
        if cve_id in rules["bypass"]["siglas"][sigla].get("cves", []):
            return True
        if lib in rules["bypass"]["siglas"][sigla].get("libs", []):
            return True
        if severity in rules["bypass"]["siglas"][sigla].get("severidades", []):
            return True

    # 3. Componente
    if componente in rules.get("bypass", {}).get("componentes", {}):
        if cve_id in rules["bypass"]["componentes"][componente].get("cves", []):
            return True
        if lib in rules["bypass"]["componentes"][componente].get("libs", []):
            return True
        if severity in rules["bypass"]["componentes"][componente].get("severidades", []):
            return True

    return False

# Verifica se a issue deve ser bloqueada por severidade
def is_blocked(issue, rules, sigla):
    severity = issue["severity_label"]
    grupos = rules.get("bloqueios", {}).get("grupos_de_siglas", {})
    for grupo_severidade, siglas in grupos.items():
        if sigla in siglas:
            if severity == grupo_severidade:
                return True
    return severity == "CRITICAL"  # Regra global padrão

def main():
    if len(sys.argv) != 5:
        print("Uso: python script.py <arquivo_txt> <arquivo_yaml> <sigla> <componente>")
        sys.exit(1)

    txt_path = sys.argv[1]
    yaml_path = sys.argv[2]
    sigla = sys.argv[3]
    componente = sys.argv[4]

    rules = load_rules(yaml_path)
    issues = parse_issues(txt_path)

    final_issues = []

    for issue in issues:
        if is_bypassed(issue, rules, sigla, componente):
            continue
        if is_blocked(issue, rules, sigla):
            final_issues.append(issue)

    print(json.dumps(final_issues, indent=2))

if __name__ == "__main__":
    main()
