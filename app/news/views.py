from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

hn = 'https://thehackernews.com/'

hn_list = []


def get_hn():
    r = requests.get(hn).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='body-post clear')
    for post in posts:
        title = post.find('h2', class_='home-title').text
        url = post.find('a').get('href')
        image = post.find('img').get('data-src')
        pub_date = post.find('div', class_='item-label').text[1:18]
        data = {'title': title,
                'url': url,
                'image': image,
                'pub_date': pub_date
                }
        hn_list.append(data)


get_hn()


def news(requests):
    context = {
        'hn_list': hn_list,
    }
    return render(requests, 'news/news.html', context)
