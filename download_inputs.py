import os
import time
import configparser
import requests


def download(year: int, day: int, cookies: dict, force=False, waiting: float = 0.5):
    dir = f'{year}/{day}'
    input_file = f'{dir}/input.txt'
    if not force and os.path.exists(input_file):
        return
    os.makedirs(dir, exist_ok=True)
    print(f'Downloading input of year {year}, day {day}...')
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)

    with open(input_file, 'w+') as f:
        f.write(res.text)

    time.sleep(waiting)


# read config
config = configparser.ConfigParser()
config.read('config.ini')
cookies = dict(
    session=config['Cookies']['session']
)

year = 2020
day = 1


# for year in range(2015,2023):
# for year in range(2022,2023):
#     for day in range(1,16):
#         download(year, day, cookies)

download(2022,3,cookies)
