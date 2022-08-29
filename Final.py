from email import header
from time import sleep
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


Route=''
Header="""from flask import render_template\n
from flask import Flask, render_template,request \n
app=Flask(__name__)\n

    """



Basic="""
@app.route('/')
def indexREPLACEME():\n
    return render_template("GIT.html")\n
    """

End="""
if __name__ == '__main__':\n
    app.run( port=8080 ,debug=True)

    """



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
        print('==============FILE NAME===============')
        print(fileName)
        fileName=fileName+'.pdf'
        print('====================================')
        BuildServer(fileName)
    
  

    
    
    print('Server file was built at app.py')
    GetEmails.GetEmails()
    



dict={}



i=1
 
def BuildServer (fileName,n=5):
    Links=PDFProcessor.getLinks('PDFRoom/'+str(fileName))
    global i
    global Route

   
    NewRoute="""
@app.route('/REPLACEME')
def indexREPLACEME():\n
    return render_template("REPLACEME.html")\n
    """

    memoryvar=NewRoute

 
    
    print('===============================Kareem ========')
    print(Links)
    if Links is not None:
        for link in Links:
            NewFileName=str(i)+'.html'
            dict[link]='http://localhost:8080/'+str(i)
            Builder.Clone(link,NewFileName)
            NewRoute=NewRoute.replace('REPLACEME', str(i), 3)
            print('===========script check =================')
            print(NewRoute)
            print('===========end script check =================')
            Route+=NewRoute
            #f.write(NewRoute)
            NewRoute=memoryvar
            i+=1
            if n==0:
                break
            n-=1
    print(dict)
    
    PDFProcessor.swap_links(dict,str(fileName))
    f = open("app.py", "w")
    f.write(Header)
    f.write(Basic)
    f.write(Route)
    f.write(End)
    f.close()
    



#SearchPdf(sargs)