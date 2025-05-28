// Groovy Script para rodar na Shared Library (ex: dentro de vars ou um step inline)
// Este código assume que já existe um relatório Veracode (saida.txt) e que há um arquivo YAML com regras de bypass

@Grab('org.yaml:snakeyaml:1.30')
import org.yaml.snakeyaml.Yaml

import groovy.json.JsonOutput

// Função principal
void validarVulnerabilidades(Map config = [:]) {
    def arquivoTxt = config.arquivo ?: 'saida.txt'
    def sigla = config.sigla ?: 'DESCONHECIDA'
    def componente = config.componente ?: 'NAO_INFORMADO'
    def yamlUrl = config.regrasYaml ?: 'https://bitbucket.exemplo.com/raw/veracode-bypass.yaml'

    def txt = new File(arquivoTxt).text
    def issues = extrairIssuesComoMapa(txt)

    def regrasYaml = new URL(yamlUrl).text
    def bypass = new Yaml().load(regrasYaml)

    def bloqueios = []

    issues.each { issue ->
        if (!deveSerBypassado(issue, bypass, sigla, componente)) {
            bloqueios << issue
        }
    }

    println "----- Resultado da Validação de Vulnerabilidades -----"
    if (bloqueios.isEmpty()) {
        println "✔ Nenhuma vulnerabilidade bloqueante encontrada."
    } else {
        bloqueios.each {
            println "❌ [${it.id}] ${it.tipo} | ${it.cve} | ${it.lib} | CVSS ${it.severidade}"
        }
        error "Build bloqueado por ${bloqueios.size()} vulnerabilidade(s) crítica(s)"
    }
}

// Extrai a seção de issues do arquivo txt e converte para lista de Mapas
List<Map> extrairIssuesComoMapa(String conteudo) {
    def lines = conteudo.readLines()
    def issues = []
    def capturando = false

    lines.each { line ->
        if (line ==~ /^Issues$/) {
            capturando = true
            return
        }
        if (capturando && line.trim().isEmpty()) {
            capturando = false
            return
        }
        if (capturando && line ==~ /^\d{9}.*/) {
            def partes = line.tokenize()
            def id = partes[0]
            def tipo = partes[1]
            def severidade = partes[2] as Double
            def descricao = partes[3..-3].join(' ')
            def lib = partes[-2..-1].join(' ')

            def cve = descricao.find(/CVE-\d{4}-\d{4,7}/) ?: ''

            issues << [
                id: id,
                tipo: tipo,
                severidade: severidade,
                descricao: descricao,
                lib: lib,
                cve: cve
            ]
        }
    }
    return issues
}

// Verifica se uma issue deve ser ignorada (bypass)
boolean deveSerBypassado(Map issue, Map regras, String sigla, String componente) {
    def g = regras.bypass.global ?: [:]
    def s = (regras.bypass.siglas ?: [:])[sigla] ?: [:]
    def c = (s.componentes ?: [:])[componente] ?: [:]

    def cvesBypass = (g.cves ?: []) + (s.cves ?: []) + (c.cves ?: [])
    def libsBypass = (g.libs ?: []) + (s.libs ?: []) + (c.libs ?: [])
    def severidadesBypass = (g.severidades ?: []) + (s.severidades ?: []) + (c.severidades ?: [])

    def matchCVE = issue.cve && issue.cve in cvesBypass
    def matchLib = libsBypass.any { lib -> issue.lib.contains(lib) }
    def matchSeveridade = severidadesBypass.contains(issue.severidade)

    return matchCVE || matchLib || matchSeveridade
}

// Exemplo de chamada:
// validarVulnerabilidades(
//     arquivo: 'saida.txt',
//     sigla: 'ABCD-CAZT',
//     componente: 'net-abcd-gutt-controle-gestao',
//     regrasYaml: 'https://bitbucket.exemplo.com/raw/veracode-bypass.yaml'
// )
