'''
	@author: andrew baumann 
	@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
	@contact: abaumann@columnit.com	
	@additional: using Kimino 
'''

import json
import urllib

class Crawler:
	def __init__(self):
		
		self.data_critic = json.load(urllib.urlopen("https://www.kimonolabs.com/api/3xwub6d2?apikey=wy3dBuCMFAFaeHy2nWTQCYliOCKPNvEw"))
		
		self.data_user = json.load(urllib.urlopen("https://www.kimonolabs.com/api/7ewaqu4c?apikey=wy3dBuCMFAFaeHy2nWTQCYliOCKPNvEw"))

		self.years_critic = json.load(urllib.urlopen("https://www.kimonolabs.com/api/8lgonfda?apikey=wy3dBuCMFAFaeHy2nWTQCYliOCKPNvEw"))
		
	def add(self,x,y): return x+y
	
	def years_critic_crawler(self):	
		total = 0
		# print(data["results"]["collection1"][0]["acc_score"])
		acc_list = []

		for x in self.years_critic["results"]["collection1"]:
			acc_list.append(int(x["score"]))
			
		added_acc = reduce(self.add, acc_list)
		total = added_acc / len(acc_list)

		print "Average Score from 1990-2015: " + str(total)
		
		return total
	
		
	def critic_crawler(self):	
		total = 0
		# print(data["results"]["collection1"][0]["acc_score"])
		acc_list = []

		for x in self.data_critic["results"]["collection1"]:
			acc_list.append(int(x["acc_score"]))
			
		added_acc = reduce(self.add, acc_list)
		total = added_acc / len(acc_list)

		print "Accumulated Critic Sum: " + str(total)
		
		return total
	
	def overall_critic_crawler(self):
		total = 0
		
		acc_list = []
		
		for x in self.data_critic["results"]["collection2"]:
			acc_list.append(int(x["overall_score"]))
			
		added_acc = reduce(self.add, acc_list)
		total = added_acc / len(acc_list)
		
		print "Overall Critic Sum: " + str(total)
		
		return total
		
	def user_crawler(self):	
		total = 0
		acc_list = []

		for x in self.data_user["results"]["collection1"]:
			acc_list.append(int(x["acc_score"]))
			
		added_acc = reduce(self.add, acc_list)
		total = added_acc / len(acc_list)

		print "Accumulated User Sum: " + str(total)
		
		return total*10
		
	def overall_user_crawler(self):
		total = 0
		
		acc_list = []
		
		for x in self.data_user["results"]["collection2"]:
			acc_list.append(float(x["overall_user"]))
			
		added_acc = reduce(self.add, acc_list)
		total = added_acc / len(acc_list)
		
		print "Overall User Sum: " + str(total)
		
		return total*10
		
		
		
		
		
		
		