from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import threading
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from PIL import ImageTk, Image
import shutil
import os
import random
from win10toast import ToastNotifier


language = list(LANGUAGES.values())
def multi_speak():
    """
    creates a thread for speak1 function 
    """
    threading.Thread(target=speak1).start()

    
def Notify():
    lang = ""
    r_no = random.randint(1,97)
    if r_no < 26:
        lang = "Spanish"
    elif r_no < 72:
        lang = "French"
    else:
        lang = "German"
    noti = ToastNotifier()
    f = open("words.txt")
    words = f.readlines()
    f.close()
    noti.show_toast('Word of the Day',f"\tLanguage : {lang}\n{words[r_no]}",duration=10, icon_path="tranlator\\translator.ico", threaded = True)

def multi_listen():
    
    """
    creates a thread for speak1 function 
    """
    threading.Thread(target=listen).start()

def listen():
        """
        performs speech to text conversion
        """
        global content
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1)

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=1)
            lab1=Label(root,text="Say Something......",bg="#bbbbbb",fg="#433d3c",font=("monotype corsiva",25,'bold'))
            lab1.pack(pady=(70,20))
            audio = r.listen(source)
            lab2=Label(root,text="Time's up, Thanks !!",bg="#bbbbbb",fg="#433d3c",font=("monotype corsiva",25,'bold'))
            lab2.pack(pady=(5,5))
        try:
            text = r.recognize_google(audio,language='english')
            content = text+"\n"
            Input_text.insert(1.0,content)
            lab1.pack_forget()
            lab2.pack_forget()
        except:
            Label(root,text="Unable to understand, please repeat :",bg="#bbbbbb",fg="#433d3c",font=("monotype corsiva",25,'bold')).pack(pady=(5,5))
            listen()

def speak1():
    """
    perforn speech to text
    """
    # text = Output_text.get(1.0,END)
    # engine = pyttsx3.init() 
    # engine.say(text, "bn") 
    # engine.runAndWait()
    text = Output_text.get(1.0,END) 
    ['af', 'sq', 'am', 'ar', 'hy' , 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro' , 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz','vi','cy','xh','yi','yo','zu']
    dest=dest_lang.get()
    index=0
    for i in language:
        if dest==i:
            break
        index=index+1
    tem= list(LANGUAGES.keys())[index]
    g = gTTS(text,lang=tem)
    g.save("translated.mp3")
    playsound("translated.mp3")


    # say method on the engine that passing input text to be spoken 
    
  
    # run and wait method, it processes the voice commands.  


    
root = Tk()
root.title("Translator")   
root.geometry("1600x900")
root.iconbitmap("tranlator\\translator.ico")
root.resizable(False,False)
bg=ImageTk.PhotoImage(Image.open("tranlator\\background2.png"))
mic=ImageTk.PhotoImage(Image.open("tranlator\\micicon.png"))
translate=ImageTk.PhotoImage(Image.open("tranlator\\translate.png"))
speak_img= ImageTk.PhotoImage(Image.open("tranlator\\speak.png"))

    


    # src_lang = ttk.Combobox(root, values= language, width =22)
    # src_lang.place(x=20,y=60)
    # src_lang.set('choose input language')

    # dest_lang = ttk.Combobox(root, values= language, width =22)
    # dest_lang.place(x=890,y=60)
    # dest_lang.set('choose output language')

background=Label(root, image=bg, bd=0).place(x=0,y=0)
Word_List=Button(root,text="Word List",font=("Century Gothic",18),bd=0,width=14, fg="white", bg="black", command=Notify).place(x=418,y=0)
       
Output_text = Text(root,font = ('Century Gothic',9),bg= "#242424", fg="white",height = 21, wrap = WORD, padx=5, pady= 5, width =100)
Output_text.place(x = 857 , y = 209)
    
Input_text = Text(root,font = ('Century Gothic',9),bg= "#242424", fg="white",height = 21, wrap = WORD, padx=5, pady= 5, width =100)
Input_text.place(x = 31 , y = 209)
src_lang=ttk.Combobox(root, font=("Century Gothic",12),width=26,values = language)
src_lang.place(x=36,y=70)
src_lang.set('choose input language')
    
dest_lang=ttk.Combobox(root, font=("Century Gothic",12),width=26,values = language)
dest_lang.place(x=354,y=70)
dest_lang.set('choose output language')
    

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0,END) , src = src_lang.get(), dest = dest_lang.get())
   
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
    s=translated.text
    print(s)
    f=open("temp.txt",'a')
    f.write("Entered text in : "+src_lang.get() + "\n" +"Text entered : "+Input_text.get(1.0,END)+"Translated to Language: "+dest_lang.get()+"\n")
    f.close()
    
mic_button=Button(root, bd=0,bg= "#242424",image=mic, activebackground="#374045", activeforeground="#242424",command=multi_listen).place(x=1365,y=45)
translate_button=Button(root, bd=0,bg= "#242424",image=translate, activebackground="#242424", activeforeground="#242424", command= Translate).place(x=760,y=347)
speak_button=Button(root, bd=0,bg= "#bfbfbf",image=speak_img, activebackground="#bfbfbf", activeforeground="#bfbfbf", command= multi_speak) .place(x=1410,y=705)
root.mainloop()