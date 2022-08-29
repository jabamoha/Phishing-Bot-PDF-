import requests,bs4
import os
import re
index=0

def get_result_search(keyword,n):
    # input:key words to search in google , n is the number of search's(n results...) 
    #output: url's of pdf's from google 
    lis=[]
    res=requests.get('https://google.com/search?q='+str(keyword)+' .pdf')
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    # the next line to get the urls from the the search result
    linkElements=soup.select('div#main > div > div > div > a')
    linkToOpen=min(n,len(linkElements))
    for i in range(linkToOpen):
        url=('https://google.com'+linkElements[i].get('href'))
        if '.pdf' in url:
            # check if the url a pdf file 
            lis.append(url)
    return lis

def Downloading_PDF(url):
    # Get response object for link
    global index
    response = requests.get(url)
    name_of_pdf=get_name_of_pdf(url)
    if not re.match("^[A-Za-z0-9_-]*$", name_of_pdf):
        index+=1
        name_of_pdf=str(index)
    # Write content in pdf file
    pdf = open('PDFRoom/'+name_of_pdf+".pdf", 'wb')
    pdf.write(response.content)
    pdf.close()
    return name_of_pdf
    

def get_name_of_pdf(url):
    # method to detect and return the name of the pdf file from the url...
    str=url.split('/')
    for s in str:
        if '.pdf' in s:
            sub=s.split('.pdf')[0]
            sub=sub.replace('%2520',' ')
            return sub
    return None



def Search_PDFs(keywords,n=5):
    # the main method 
    NamesList=[]
    list=get_result_search(keyword=keywords,n=n)
    for elt in list:
        NamesList.append(Downloading_PDF(elt))
    return NamesList    