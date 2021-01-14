#pip install gTTS
from gtts import gTTS

in_text = input("Enter text ")
audio=gTTS(text=in_text,lang='en',slow=False)
audio.save("audio.mp3")

#one liner: gTTS(text=input("Enter text "),lang='en',slow=False).save("audio.mp3")
