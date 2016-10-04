#!/usr/bin/env python3
# coding=utf-8
import requests, sys
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
		sys.exit(1)

def return_menu(soup):
	a = soup.find_all("div", { "class": "widget widgetWysiwyg clearfix" })
	print(a[0].find_all("p"))
	#return(a[0].find_all("p")[0].find_all("p"))
	return(a)

def return_date(soup):
	#return(b[0].find_all("p")[0].text)
	return None

def debug_print(date, menu):
	print(menu[2].text)
		
if __name__ == "__main__":
	file = get_file()

	bs = prepare_bs(file)

	date = return_date(bs)
	menu_list = return_menu(bs)

	debug_print(date, menu_list)
