#pip install gTTS
from gtts import gTTS

in_text = input("Enter text ")
audio=gTTS(text=in_text,lang='en',slow=False)
audio.save("audio.mp3")
