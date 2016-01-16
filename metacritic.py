'''
@author: andrew baumann 
@purpose: crawl metacritic's scores, and assemble some data (avg, etc)
@contact: abaumann@columnit.com	
'''
import json
from multiprocessing import Process, freeze_support
from crawler import Crawler

def add(x,y): return x+y

if __name__ == '__main__':
	freeze_support()
	crawl = Crawler()
	crawl.set_crawl()
