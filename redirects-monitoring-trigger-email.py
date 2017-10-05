import requests
import json
import smtplib
import difflib
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
urls=['url1', 'url2', 'url3']  # List of urls to add
m=mail()
data_today={}
for url in urls:
    output=[]
    r=None
    try:
        r=requests.get(url)
    except:
        output.append('Connection error')
    if r and r.history:
        for resp in r.history:
            output.append(resp.url+' -> '+str(resp.status_code)+'\n')
    output.append(r.url+' -> '+str(r.status_code)+'\n')
    data_today[url]=''.join(output)
    
with open('redirect.txt', 'r') as infile:
    data_yes=json.load(infile) 
    
for url in urls:
    if url in data_yes:
        change=diff(data_today[url], data_yes[url])
        if change:
            m.send("Subject:"+url+"\nModified lines :\n"+change)
            print 'changed.mail sent.'
        else:
            print url+': No changes found'
    else:
        print 'New URL found ... adding'
m.clean() # close the mail 
with open('redirect.txt', 'w') as outfile:
    outfile.write(json.dumps(data_today))
with open('redirect'+time.strftime("%d-%m-%Y")+'.txt', 'w') as outfile:
    outfile.write(json.dumps(data_today))  
