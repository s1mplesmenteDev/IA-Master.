from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

perguntaDuckDuckGo = input('Digite a pergunta para DuckDuckGo: ')
perguntaWikipedia = input('Digite a pergunta para o Wikipedia')

ddg_search = DuckDuckGoSearchRun()

search_result = ddg_search.run({perguntaDuckDuckGo})
print(search_result)

consulta_wikipedia = WikipediaQueryRun(
    api_wrapper = WikipediaAPIWrapper(
        lang='pt'
    )
)

result_wikipedia = consulta_wikipedia.run({perguntaWikipedia})
print(result_wikipedia)