# Metacritic Crawl
##Summary
Crawl through metacritic's critic and user scores to find an average. 
##Purpose
I wanted to leverage Metacritic to analyze how we use ratings. It all started because some people think that average ratings tend more toward "7/10" rather than a true average "5/10". Using metacritic, I want to analyze this hypothsis. 
##Plan
- [x] intial kimono setup
- [x] grab all critic ratings from one movie
- [x] grab all user ratings from one movie
- [x] compute averages of above data sets
- [x] grab metacritic critic score of a large amount of movies
- [ ] grab individual movie scores from a large amount of movies
- [x] grab metacritic user scores of a large amount of movies
- [ ] grab individual critic scores from a large amount of movies
- [ ] **TODO** LIST:
	- [x] implement other ratings (games, etc.)
	- [ ] research other sources for ratings data
	- [ ] research tools to graphify current datasets
- [ ] write-up an analysis of the data

##History
- 11/3/2015: Inital Commit
- 11/4/2015: Switched from Kimono to BeautifulSoup and lxml
- 11/6/2015: Added Multithreading
- 1/16/2016: Added user scores 