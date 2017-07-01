from bs4 import BeautifulSoup
import urllib2
import sys

url = raw_input("Enter the url")

content = urllib2.urlopen(url).read() #content holds the source code of the given url

soup = BeautifulSoup(content,"html.parser") #we use html parser here others like lxml,etc can also be used

while(1):

	print "Enter your choice"

	choice = int(raw_input("\n1.title\n2.links\n3.exit\n"))

	if(choice == 1):
		print soup.title.string # prints only the string between the title tag
	elif(choice == 2):
		for links in soup.find_all('a'): #finds all occurances of anchor tag
			print links.get('href') # from the occurances of anchor tag get the value of href
	elif(choice == 3):
		print "good Bye"
		sys.exit() #kills the process