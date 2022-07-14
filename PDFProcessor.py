import pdfrw


def getLinks(filename):
    # method to get all links in the pdf file.
    pdf = pdfrw.PdfReader(str(filename))
    list=[]
    for page in pdf.pages:  
        for annot in page.Annots or []:
            url = annot.A.URI
            list.append(url)
    return list

