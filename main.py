import speech_recognition as sr
import keyboard
import pygame
import os


scripts = {
    "консоль": "console\\main.py",
}


def run(command: list):
    command = " ".join(command)
    os.system(f"start {command}")


def capital(s):
    t = s.split('. ')
    for i in range(1, len(t)):
        t[i] = t[i][0].upper() + t[i][1:]
    return '. '.join(t)


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alert.mp3")
    pygame.mixer.music.play()


def write():
    print("WriteFunc")
    play_sound()
    keyboard.write(capital(record_voice(timeout=3).replace(" точка", ".").replace(" запятая", ",").capitalize()),
                   delay=0.005)


def test():
    print("TestFunc")


def record_voice(timeout=1, debug=False):
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        play_sound()
        if not debug:
            return r.recognize_google(r.listen(source, timeout=timeout), show_all=True,
                                      language="ru-RU")["alternative"][0]["transcript"].lower()
        else:
            print(r.recognize_google(r.listen(source), show_all=True,
                                     language="ru-RU")["alternative"][0]["transcript"].lower())


commands = {
    "тест": test,
    "напиши": write,
    "запусти": run,
}


def start():
    try:
        com = record_voice()
        for k, v in commands.items():
            if k == com.split()[0]:
                if len(com.split()) == 1:
                    v()
                else:
                    com = com.split()
                    com.pop(0)
                    v(com)
    except:
        print("Произошла ошибка в функции start")


keyboard.add_hotkey("Ctrl + Alt", start)
keyboard.add_hotkey("Ctrl + W", write)
keyboard.wait("Ctrl + q")

