import requests
import urllib.request
from bottle import route, run, template, redirect, request
from bs4 import BeautifulSoup


@route("/")
def index():
    info1 = get_info_sunday()
    return template("index", out1=info1)


def get_info_sunday():
    url = 'http://baseson.nexton-net.jp/koihime-portal/'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '        'AppleWebKit/537.36 (KHTML, like Gecko) '        'Chrome/78.0.3904.108 Safari/537.36'
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    topicsindex = soup.find('section', attrs={'class': 'b-box'})
    info = [a.string for a in topicsindex.find_all("p")]
    return(info)


run(host="localhost", port=1055, debug=True, reloader=True)
