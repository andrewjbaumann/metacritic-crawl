'''
@author: andrew baumann 
@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
@contact: abaumann@columnit.com	
@additional: using BeautifulSoup
'''
import json 
import urllib
import urllib2
# import time
import bs4
from multiprocessing import Process, Manager
from itertools import chain 
from urllib2 import urlopen
from bs4 import BeautifulSoup 
ns = '\n'

class Crawler:
	def __init__(self):
		self.data = list()
		self.udata = list()
		self.cdata = list()
		self.metacritic_base_url = "http://www.metacritic.com/browse/replace/score/metascore/all/filtered?sort=desc&page="
		self.metacritic_year_url = "http://www.metacritic.com/browse/<genre>/score/metascore/year/filtered?view=condensed&year_selected=<year>&sort=desc&page="
		
	def add(self,x,y): return x+y
	def calc_avg(self,data): return float(reduce(lambda x, y: x+y, data) / len(data))
	
	def set_crawl(self):
		manager = Manager()
		self.data = manager.list()
		
		movies_url = self.metacritic_base_url.replace("replace","movies")
		games_url = self.metacritic_base_url.replace("replace","games")
		albums_url = self.metacritic_base_url.replace("replace","albums")
		tv_url = self.metacritic_base_url.replace("replace","tv")
		
		pMovie = Process(target=self.metacritic_scrapper, args=(movies_url, "Movies"))		
		# pGames = Process(target=self.metacritic_scrapper, args=(games_url, "Games"))	
		# pMusic = Process(target=self.metacritic_scrapper, args=(albums_url, "Music"))	
		# pTV = Process(target=self.metacritic_scrapper, args=(tv_url, "TV"))
		
		pMovie.start()
		# pMusic.start()
		# pGames.start()
		# pTV.start()
		
		pMovie.join()
		# pMusic.join()
		# pGames.join()
		# pTV.join()
		
		f = open('results.txt ', 'w')
		f.write(str(self.udata) + "\n\n" + str(self.cdata))
		
		user_avg = self.calc_avg(self.udata)
		critic_avg = self.calc_avg(self.cdata)
		
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
			self.critic_scrapper(soup)
			print purpose + " Page Complete: " + str(page)
			# try:
			# except TypeError:	
				# print purpose + " Page Failed: " + str(page)
				# break

	def critic_scrapper(self,soup):
		data_coll = list()
		c_scores = list()
		u_scores = list()
		
		rows = [rw for rw in soup.find_all("div","product_row movie")]
		
		for x in rows:
		#Title = Product Title, Url = Product's MC page
		#CS = Critic Score, US = User Score
			title = x.find("div", class_="product_item product_title").a.string.strip() 
			url = x.find("div", class_="product_item product_title").a.get("href")	
			cs = x.find("div", class_="product_item product_score").div.string
			us = x.find("div", class_="product_item product_userscore_txt").select("span:nth-of-type(2)")[0].string
			
			data_coll.extend((title,url,cs,us))
			
			if us != "tbd":
				us = int(float(us)*10) 
				
			cs = int(cs)
			
			c_scores.extend(cs)			
			u_scores.extend(us)

		
		if type(c_scores[-1]) != type(c_scores[0]):
			del c_scores[-1]
		if type(u_scores[-1]) != type(u_scores[0]):
			del u_scores[-1]
	
		# c_scores = [int(i) for i in c_scores]
		
		# u_scores = [int(float(i)*10) for i in u_scores]
		
		self.data.extend(data_coll)
		self.udata.extend(u_scores)
		self.cdata.extend(c_scores)

		
		
		
		
		
		
		
		
		
		
