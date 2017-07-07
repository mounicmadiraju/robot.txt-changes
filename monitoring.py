# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib


while True:

    url = "https://mounicmadiraju.blogspot.com/"
  
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
      response = requests.get(url, headers=headers)
       soup = BeautifulSoup(response.text, "lxml")

   
    if str(soup).find("Google") == -1:
      
        time.sleep(60)
       
        continue

   
    else:
      
        msg = 'Subject: This is Mounic/'s script talking, CHECK GOOGLE!'
      
        fromaddr = 'YOUR_EMAIL_ADDRESS'
     
        toaddrs  = ['AN_EMAIL_ADDRESS','A_SECOND_EMAIL_ADDRESS', 'A_THIRD_EMAIL_ADDRESS']

      setup the email server,
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
     add my account login name and password,
     server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")

       
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

      send the email
       server.sendmail(fromaddr, toaddrs, msg)
        disconnect from the server
         server.quit()

        break
