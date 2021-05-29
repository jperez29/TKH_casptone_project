import requests
import sys

from bs4 import BeautifulSoup
from typing import Dict, List


HEADERS: Dict[str, str] = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
TECH_LIST: List[str] = ['HTML', 'CSS', 'JavaScript', 'PHP', 'Angular', 'React', 'Vue', 'TypeScript', 'Node.JS', 'Swift', 'Java', 'jQuery', 'C++']

# Query params
JOB_TITLE: str = 'front end developer'
CITY: str = 'New York'
STATE: str = 'NY'


def fill_spaces_with_plus_sign(string: str) -> str:
    return '+'.join(string.split())


def prepare_location(city: str, state: str) -> str:
    city: str = fill_spaces_with_plus_sign(city)
    state: str = fill_spaces_with_plus_sign(state)

    return f'{city}%2C+{state}'


def generate_indeed_url(job_title: str, city: str, state: str, start_page: int = 0) -> str:
    job_title:str = fill_spaces_with_plus_sign(job_title)
    location: str = prepare_location(city, state)

    return f'https://www.indeed.com/jobs?q={job_title}&l={location}&start={start_page}'


def send_request(indeed_url: str):
    try:
        r = requests.get(indeed_url, HEADERS)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def parse_job_title(request_job_fields: List[str]) -> str:
    return request_job_fields[0]


def parse_company(request_job_fields: List[str]) -> str:
    return request_job_fields[1]


def parse_html(soup) -> Dict[str, Dict[str,str]]:
    job_results: Dict[str, Dict[str,str]] = {}

    if soup:
        divs = soup.find_all(id ="mosaic-provider-jobcards")
        a_tags = soup.find_all('a', class_ = 'result')

        for item in a_tags:
            job_url: str = 'indeed.com' + item.get('href')

            job_data: Dict[str, str] = {'job_title': '', 'company': ''}

            request_job_fields: List[str] = list(filter(lambda ele: ele != 'new', list(item.stripped_strings)))

            job_data['job_title'] = parse_job_title(request_job_fields)
            job_data['company'] = parse_company(request_job_fields)

            job_results[job_url] = job_data
    else:
        print('Soup is empty')
        sys.exit()

    return job_results

'''
def extract_func():
    url = f"https://www.indeed.com/viewjob?jk=382c2afc58e7307a&tk=1f663vu84u2n4800&from=serp&vjs=3"
    r = requests.get(url, HEADERS)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform_func(soup):
    body = divs = soup.find_all(id ="jobDescriptionText")
    text = ''
    for item in body:
        text += str(list(item.stripped_strings))
    list_of_tech = ['HTML', 'CSS', 'JavaScript', 'PHP', 'Angular', 'React', 'Vue', 'Typescript', 'Node.JS', 'Swift', 'Java', 'jQuery']
    dct = {}
    print(len(list(text)))
#     for item in list_of_tech:
#         for word in list(text):
#             if item in word:
#                 print(f'{item} is here')
#                 if item not in dct.keys():
#                     dct[item] =1
#                 else:
#                     dct[item] += 1
    print(dct)

#     lst = []
#     for item in body:
#         print(lst.append(list(item.stripped_strings)))
#     print(lst)


dct_front_end = {}
for item in list_of_tech:
    if item in body_job_description:
        append to dct_front_end
            dct[item] +=1
'''


def main():
    indeed_url: str = generate_indeed_url(JOB_TITLE, CITY, STATE)

    soup = send_request(indeed_url)

    job_results: Dict[str, Dict[str,str]] = parse_html(soup)
    print(job_results)

    #d = extract_func()

    #transform_func(d)

if __name__ == '__main__':
    main()
