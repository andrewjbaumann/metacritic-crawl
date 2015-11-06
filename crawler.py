'''
@author: andrew baumann 
@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
@contact: abaumann@columnit.com	
@additional: using BeautifulSoup
'''

import json
import urllib
import urllib2
import pprint
import time
import bs4
from multiprocessing import Process, Manager
from urllib2 import urlopen
from bs4 import BeautifulSoup 

class Crawler:
	def __init__(self):
		self.print_string = ""
		self.query = ""
		self.data = list()
		self.metacritic_base_url = "http://www.metacritic.com/browse/replace/score/metascore/all/filtered?sort=desc&page="
		self.avg = 0
		
	def add(self,x,y): return x+y
	def calc_avg(self): self.avg = float(reduce(lambda x, y: x+y, self.data) / len(self.data))
	def print_avg(self): print self.avg
	
	def set_crawl(self):
		manager = Manager()
		self.data = manager.list()
		
		movies_url = self.metacritic_base_url.replace("replace","movies")
		games_url = self.metacritic_base_url.replace("replace","games")
		albums_url = self.metacritic_base_url.replace("replace","albums")
		tv_url = self.metacritic_base_url.replace("replace","tv")
		
		pMovie = Process(target=self.metacritic_webscrapper, args=(89, movies_url, "Movies"))		
		pGames = Process(target=self.metacritic_webscrapper, args=(127, games_url, "Games"))	
		pMusic = Process(target=self.metacritic_webscrapper, args=(95, albums_url, "Music"))	
		pTV = Process(target=self.metacritic_webscrapper, args=(17, tv_url, "TV"))
		
		pTV.start()
		pMovie.start()
		pMusic.start()
		pGames.start()
		
		pTV.join()
		pMovie.join()
		pMusic.join()
		pGames.join()
		
		f = open('results.txt ', 'w')
		f.write(str(self.data))
		
		self.calc_avg()
		
	def metacritic_webscrapper(self, max_page, url, purpose):
		for page in range (0,4):				
			req = urllib2.Request(url + str(page), headers={'User-Agent' : "Magic Browser"})
			html = urlopen(req)
			soup = BeautifulSoup(html, "lxml")
			metasoup = soup.find("div", "content_section mpu_layout")
			try: 
				temp_data = [sc.div.string for sc in metasoup.find_all("div","product_score")]
				if type(temp_data[-1]) != type(temp_data[0]):
					del temp_data[-1]
				temp_data = [int(i) for i in temp_data]
				self.data.extend(temp_data)
				print purpose + " Page Complete: " + str(page)
			except TypeError:	
				print purpose + " Page Failed: " + str(page)

		self.data.extend(temp_data)		
	