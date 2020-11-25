import time
from selenium import webdriver
 


# Using readlines() read each link
file1 = open('paint.txt', 'r') 
Lines = file1.readlines() 


# download each file. file stored in download folder of chrome or firefox as the case may be
for line in Lines:
	driver = webdriver.Chrome('c:/windows/chromedriver.exe')  # Optional argument, if not specified will search path.
	#uncomment below and comment above line if you are using Firefox browser
	#driver = webdriver.Firefox()
	try:
		driver.get(line)
		driver.find_element_by_xpath("//button[@aria-label='Download image']").click();
		# wait for 10 seconds to download
		time.sleep(10)
		driver.quit()
	except:
		driver.quit()
		pass
		