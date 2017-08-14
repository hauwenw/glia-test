from bs4 import BeautifulSoup
import requests

def crawler(board_name):
    try:
        domain = 'https://www.ptt.cc'
        index = '/bbs/%s/index.html' % board_name
        response = requests.get(domain + index)
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all('div', 'r-ent')
        board = soup.find('a', 'board').getText().strip()
        print(board)
        for post in posts:
            meta = post.find('div', 'title').find('a')
            if(meta):
                title = meta.getText().strip()
                link = meta.get('href')
                date = post.find('div', 'date').getText()
                author = post.find('div', 'author').getText()
                content_response = requests.get(domain + link)
                content_soup = BeautifulSoup(content_response.text, "html.parser")
                content = content_soup.find('div', {'id': 'main-container'}).getText().strip()
            print(date, author, title)
            print(content)
    except:
        print('Cannot find board!')

crawler('NBA')