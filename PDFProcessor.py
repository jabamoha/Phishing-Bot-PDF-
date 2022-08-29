import pdfx
import validators
import pdfrw
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




#--------------------------------
def swap_links(dict,filename):
    print('=================swap href===========')
    print(dict)
    try:
        pdf = pdfrw.PdfReader("PDFRoom/"+str(filename))
        new_pdf = pdfrw.PdfWriter()  

        for page in pdf.pages:  

            for annot in page.Annots or []:
                old_url = annot.A.URI
                if old_url in dict:
                    print('========href-change=========')
                    new_url = pdfrw.objects.pdfstring.PdfString('(https://www.google.com/)')
                else:
                    new_url= pdfrw.objects.pdfstring.PdfString('#')
                annot.A.URI = new_url

                # print(annot.A.URI)
            new_pdf.addpage(page)   

        new_pdf.write('PDFRoom/'+str('PH_'+filename))
        return str('PH_'+filename)
    except:
        print('======File have not Links======')

# swap_links(None,'AA.pdf')
