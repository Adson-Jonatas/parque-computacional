import sys
import re
import json
import yaml
from typing import List, Dict


def parse_txt_to_issues(txt_path: str) -> List[Dict]:
    issues = []
    in_issues_section = False

    with open(txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("Issues"):
                in_issues_section = True
                continue
            elif in_issues_section and line == "":
                break  # fim da seção
            elif in_issues_section:
                parts = line.split()
                if len(parts) < 4:
                    continue
                issue_id, issue_type, severity = parts[:3]
                rest = ' '.join(parts[3:])
                m = re.match(r'(.*) ([^ ]+ [^ ]+)$', rest)
                if m:
                    description = m.group(1)
                    library = m.group(2)
                else:
                    description = rest
                    library = ""

                issues.append({
                    "issue_id": issue_id,
                    "issue_type": issue_type,
                    "severity": severity,
                    "description": description,
                    "library": library,
                })
    return issues


def load_yaml_rules(yaml_path: str) -> Dict:
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def deve_bloquear(severity: str, sigla: str, rules: Dict) -> bool:
    if severity in rules.get("bloquear_severidades_globais", []):
        return True
    sigla_rules = rules.get("bloquear_severidades_por_sigla", {}).get(sigla, [])
    return severity in sigla_rules


def deve_bypassar(issue: Dict, sigla: str, rules: Dict) -> bool:
    cve_match = any(cve in issue.get("description", "") for cve in rules.get("bypass_globais", {}).get("cves", []))
    lib_match = issue["library"].split()[0] in rules.get("bypass_globais", {}).get("libs", [])

    sigla_bypass = rules.get("bypass_por_sigla", {}).get(sigla, {})
    cve_sigla = any(cve in issue.get("description", "") for cve in sigla_bypass.get("cves", []))
    lib_sigla = issue["library"].split()[0] in sigla_bypass.get("libs", [])

    return cve_match or lib_match or cve_sigla or lib_sigla


def main():
    if len(sys.argv) != 5:
        print("Uso: python script.py <arquivo_txt> <arquivo_yaml> <sigla> <componente>")
        sys.exit(1)

    txt_path, yaml_path, sigla, componente = sys.argv[1:5]
    issues = parse_txt_to_issues(txt_path)
    rules = load_yaml_rules(yaml_path)

    resultado = []
    auditoria = []

    for issue in issues:
        auditoria_entry = issue.copy()
        if deve_bypassar(issue, sigla, rules):
            auditoria_entry["motivo"] = "Bypass aplicado"
        elif deve_bloquear(issue["severity"], sigla, rules):
            auditoria_entry["motivo"] = "Bloqueado por severidade"
            resultado.append(issue)
        else:
            auditoria_entry["motivo"] = "Aceito (não bloqueado)"
        auditoria.append(auditoria_entry)

    with open("resultado.json", "w", encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    with open("auditoria.json", "w", encoding='utf-8') as f:
        json.dump(auditoria, f, indent=2, ensure_ascii=False)

    print("Processamento concluído. Arquivos resultado.json e auditoria.json gerados.")


if __name__ == "__main__":
    main()
