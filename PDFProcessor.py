import pdfx
import validators
import pdfrw
Shtup=('gif','pdf','jpg','png','tiff','psd','raw','ai','indd')
def getLinks(filename):
    # method to get all links in the pdf file.
    try:
        l=[]
        pdf = pdfrw.PdfReader(filename)
        for page in pdf.pages:  
            for annot in page.Annots or []:
                old_url = annot.A.URI
                o=str(old_url).replace(')','')
                o=o.replace('(','')
                if o.split('.')[-1] not in Shtup:
                 l.append(o)

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
            #print(page.Annots)
            for annot in page.Annots or []:
                print('fotnaaaaaaaaaaaaaaaaaaaa')
                old_url = annot.A.URI
                print(old_url)
                o=str(old_url).replace(')','')
                o=o.replace('(','')
                if o in dict:
                    print('========href-change=========')
                    new_url = pdfrw.objects.pdfstring.PdfString('('+dict[o]+')')
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

# swap_links(None,'AA.pdf')

# print(getLinks('PDFRoom/PH_AA.pdf'))
