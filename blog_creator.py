from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import smtplib
import requests
import random


# to schedule the task uncomment the line below:
# from datetime import datetime

KEY = "YOUR BLOGIN API KEY" 
URL = "https://blogin.co/api/rest/posts"
# News API url: https://newsapi.org/
NEWS_API_KEY = 'YOUR NEWS API KEY'
NEWS_API_URL = 'https://newsapi.org/v2/everything'
KEY_WORD = input("What would you like to talk about? Google, Google Workspace, Jumpcloud etc..: ").title()

google_news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": KEY_WORD
}

current_date = datetime.now()
time = current_date.isoformat()

google_news_response = requests.get(NEWS_API_URL, params=google_news_parameters)

articals_lenth = len(google_news_response.json()["articles"])
rand_num = random.randint(0, articals_lenth)

title = google_news_response.json()["articles"][rand_num]["title"]
content = google_news_response.json()["articles"][rand_num]["content"]
url = google_news_response.json()["articles"][rand_num]["url"]
description = google_news_response.json()["articles"][rand_num]["description"]


def send_email_success():
    email = 'YOUR EMAIL'
    password = 'YOUR APP PASSWORD'
    send_to_email = 'DESTINATION EMAIL'
    subject = "Blogin Blog been created, approve it now!"
    message = "Hi new features and updates released " \
              "and a Blogin post been created waiting for your approval here:" \
              "https://pipl.blogin.co/my-posts/#published please notice that the post will be published 1 hour from now" \
              "automatically you have the option to EDIT or DELETE the post for only 1 hour."

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Attach the message to the MIMEMultipart msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()

    # You now need to convert the MIMEMultipart object to a string to sendfor _ in range(20):
    server.sendmail(email, send_to_email, text)
    server.quit()



json = {
    "title": f"{title}",
    "text": f"<p>👋 Welcome, great to have you here.</p>"
            f"<p>{content}</p>"
            f"<p>{description}</p>"            
            f"<p><a href={url}>Read More</a></p>",
    "published": True,
    "wiki": False,
    "important": False,
    "pinned": False,
    "date_published": f"{time[0:19]}+01:00",
    "visibility_team": [
        {
            "id": ID,
            "name": "DEPARTMENT NAME",
            "position": POSITION,
            "locked": False
        }
    ],
    "notify": False,
    "author": {
        "id": "ID"
    },
    "categories": [
        {
            "id": "ID",
        }
    ]
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {KEY}',
}

response = requests.post(URL, json=json, headers=headers)

send_email_success()


print(f"\n\nYEAAS🎉🎉🎉!!, Blog created Successfully!\nSee:👇🏼\nhttps://pipl.blogin.co/my-posts/#published\n\n")
