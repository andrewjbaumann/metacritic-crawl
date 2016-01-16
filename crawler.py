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
		self.user_data = list()
		self.critic_data = list()
		self.metacritic_base_url = "http://www.metacritic.com/browse/replace/score/metascore/all/filtered?sort=desc&page="
		self.metacritic_year_url = "http://www.metacritic.com/browse/<genre>/score/metascore/year/filtered?view=condensed&year_selected=<year>&sort=desc&page="
		self.years_dict = dict()		
		
	def add(self,x,y): return x+y
	def calc_avg(self,data): return float(reduce(lambda x, y: x+y, data) / len(data))
	
	def set_crawl(self):
		manager = Manager()
		self.user_data = manager.list()
		self.critic_data = manager.list()
		
		movies_url = self.metacritic_base_url.replace("replace","movies")
		games_url = self.metacritic_base_url.replace("replace","games")
		albums_url = self.metacritic_base_url.replace("replace","albums")
		tv_url = self.metacritic_base_url.replace("replace","tv")
		
		pMovie = Process(target=self.metacritic_scrapper, args=(movies_url, "Movies"))		
		pGames = Process(target=self.metacritic_scrapper, args=(games_url, "Games"))	
		pMusic = Process(target=self.metacritic_scrapper, args=(albums_url, "Music"))	
		pTV = Process(target=self.metacritic_scrapper, args=(tv_url, "TV"))
		
		pTV.start()
		pMovie.start()
		pMusic.start()
		pGames.start()
		
		pTV.join()
		pMovie.join()
		pMusic.join()
		pGames.join()
		
		f = open('results.txt ', 'w')
		f.write(str(self.user_data) + "\n\n" + str(self.critic_data))
		
		user_avg = self.calc_avg(self.user_data)
		critic_avg = self.calc_avg(self.critic_data)
		
		print "\nUser average: " + str(user_avg)
		print "Critic average: " + str(critic_avg)
		print "Overall average: " + str(self.calc_avg([user_avg, critic_avg]))
		
	def year_crawl(self):
		manager = Manager()
		self.data = manager.list()
		
		movies_url = self.metacritic_year_url.replace("genre","movies")
		movies_url = self.metacritic_year_url.replace("genre","games")
		movies_url = self.metacritic_year_url.replace("genre","albums")
		movies_url = self.metacritic_year_url.replace("genre","tv")
		
		
	def metacritic_scrapper(self, url, purpose):
		for page in range (0,1):				
			req = urllib2.Request(url + str(page), headers={'User-Agent' : "Magic Browser"})
			html = urlopen(req)
			soup = BeautifulSoup(html, "lxml")
			try:
				self.critic_scrapper(soup)
				self.user_scrapper(soup)
				print purpose + " Page Complete: " + str(page)
			except TypeError:	
				print purpose + " Page Failed: " + str(page)
				break

	def critic_scrapper(self,soup):
		data = [sc.div.string for sc in soup.find_all("div","product_score")]
		if type(data[-1]) != type(data[0]):
			del data[-1]
		data = [int(i) for i in data]
		self.critic_data.extend(data)
	
	def user_scrapper(self,soup):
		data = [sc.string for sc in soup.find_all("span","data textscore textscore_favorable")]
		filter(lambda x: x == "tbd", data)
		if type(data[-1]) != type(data[0]):
			del data[-1]
		data = [int(float(i)*10) for i in data]
		self.user_data.extend(data)
	