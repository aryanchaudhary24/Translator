import random
from win10toast import ToastNotifier

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
    noti.show_toast('Word of the Day',f"\tLanguage : {lang}\n{words[r_no]}",duration=10, icon_path="translator.ico", threaded = True)

Notify()