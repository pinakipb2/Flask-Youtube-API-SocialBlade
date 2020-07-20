from flask import Flask, render_template, flash, make_response, url_for, request, redirect
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'socialblade.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://socialblade.com/youtube/realtime',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d332bb3cb61bee07c27ba838d4c093c1a1594972233; PHPSESSXX=uovp347sd08nll1qg09k64o2it; lngtd-sdp=1; __asc=edda55621736c3f8ce989bfe558; __auc=edda55621736c3f8ce989bfe558; _ga=GA1.2.333021533.1595248971; _gid=GA1.2.433748756.1595248971; __qca=P0-583923351-1595248971914; _cb_ls=1; _cb=CVYg6BXuaF1DYnE6E; _cb_svref=null; __gads=ID=e7bb21ac4c248082:T=1595249434:S=ALNI_MZD1y79pJ2PwvJlQlaPyIYjGiUWcg; _chartbeat2=.1595248991325.1595249492944.1.DKdPG7B1m6KUDKzhrZDkhJXKDcNZ5I.2',
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/channel',methods=['POST'])
def channel():
    channel_name = request.form.get('name')
    params = (
    ('query', channel_name),
)
    r = requests.get('https://socialblade.com/youtube/search/search', headers=headers, params=params)
    soup = BeautifulSoup(r.text,'html.parser')
    a = (soup.findAll('a', {"class": "core-button core-small ui-black"})[0])
    channel_id = a.get('href')
    channel_url = "https:" + channel_id
    
    
    divTag = soup.findAll("div",{"style":"width: 1200px; height: 88px; background: #fff; padding: 15px 30px; margin: 2px auto; border-bottom: 2px solid #e4e4e4;"})[0]
    
    name1 = divTag.p.text
    
    divTag = soup.findAll("div",{"style":"width: 1200px; height: 88px; background: #fff; padding: 15px 30px; margin: 2px auto; border-bottom: 2px solid #e4e4e4;"})[1]
    
    name2 = divTag.p.text
    
    desc = name1 + name2
    
    divTag = soup.findAll("span",{"style":"font-size: 0.9em; background: #f6f6f6; padding: 2px 5px; border: 1px solid #e2e2e2; color:#666;"})[0]
    
    uploads = divTag.text
    
    divTag = soup.findAll("span",{"style":"font-size: 0.9em; background: #f6f6f6; padding: 2px 5px; border: 1px solid #e2e2e2; color:#666;"})[1]
    
    subs = divTag.text
    
    divTag = soup.findAll("span",{"style":"font-size: 0.9em; background: #f6f6f6; padding: 2px 5px; border: 1px solid #e2e2e2; color:#666;"})[2]
    
    views = divTag.text
    
    return render_template('details.html',channel_url=channel_url,desc=desc,channel_name=channel_name,subs=subs,views=views,uploads=uploads)

if __name__ == '__main__':
    app.run(debug=True)