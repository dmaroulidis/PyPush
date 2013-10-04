import httplib, urllib

def connect_send_getresponse() :
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.urlencode({
        "token": "amUZ7agu3DxNCvK8bZx1oKWu7smrBq",
        "user": user_key,
        "title": title,
        "message": message,
        "url": url,
        "url_title": url_title,
        "priority": priority,
        "retry": retry,
        "expire": expire,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

print "Welcome to PyPush!"
user_key = raw_input("User Key: ")
title = raw_input("Title: ")
message = raw_input("Message: ")
url = raw_input("Supplementary URL (optional): ")
url_title = raw_input("Supplementary URL Title (optional): ")
retry = 0
expire = 0
priority = raw_input("Priority (-1, 0, 1, 2): ")

if priority == "2":
    retry = raw_input("How often the will message be sent? (In seconds) ")
    expire = raw_input("When will the message stop being sent? (In seconds) ")
    connect_send_getresponse()
else:
    connect_send_getresponse()

print "Message sent."
