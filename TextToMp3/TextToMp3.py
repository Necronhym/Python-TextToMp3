from gtts import gTTS
from tkinter import filedialog
from tkinter import *
lan = 'en'
path = filedialog.askopenfilenames()[0]
f = open(path);
text = f.read();
f.close();
obj = gTTS(text=text, lang=lan, slow=False)
inp2=path[path.rfind('/')+1:path.rfind('.')]
obj.save(inp2 + ".mp3")
