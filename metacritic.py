'''
	@author: andrew baumann 
	@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
	@contact: abaumann@columnit.com	
	@additional: using Kimino 
'''
import json
from multiprocessing import Process, freeze_support
from crawler import Crawler

def add(x,y): return x+y

if __name__ == '__main__':
	freeze_support()
	crawl = Crawler()
	crawl.set_crawl()



# totals.append(crawl.years_critic_crawler())

# totals.append(crawl.critic_crawler())
# totals.append(crawl.overall_critic_crawler())
# totals.append(crawl.user_crawler())
# totals.append(crawl.overall_user_crawler())

# added_totals = reduce(add, totals)
# complete_avg = added_totals / len(totals)

# print complete_avg