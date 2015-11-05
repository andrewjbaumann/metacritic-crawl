'''
	@author: andrew baumann 
	@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
	@contact: abaumann@columnit.com	
	@additional: using Kimino 
'''

import json
import urllib
import urllib2
import pprint
import time
import bs4
from urllib2 import urlopen
from bs4 import BeautifulSoup 

BASE_URL = "http://www.metacritic.com/browse/movies/score/metascore/all/filtered?sort=desc&page="

class Crawler:
	def __init__(self):
		self.print_string = ""
		self.query = ""
		self.data = list()
		
	def add(self,x,y): return x+y
	
	def set_json(self,data_name):
		if data_name == "metacritic-critics":
			self.print_string = "Metacritic Critic's Average: "
			self.query = "score"
			self.data = list()
		
	def webscrapper_test(self, page):
		for page in range (0,89):	
			# print "Waiting.",
			# time.sleep(.3)
			# print ".",
			# time.sleep(.3)
			# print "."
			
			req = urllib2.Request(BASE_URL + str(page), headers={'User-Agent' : "Magic Browser"})
			html = urlopen(req)
			soup = BeautifulSoup(html, "lxml")
			metasoup = soup.find("div", "content_section mpu_layout")
			try: 
				temp_data = [sc.div.string for sc in metasoup.find_all("div","product_score")]
				if type(temp_data[-1]) != type(temp_data[0]):
					print type(temp_data[-1])
					del temp_data[-1]
				temp_data = [int(i) for i in temp_data]
				self.data.extend(temp_data)
				# pprint.pprint(temp_data)
				print len(temp_data)
				print "Page Complete: " + str(page)
			except TypeError:	
				pprint.pprint(temp_data)
				print len(temp_data)
				print "Page Failed: " + str(page)

		
		f = open('results.tx', 'w')
		f.write(str(self.data))
		return



		
		
		