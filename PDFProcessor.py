from ntpath import join
import pdfx
import validators

Shtup=('gif','pdf','jpg','png','tiff','psd','raw','ai','indd')
def getLinks(filename):
    # method to get all links in the pdf file.
    try:
        pdf=pdfx.PDFx(filename)
        p=pdf.get_references()
        l=[]
        for i in p:
            # the url format <url :.....>
            s=str(i).split(' ')[1][:-1]
            if validators.url(s):
                # check if the url for image or...(see the tuple)
                if s.split('.')[-1] not in Shtup:
                    l.append(s)
        return l
    except:
        return None

getLinks('PDFRoom/datasprings_dynamiclogin_userguide.pdf')