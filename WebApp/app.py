# import flask modules
from genericpath import isfile
from flask import Flask, render_template,request


# import the pathlib to check if the file exists
from pathlib import Path

# import the os and sys pacakges to slove the import moudles problem
import os
import sys
dir=os.getcwd().split('\\')[:-1]
p=''
for i in range(0,len(dir)-1):
    p+=dir[i]+'\\'
p+='PHISHING-BOT-PDF-'
sys.path.insert(0,p)

# import the python file that find pd
import  SearchEngine
import PDFProcessor

# import the python module to extract emails...
import GetEmails

# import shutil to remove files...
import shutil

# create a flask appliction
app=Flask(__name__)

# the main page...
@app.route('/')
def index():
    return render_template('index.html',dict=None)

@app.route('/handle_data',methods=['POST'])
def get_args():
    # get the input 
    search_input=request.form['search_query']
    clear_dir('URLS_FILES')
    clear_dir('KEYS')
    clear_dir('PDFRoom')
    # check if the file of the key words exists,(yes then remove it.).
    my_keys_file=Path('../KEYS/keywords.txt')
    if my_keys_file.exists():
        # remove the file using os
        os.remove('../KEYS/keywords.txt')
    # write the keywords in a .txt file to read it for extract emails...
    with open('../KEYS/keywords.txt','w') as f:
        f.write(search_input)
        f.close()

    # Find the pdf(s) and save them in ../PDFRoom ...
    SearchEngine.Search_PDFs(keywords=search_input)
    dict=Build_Dict()
    # get the emails
    GetEmails.GetEmails()
    return render_template('index.html',dict=dict)


def Build_Dict():
    #get the list of PDF(s)
    PdfList=os.listdir('../PDFRoom') 
    # why ..? because the currDir is WebApp

    # build a dictionary ,the key is unique number and the value is list of items...
    dict={}
    for index in range(0,len(PdfList)):
        l=[]
        url_list=PDFProcessor.getLinks('../PDFRoom/'+str(PdfList[index]))
        if url_list is not None:
            pathOfFile=Build_URL_File(index=index,urls=url_list)
            # the append(arg):add arg to the end of the list
            l.append(PdfList[index])
            l.append(pathOfFile)
            dict[index]=l
            # the value of this keys is a list
    return dict 


p+='\\URLS_FILES\\'
def Build_URL_File(index,urls):
    # A function to build a text file for the urls
    global p
    with open('../URLS_FILES/'+str(index)+'.txt','w') as file:
        for url in urls:
            try:
              file.write(url)
            except:
                print(url)
            file.write('\n')
        file.close()
        # return the path of the file
        return p+str(index)+'.txt'

def clear_dir(DirName):
    # A function to remove all files in dir
    folder='../'+str(DirName)
    # why ../ ?  ,because the current dir is WebApp
    for filename in os.listdir(folder):
        file_path=os.path.join(folder,filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except:
            print('File Not Found')

    
 





# run the flask app
if __name__ == '__main__':
    app.run( port=8080 ,debug=True)
