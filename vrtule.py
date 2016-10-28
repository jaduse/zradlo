#!/usr/bin/env python3
# coding=utf-8
# VRTULE

import os
import requests
import re
import tempfile

from bs4 import BeautifulSoup
from subprocess import check_output


# TODO: POLIVKY+posledni radky, co nemaj \t
# TODO: POLIVKY+posledni radky, co nemaj \t
# TODO: POLIVKY+posledni radky, co nemaj \t
# TODO: POLIVKY+posledni radky, co nemaj \t
# TODO: POLIVKY+posledni radky, co nemaj \t

_, TMP = tempfile.mkstemp()


def get_file():
    response = requests.get("http://uvrtulejidelna.webnode.cz/sluzby/")

    if response.status_code != 200:
        raise requests.RequestException("Error: Vrtule response error")

    html = response.text
    bs = BeautifulSoup(html, "html.parser")

    content_div = bs.find_all("div", {"class": "box_content"})[-1]

    for a in content_div.find_all("a", href=True):
        url = a["href"]
        if ".doc" in url:
            doc_url = url

    doc_stream = requests.get(doc_url, stream=True)
    with open(TMP, "wb") as f:
        for chunk in doc_stream.iter_content(chunk_size=1024):
            f.write(chunk)

    antiword = check_output(["antiword", TMP]).decode("utf8")

    return antiword


def return_menu(antiword):
    lines = [l for l in antiword.split("\n") if l]

    food = []
    date = lines[2].strip()

    for item in lines[2:]:
        match = re.match("\s+?([0-9]+g)\s+(.*?)\s+([0-9]+\s+Kč)", item)
        if not match:
            continue

        food.append((
            match.group(1),
            match.group(2),
            match.group(3)
        ))

    return (date, food)


def debug_print(date, menu):
    print(date, menu)


def result():
    try:
        page = get_file()
        date, menu_list = return_menu(page)

        return (date, menu_list)
    except:
        return ("Chyba", ["", "", ""])

    os.remove(TMP)

if __name__ == "__main__":
    print(result())
