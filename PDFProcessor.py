import pdfrw
import requests
import bs4


def getLinks(filename):
    # method to get all links in the pdf file.
    pdf = pdfrw.PdfReader(str(filename))
    list=[]
    for page in pdf.pages:  
        for annot in page.Annots or []:
            url = annot.A.URI
            list.append(url)
    return list

text= "geeksforgeeks"
url = 'https://google.com/search?q=' + text
  
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )
  
# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,
                         "html.parser")
print(soup)