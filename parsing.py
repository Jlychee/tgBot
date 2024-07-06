import time

from bs4 import BeautifulSoup

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#smbツ#000

def get_url(nickname, s):
    return f'https://tracker.gg/valorant/profile/riot/{nickname.replace("#", "%23")}/overview{s}'

def get_source_html(url):
    service = Service(
        executable_path=r'C:\Users\Катя\Documents\GitHub\tg_bot_test\chromedriver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={UserAgent.random}')
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url=url)
        time.sleep(3)
        with open(r'.source_page.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        pass
    finally:
        driver.close()
        driver.quit()


def get_items_urls(file_path):
    data_info = {}

    with open(file_path) as file:
        scr = file.read()

    soup = BeautifulSoup(scr, 'lxml')

    data_info['Current Rating'] = soup.find('div', class_='rating-entry__rank').find('div', class_='value').text
    data_info['Peak Rating'] = soup.find('div',
                                         class_='rating-summary__content rating-summary__content--secondary').find(
        'div', class_='value').text
    data_info['Level'] = \
        soup.find('div', class_='flex flex-1 flex-row gap-8 items-center justify-between').find_all('span',
                                                                                                    class_='stat__value')[
            1].text
    play_time = soup.find('span', class_='playtime').text.split()
    if len(play_time) == 2:
        data_info['Playtime'] = play_time[0]
    else:
        data_info['Playtime'] = ''.join(play_time[:-1])
    data_info['Matches'] = soup.find('span', class_='matches').text.split()[0]
    data_info['Top agent'] = soup.find('div', class_='top-characters trn-card trn-card--bordered').find('div',
                                                                                                        class_='st-content__item').find(
        'div', class_='value').text
    data = soup.find_all('div', class_='stat align-left giant expandable')
    for i in data:
        data_info[i.find('span', class_='name').text] = i.find('span', class_='value').text
    return data_info
