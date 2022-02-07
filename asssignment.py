from bs4 import BeautifulSoup
import requests

surl = 'https://time.com'
html_text = requests.get(surl).text
soup = BeautifulSoup(html_text, 'lxml')
titles = soup.find_all('li', class_='latest-stories__item')
print('[')
for title in titles:
    head_lines = title.find('h3', class_='latest-stories__item-headline').text
    time_stamp = title.find('time', class_='latest-stories__item-timestamp').text.replace("  ", "")
    link_story = title.a['href']
    print('{')
    print(f'"title": "{head_lines.strip()}"')
    print(f'"link": "{surl+link_story}"')
    print('},')
print(']')

