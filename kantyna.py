#!/usr/bin/env python3
# coding=utf-8
import requests, sys, re
from bs4 import BeautifulSoup

def get_file():
	kantyna = requests.get("http://www.manihi.cz/zavodni-stravovani-kantyna/kantyna-rosmarin-business-center/denni-menu")
	return kantyna

def prepare_bs(kantyna):
	if kantyna is not None and kantyna.status_code == 200:
		html = kantyna.text
		soup = BeautifulSoup(html, 'html.parser')
		return soup

	else:
		return "Error"

def return_menu(soup):
	a = soup.find_all("p", style="margin-left:132px;")
	items = []
	for item in a:
		if "CHCETE" not in item.text:
			print(item.text)
			text = item.text
			split = text.split("–")
			meme = [split[0]]
			meme.append(re.split("\s{2,}", split[1])[0])
			meme.append(re.split("\s{2,}", text)[1])
			items.append(meme)
	return items


def return_date(soup):
	b = soup.find_all("div", { "class": "widget widgetWysiwyg clearfix" })
	return(b[0].find_all("p")[0].text)

def debug_print(date, menu):
	print(date)

def lol():
	try:
		file = get_file()

		bs = prepare_bs(file)

		date = return_date(bs)
		menu_list = return_menu(bs)

		debug_print(date, menu_list)
		return(date, menu_list)
	except:
		return None

if __name__ == "__main__":
	file = get_file()

	bs = prepare_bs(file)

	date = return_date(bs)
	menu_list = return_menu(bs)
	print(menu_list)

	#debug_print(date, menu_list)
