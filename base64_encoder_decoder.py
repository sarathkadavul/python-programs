import base64

def main():
	data = raw_input("\n enter your string\n")
	choice = int(raw_input("\nenter your choice \n1.encode\n2.decode\n"))
	if(choice == 1):
		print (base64.encodestring(data))
	elif(choice == 2):
		print (base64.decodestring(data))
	else:
		print ("invalid choice")

if __name__ == '__main__':
	main()
