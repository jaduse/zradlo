#!/usr/bin/env python3
# coding=utf-8
# VRTULE

import requests, sys, re
from bs4 import BeautifulSoup

def get_file():
	kantyna = requests.get("http://uvrtulejidelna.webnode.cz/sluzby/")
	return kantyna

def prepare_bs(kantyna):
	if kantyna is not None and kantyna.status_code == 200:
		html = kantyna.text
		soup = BeautifulSoup(html, 'html.parser')
		return soup

	else:
		sys.exit(1)

def return_menu(soup):
	a = soup.find_all("p", style="margin-left:132px;")
	for item in a:
		

def return_date(soup):
	#b = soup.find_all("div", { "class": "widget widgetWysiwyg clearfix" })
	#return(b[0].find_all("p")[0].text)
	return ""

def debug_print(date, menu):
	print(date)

def lol():
	file = get_file()

	bs = prepare_bs(file)

	date = return_date(bs)
	menu_list = return_menu(bs)

	debug_print(date, menu_list)
	return(date, menu_list)

if __name__ == "__main__":
	file = get_file()

	bs = prepare_bs(file)

	date = return_date(bs)
	menu_list = return_menu(bs)
	print(menu_list)

	#debug_print(date, menu_list)
