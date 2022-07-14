import requests,bs4
from tldextract import extract

def get_source_code(url):
    # return the html code of the url
    req_res=requests.get(url=url)
    soup=bs4.BeautifulSoup(req_res.text,"html.parser")
    return soup



def get_domain_from_url(url):
    _,td,tsu=extract(url)
    return str(td+'.'+tsu)


    