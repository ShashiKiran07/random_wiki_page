from flask import Blueprint, jsonify, request
import requests
from bs4 import BeautifulSoup
import sys

import random
import re

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def find_wiki():
    wiki_link = "https://en.wikipedia.org/wiki/cat"


    response = requests.get(wiki_link)
    response.raise_for_status()
    # soup = BeautifulSoup(response.content, 'html.parser')
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.get_text()
    summary = ''
    for i in soup.select('p'):
        summary += i.get_text()
    summary = summary[:500] + ' .....'
    for link in soup.find_all('a'):
        print(link.get('href'))
    result = []
    result.append({'link' : wiki_link, 'title' : title, 'summary':summary})
    print(result)
    return jsonify({'result':result})
