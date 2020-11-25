import requests
from bs4 import BeautifulSoup
 

 
 
links_to= 'https://www.artic.edu/collection?is_public_domain=1&classification_ids=prints%20and%20drawing&material_ids=watercolor&page='
 
reqs = requests.get(links_to)
soup = BeautifulSoup(reqs.text, 'lxml')

 


#initialise a empty list to store the  list of pages
pages=[] 

# find the number of  pages to scrape  and store them in list(pages)
for ul_list in soup.find_all('ul',{'class':'m-paginator__pages'}):
	for litag in ul_list.find_all('li'):
		try:
			page_links=litag.find("a") 
			pages.append(page_links.text)
		except:
			continue	

# get the last page number
last_page=(pages[-1])		

# initilaise the list to store the links of the paginated-page 
final_link=[]

# read Dijkstra to understand +1
for i in range(int(last_page)+1):
	# make a list of links of pages to visit
	link_ =links_to+str(i)
	final_link.append(link_)


# now you have the links of the pages to visit
# start the links visit excluding 1st item from the list beacuse it is duplicate
# do not know why it occurs
# stoe the links in paint.txt
for urls in final_link[1:]:
	reqs = requests.get(urls)
	soup = BeautifulSoup(reqs.text, 'lxml')
	# get first page elements
	for ultag in soup.find_all('ul', {'id': 'artworksList'}):
		for litag in ultag.find_all('li'):
			paint_links=litag.find("a").get('href')
			with open('paint.txt','a') as fd:
				fd.write(paint_links+'\n')

 
