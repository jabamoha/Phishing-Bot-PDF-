from this import d
from unicodedata import name
import requests,bs4
from tldextract import extract
import os

def get_source_code(url):
    # return the html code of the url
    req_res=requests.get(url=url)
    soup=bs4.BeautifulSoup(req_res.text,"html.parser")
    return soup



def get_domain_from_url(url):
    _,td,tsu=extract(url)
    return str(td+'.'+tsu)

def build_app_dir(url):
    name_of_dir=get_domain_from_url(url=url).split('.')[0]
    curr_path=os.path.abspath(os.getcwd())+'\\'+'WebApp'
    path=os.path.join(curr_path,name_of_dir)
    os.mkdir(path=path)


def build_html_file(url):
    source_code=get_source_code(url=url)
    name_of_dir=get_domain_from_url(url=url).split('.')[0]
    os.path.abspath(os.getcwd())+'\\'+'WebApp'
    # need to complete...
    