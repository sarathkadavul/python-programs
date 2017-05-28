import zipfile

def main():
	name = raw_input("Enter the file name")
	zi = zipfile.ZipFile(name)
	zi.extractall('extracted')

if __name__ == '__main__':
	main()