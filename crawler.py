'''
	@author: andrew baumann 
	@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
	@contact: abaumann@columnit.com	
	@additional: using Kimino 
'''

import json

class Crawler:
	def __init__(self):
		with open('kimonoData.json') as data_file:
			self.data = json.load(data_file)

	def add(self,x,y): return x+y
	
	def critic_crawler(self):	
		total = 0
		# print(data["results"]["collection1"][0]["acc_score"])
		acc_list = []

		for x in self.data["results"]["collection1"]:
			acc_list.append(int(x["acc_score"]))
			
		avg_critic = reduce(self.add, acc_list)
		total = avg_critic / len(acc_list)

		print total