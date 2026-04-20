# tgBotValorant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/aiogram-3.9-2C2D72?style=for-the-badge&logo=telegram&logoColor=white" alt="aiogram">
  <img src="https://img.shields.io/badge/Selenium-4.22-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/BeautifulSoup4-4.12-8B4513?style=for-the-badge" alt="BeautifulSoup4">
  <img src="https://img.shields.io/badge/Tracker.gg-Valorant_stat-blue?style=for-the-badge" alt="Tracker.gg">
</p>

tgBotValorant — Telegram-бот, который позволяет быстро посмотреть статистику игрока в Valorant и получить случайного агента под настроение.

## Table of Contents

- [About](#about)
- [How it works](#how-it-works)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Project structure](#project-structure)
- [Authors](#authors)

## About

Проект сделан как Telegram-бот для игроков в Valorant.

Бот умеет:
- показывать статистику игрока по нику Riot;
- выдавать данные за текущий сезон или за все сезоны;
- случайно выбирать агента в режиме `mood`;
- отправлять картинку и описание настроения.

Статистика собирается через парсинг страницы профиля на tracker.gg, а взаимодействие с пользователем построено на inline-кнопках и командах Telegram.

## How it works

### 1. Старт бота

После `/start` бот показывает основные кнопки:
- получить статистику игрока;
- узнать, какой ты сегодня агент.

### 2. Получение статистики

Пользователь выбирает, нужна ли статистика:
- только за текущий сезон;
- за все сезоны.

После этого бот просит ввести ник в формате:

```text
!nickname#tag
```

Например:

```text
!ValenOK#top
```

Дальше бот открывает страницу игрока на tracker.gg, вытаскивает основные показатели и отправляет их в чат.

### 3. Режим mood

По команде `/mood` или через кнопку бот случайно выбирает изображение из папки `Mood/` и показывает, какой ты сегодня агент по вайбу.

## Installation

Клонируйте репозиторий:

```bash
git clone https://github.com/Jlychee/tgBotValorant.git
cd tgBotValorant
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Что нужно подготовить перед запуском:
- указать Telegram Bot Token в конфиге, так как бот запускается через `config.TOKEN`;
- настроить путь к ChromeDriver, потому что в парсере используется Selenium;
- убедиться, что папка `Mood/` с изображениями находится рядом с проектом.

Запуск:

```bash
python run.py
```

## Tech Stack

- Python
- aiogram
- Selenium
- BeautifulSoup4
- lxml
- fake-useragent

## Project structure

- `run.py` — запуск Telegram-бота
- `main.py` — команды, callback-обработчики и клавиатуры
- `parsing.py` — парсинг статистики игрока с tracker.gg
- `img_path.py` — выбор случайной картинки из папки `Mood`
- `Mood/` — изображения для режима настроения
- `chromedriver/` — драйвер для Selenium
- `requirements.txt` — зависимости проекта

## Authors

- [Jlychee](https://github.com/Jlychee)

