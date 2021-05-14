import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    url = f"https://www.indeed.com/jobs?q=python&l=New+York%2C+NY&start={page}"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ ="tapItem result job_e8f18d2cffb5cb7d sponsoredJob saved resultWithShelf sponTapItem tapItem-noPadding desktop")
    return len(divs)

c = extract(0)
print(transform(c))