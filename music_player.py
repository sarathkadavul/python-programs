import pygame
import glob
def quittt():
	a = raw_input("type 1.quit \n2.pause\n3.resume\n4.select")
        if(a=="quit"):
		print("bye bye")
                pygame.quit()
	elif(a=="pause"):
		print("paused ")
		selectsong.channel.pause()
		quittt()
        elif(a=="resume"):
		print("resumed")
		selectsong.channel.unpause()
		quittt()
	elif(a=="select"):
		selectsong()
	else:
                quittt()
def selectsong():
	a = glob.glob("*.flac")
	b = glob.glob("*.mp3")
	for k in b:
		a.append(k)
	j =1
	for i in a:
		print(j,i)
		j = j+1
	ch = int(raw_input("enter the song number>>"))
	song = pygame.mixer.Sound(a[ch-1])
	if(pygame.mixer.get_busy()):
		pygame.mixer.stop()
	selectsong.channel = song.play()
	print("playing song",a[ch-1])
	quittt()
pygame.init()
track = selectsong()
#song = pygame.mixer.Sound(track)
#channel = song.play()
#quittt()
