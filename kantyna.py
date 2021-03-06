#!/usr/bin/env python3
# coding=utf-8
import requests
import re

from bs4 import BeautifulSoup


def get_file():
    response = requests.get(
        "http://www.manihi.cz/zavodni-stravovani-kantyna/"
        "kantyna-rosmarin-business-center/denni-menu"
    )

    if not response or response.status_code != 200:
        return requests.RequestException("Kantyna response error")

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def return_menu(soup):
    date, *menu_items = soup.find_all(
        "div", {"class": "widget widgetWysiwyg clearfix"})[0].find_all("p")

    food = []
    for item in menu_items:
        text = item.text
        match = re.match("(.*?)([0-9]{2,3}\s+Kč)", text)

        if not match:
            continue

        food.append((match.group(1), match.group(2)))

    return (date.text.strip(), food)


#  deprecated
def return_date(soup):
    b = soup.find_all("div", {"class": "widget widgetWysiwyg clearfix"})
    return(b[0].find_all("p")[0].text)


def result():
    try:
        page = get_file()
        date, menu_list = return_menu(page)

        return (date, menu_list)

    except Exception as exp:
        return ("", [str(exp)])


if __name__ == "__main__":
    print(result())
