import speech_recognition as sr
import threading, time
import pyttsx3



r = sr.Recognizer()
engine = pyttsx3.init()
mic = sr.Microphone(device_index=0)
global audiolist
global textlist
textlist = []
audiolist = []
global word
global tts
tts = True
word = ''
def microphone_record():
        try:
            with mic as source:
                audio = r.record(source, duration=2)
                #print("Audio recorded")
                audiolist.append(audio)

        except UnknownValueError() as uve:
            print("UVE detected")

def recog(audiolist):
    try:
        q = (r.recognize_google(audiolist.pop(0)))
        textlist.append(q)
   
            sys.exit()


    except Exception as e:
        #print("Seems quiet")
        pass


def thread_mic():
    while(True):
        microphone_record()
        #   print(len(audiolist))


def thread_recog(audiolist):
    while(True):
        if(len(audiolist)>0):
            #print("Recog triggered")
            recog(audiolist)
            print(textlist)

def speaking(x):
        engine.say(x)
        engine.runAndWait()

def speakingthread(tts, word):
    while(True):
        if(tts==True):
            print("speaking thread triggered")
            speaking(word)
            tts = False
            print("speaking thread stabilized")

speaking("System initializing")
x = threading.Thread(target=thread_mic)
x.start()
speaking("Microphone thread online")
y =  threading.Thread(target=thread_recog, args=(audiolist,))
y.start()
speaking("Recognition thread online")
speaker = threading.Thread(target=speakingthread, args=(True,word))
speaker.start()
speaking("Dynamic speech thread online")
speaking("All systems online")
#time.sleep(1)
