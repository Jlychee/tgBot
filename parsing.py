import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

data_info = {}


def get_info(nickname, season=''):
    nickname = nickname.replace(' ', '%20').replace('#', '%23')
    url = f'https://tracker.gg/valorant/profile/riot/{nickname}/overview{season}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    data_info['Current Rating'] = soup.find('div', class_='rating-entry__rank').find('div', class_='value').text
    data_info['Peak Rating'] = soup.find('div',
                                         class_='rating-summary__content rating-summary__content--secondary').find(
        'div', class_='value').text
    data_info['Level'] = \
        soup.find('div', class_='flex flex-1 flex-row gap-8 items-center justify-between').find_all('span',
                                                                                                    class_='stat__value')[
            1].text
    data_info['Playtime'] = soup.find('span', class_='playtime').text.split()[0]
    data_info['Matches'] = soup.find('span', class_='matches').text.split()[0]
    data_info['Top agent'] = soup.find('div', class_='top-characters trn-card trn-card--bordered').find('div',
                                                                                                        class_='st-content__item').find(
        'div', class_='value').text
    data = soup.find_all('div', class_='stat align-left giant expandable')
    for i in data:
        data_info[i.find('span', class_='name').text] = i.find('span', class_='value').text
    return data_info
