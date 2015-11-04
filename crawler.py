'''
	@author: andrew baumann 
	@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
	@contact: abaumann@columnit.com	
	@additional: using Kimino 
'''

import json
import urllib
from bs4 import BeautifulSoup 

class Crawler:
	def __init__(self):
			self.print_string = ""
			self.query = ""
			self.data = {}
			self.data_two = {}
			self.data_three = {}
		
	def add(self,x,y): return x+y
	
	def set_json(self,data_name):
		if data_name == "metacritic-critics":
			self.print_string = "Metacritic Critic's Average: "
			self.query = "score"
			self.data = json.load(urllib.urlopen("https://www.kimonolabs.com/api/54z63qyw?apikey=wy3dBuCMFAFaeHy2nWTQCYliOCKPNvEw"))
			self.data_two = json.load(urllib.urlopen("https://www.kimonolabs.com/api/d44be2pm?apikey=wy3dBuCMFAFaeHy2nWTQCYliOCKPNvEw"))
			self.data_three = json.load(urllib.urlopen("https://www.kimonolabs.com/api/biec8bjm?apikey=wy3dBuCMFAFaeHy2nWTQCYliOCKPNvEw"))
		
	def super_crawler(self):
		total = 0
		# print(data["results"]["collection1"][0]["acc_score"])
		acc_list = []
			
		if self.data:
			for x in self.data["results"]["collection1"]:
				acc_list.append(int(x[self.query]))
		if self.data_two:
			for x in self.data_two["results"]["collection1"]:
				acc_list.append(int(x[self.query]))
		if self.data_three:
			for x in self.data_three["results"]["collection1"]:
				acc_list.append(int(x[self.query]))
				
		self.data = {}
		self.data_two = {}
		self.data_three = {}

		added_acc = reduce(self.add, acc_list)
		total = added_acc / len(acc_list)

		print self.print_string + str(total)
		
		return total