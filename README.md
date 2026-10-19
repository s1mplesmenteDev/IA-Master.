# IA-Master.
Exercícios do Curso IA Master da PycodeBR 

**Exercícios 1 - Agent com Tools: Search + Cálculo (Pyhton REPL)**
*Enunciado*
Contexto

No Módulo 4 do curso (Agentes e Ferramentas), você viu a criação de agentes equipados com tools, incluindo exemplos com search tool, Python REPL e banco de dados SQL. No projeto demonstrado (Finanpy), o agente é inicializado com LangChain e a API da OpenAI, configurando modelo e temperatura via variáveis de ambiente, e organizando o código em pastas Agents e Tools. Neste exercício, você aplicará esses princípios para montar um agente funcional que sabe escolher e acionar tools conforme a tarefa.

*Objetivo*

Construir um agente (IA Integration Expert) que use duas tools:
search_local: busca em documentos locais (mock)
python_calc: realiza cálculos aritméticos simples (equivalente ao Python REPL)
Configurar o agente via variáveis de ambiente para escolher o modelo e a temperatura
Demonstrar que o agente decide e utiliza as tools corretamente em cenários de teste
Pré-requisitos

Conta e chave de API de um provedor compatível (ex.: OpenAI), se quiser executar com LLM real
Python 3.10+ e um ambiente virtual configurado
Noções básicas de LangChain (conforme material do curso)