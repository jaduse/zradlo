#!/usr/bin/env python3
# coding=utf-8
# VRTULE

import requests, sys, re, codecs

def return_menu():
	fs = codecs.open("vrtule.txt", "r", "utf-8")
	vrt = fs.read()
	fs.close()
	jidla = []

	for item in vrt.split("\n"):
		#([0-9]+g)\s+(.*?)\s+([0-9]+\s+Kč)
		a = re.match("([0-9]+g)\s+(.*?)\s+([0-9]+\s+Kč)", item)
		if a is not None:
			print(a.group(1), a.group(2), a.group(3))
			#jidla.append(["{0}{1}".format(a.group(1), a.group(2))], a.group(3))

	return jidla

def return_date():
	#b = soup.find_all("div", { "class": "widget widgetWysiwyg clearfix" })
	#return(b[0].find_all("p")[0].text)
	return ""

def debug_print(date, menu):
	print(date, menu)

def lol():
	date = return_date()
	menu_list = return_menu()

	debug_print(date, menu_list)
	return(date, menu_list)

if __name__ == "__main__":
	date = return_date()
	menu_list = return_menu()
	print(menu_list)

	#debug_print(date, menu_list)
