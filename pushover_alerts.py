import http.client
import urllib.parse

def pushover(apiurl,token,user,msg):
  conn = http.client.HTTPSConnection(apiurl)
  conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": token,
    "user": user,
    "message": msg,
  }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()
