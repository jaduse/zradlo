#!/usr/bin/env python3
# coding=utf-8
import requests, sys, re
from bs4 import BeautifulSoup

def get_file():
	kantyna = requests.get("http://www.chutpoint.cz/denni-nabidka/")
	return kantyna

def prepare_bs(kantyna):
	if kantyna is not None and kantyna.status_code == 200:
		html = kantyna.text
		soup = BeautifulSoup(html, 'html.parser')
		return soup

	else:
		return "Error"

def return_menu(soup):
	a = soup.find("div", { "class": "widget widgetWysiwyg clearfix" })
	b = a.findNext("h1")
	c = b.findNext("p").text
	d = [c, ""]
	print(d)

	"""for i in items_orig:
		items.append(i.text)
		print(i.text)
		print("\n")"""

	return(d)


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
		print(date, menu_list)
		return(date, menu_list)
	except:
		return("", [])

if __name__ == "__main__":
	file = get_file()

	bs = prepare_bs(file)

	date = return_date(bs)
	menu_list = return_menu(bs)
	lol()
	print(menu_list)

	#debug_print(date, menu_list)
