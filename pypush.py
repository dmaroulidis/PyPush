import httplib, urllib

print "Welcome to PyPush!"
user_key = raw_input("User Key: ")
title = raw_input("Title: ")
message = raw_input("Message: ")
priority = raw_input("Priority (-1, 0, 1, 2): ")

print "The message is being delivered..."

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "amUZ7agu3DxNCvK8bZx1oKWu7smrBq",
    "user": user_key,
    "title": title,
    "message": message,
    "priority": priority,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
