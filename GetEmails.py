import os
from time import sleep




def GetEmails():
    # cd to the email_extraction dir
    os.chdir('email_extraction')
    # sleep(1.5)
    try:
        os.remove('emails.csv')
    except:
        print('nothing..')
    os.system('scrapy crawl email_ex -o emails.csv')
    sleep(10)
    print('ok')



