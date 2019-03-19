import requests
from bs4 import BeautifulSoup
import bs4
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.before_request   #钩子
def app_before_request():
  print("HTTP {}  {}".format(request.method, request.url))

@app.route("/API",methods=["POST"])
def button_api():
  textApi = request.json.get("textApi")
  return jsonify({
    "status":2,
    "message":"{},pachou".format(textApi)
    }),200

def getHEAD(url):
  try:
    r = requests.get(url,timeout = 400)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    return html
  except:
      print('解析失败')

def getTITTLE(html):
  soup = BeautifulSoup(html,'html.parser')
  tittle = soup.select('.entry-title ')
  for a in tittle:
      print(a.string) 

  soup = BeautifulSoup(html,'html.parser')    
  time = soup.select('.posted-date')
  for span in time:
      print(span.string)

                    

def main():
  url = "https://snowstar.org/"
  html = getHEAD(url)
  getTITTLE(html)
                     
main()




if __name__ == '__main__':
  app.run(port=5000, debug=True)  
  