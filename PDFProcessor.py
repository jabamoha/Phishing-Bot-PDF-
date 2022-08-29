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
    # print(dict)
    try:
        pdf = pdfrw.PdfReader("PDFRoom/"+str(filename))
        new_pdf = pdfrw.PdfWriter()  

        for page in pdf.pages:  
            print('forrrrrrrrrrrrrrrrrrrrrrrrrrr')
            print(page.Annots)
            for annot in page.Annots or []:
                print('fotnaaaaaaaaaaaaaaaaaaaa')
                old_url = annot.A.URI
                print(old_url)
                # if old_url in dict:
                    # print('========href-change=========')
                new_url = pdfrw.objects.pdfstring.PdfString('(http://google.com)')
                # else:
                #     new_url= pdfrw.objects.pdfstring.PdfString('#')
                annot.A.URI = new_url

                # print(annot.A.URI)
            new_pdf.addpage(page)   

        new_pdf.write('PDFRoom/'+str('PH_'+filename))
        return str('PH_'+filename)
    except:
        print('======File have not Links======')

# swap_links(None,'AA.pdf')

# swap_links(None,'ndss-phish-tools-final.pdf')
