import speech_recognition
import pyttsx3
from datetime import date, datetime
from gtts import gTTS
import pyaudio
import playsound
import os
import datetime
import time
import wikipedia
import webbrowser

i = 0
while i < 5:
    laika_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("laika: Mời bạn nói: ")
        audio = laika_ear.listen(mic)
        print("laika:...")
        try:
            you = laika_ear.recognize_google(audio, language="vi-VI")
            print("You :", (you))
        except:
            i = i + 1
            print("laika: Xin lỗi! tôi không nhận được voice!")
            laika_brain = "Mình không nghe được bạn nói, bạn nói lại nhé"
            output = gTTS(laika_brain, lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            os.remove('output.mp3')
            continue
        if "chào" in you:
            laika_brain = "Tôi là laika, trợ lý ảo của bạn. Bạn cần giúp gì không"
            print("laika: ", laika_brain)
        elif "đẹp " in you:
            laika_brain = "Thầy Dã,đẹp trai,dạy giỏi nhất lớp"
            print("laika: ", laika_brain)
        elif "ngày" in you:
            today = date.today()
            laika_brain = today.strftime("Hôm nay là ngày: %d tháng %m năm %Y")
            print("laika: ", laika_brain)
        elif "Facebook" in you:
            webbrowser.open('https://www.facebook.com/', new=1)
            laika_brain = "Ok!facebook đang được mở"
            print('you:', you)
            print('laika:', laika_brain)
            output = gTTS(laika_brain, lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            break

        elif "Gmail" in you:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox', new=1)
            laika_brain = "Ok!Gmail đang được mở"
            print('you:', you)
            print('laika:', laika_brain)
            output = gTTS(laika_brain, lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            break
        elif "YouTube" in you:
            webbrowser.open('https://www.youtube.com/', new=1)
            laika_brain = "Ok!Youtbe đang được mở"
            print('you:', you)
            print('laika:', laika_brain)
            output = gTTS(laika_brain, lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            break

        elif "Chrome" in you:
            webbrowser.open('https://www.google.com.vn/', new=1)
            laika_brain = "Ok!Google đang được mở"
            print('you:', you)
            print('laika:', laika_brain)
            output = gTTS(laika_brain, lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            break
        elif "Wikipedia" in you:
            laika_ear = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                print("Wikipedia: ...")
                audio = laika_ear.listen(source, timeout=5, phrase_time_limit=5)
            try:
                wiki = laika_ear.recognize_google(audio, language="vi-VI")
            except:
                wiki = 'Sorry'
            wikipedia.set_lang("vi")
            wiki = wikipedia.summary(wiki)
            print(wiki)
            laika_brain = wiki
        elif "tạm biệt" in you:
            laika_brain = "Tạm biệt bạn, hẹn gặp lại"
            output = gTTS(laika_brain, lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3')
            break
        else:
            laika_brain = "Xin lỗi phần này tôi chưa được học"
        output = gTTS(laika_brain, lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')
        laika_speak = pyttsx3.init()
        laika_speak.say(laika_brain)
        laika_speak.runAndWait()