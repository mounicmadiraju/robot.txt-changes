import requests
import difflib
import json
import smtplib
import time
class mail:
    def __init__(self):
        self.toaddrs  = ['mounicraju@gmail.com','mounic2012@gmail.com']
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.starttls()
        self.server.login('senderemail','senderpassword')
    def send(self,msg):
        self.server.sendmail('senderemail', self.toaddrs, msg)
    def clean(self):
        self.server.quit()       
def diff(s1,s2):        # Finding the difference in the strings
    dif=list(difflib.ndiff(s1.splitlines(),s2.splitlines()))
    changed=[str(line)+'\t'+str(change) for line,change in enumerate(dif) if change[0].strip()]
    return '\n'.join(changed)
m=mail()  # loading Mail object
url_list=["url1/robots.txt", "url2/robots.txt", "url3/robots.txt"] #  Adding url's here
data_today={url:str(requests.get(url).text) for url in url_list}    # Creating the data dict for today
with open('data.txt', 'r') as infile:
    data_yes=json.load(infile)  #Getting the stored data 
for url in url_list:
    if url in data_yes:
        change=diff(data_today[url], data_yes[url])
        if change:
            m.send("Subject:"+url+"\nModified lines :\n"+change)
            print 'changed : '+url+' ,mail sent '
        else:
            print url+': No changes found'
    else:
        print 'New URL found ... adding'
m.clean() # close the mail 
with open('data.txt', 'w') as outfile:
    outfile.write(json.dumps(data_today))
with open('data'+time.strftime("%d-%m-%Y")+'.txt', 'w') as outfile:
    outfile.write(json.dumps(data_today))
