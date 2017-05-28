import urllib
import pyperclip as pc

def main():
	flag = True
	while(flag):
		raw_input("copy the url and press any key after copying==>")
		url = pc.paste()
		print (url)
		choice = raw_input("is this the correct url? [y/n]==>")
		if(choice == 'y'):
			flag = False
		elif(choice == 'n'):
			flag = True
	name = raw_input("Enter the filename ==>")
	urllib.urlretrieve(url,name)

if __name__ == '__main__':
	main()