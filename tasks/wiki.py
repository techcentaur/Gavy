import requests

def wiki(query):
    param = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": query
    }

    url = "https://en.wikipedia.org/w/api.php?"+"format="+param['format']+"&action="+param['action']+"&prop="+param['prop']+"&exintro=&explaintext=&titles="+param['titles']

    r = requests.get(url)
    data = r.json()

    pagedata = data['query']['pages']
    page = list(pagedata)
    pageid = page[0]

    wikidata = {
        'title': pagedata[pageid]['title'],
        'extract': pagedata[pageid]['extract']
    }

    return wikidata
