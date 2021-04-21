# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:46:42 2020

@author: peter
"""

#To do: Use tkinter to make a morse code machine using mouse clicking

#Morse code translator
from pynput import keyboard
import time
import winsound

# times = ""

def callb1(key): #what to do on key-press
    return False #stop detecting more key-presses

def callb(key): #what to do on key-release
    return False #stop detecting more key-releases

def keyboard_morse():
    times = ""
    while True:
        t0_pause = time.time()
        with keyboard.Listener(on_press = callb1) as listener1: #setting code for listening key-press
            listener1.join()
            t1_pause_end = time.time()-t0_pause
            try:
                if times[-1] == ".":  #the pause timing is different after a dot vs dash
                    if t1_pause_end >= 0.190 and t1_pause_end <=0.500:
                        times += "/"
                    if t1_pause_end >= 0.501:
                        times += " "
                elif times[-1] == "-": #the pause timing is different after a dot vs dash
                    if t1_pause_end >= 0.225 and t1_pause_end <=0.500:
                        times += "/"
                    if t1_pause_end >= 0.501:
                        times += " "
            except IndexError:
                pass
        t0 = time.time() #reading time in sec
        with keyboard.Listener(on_release = callb) as listener: #setting code for listening key-release
            listener.join()
        t1 = time.time()-t0
        if t1 < 0.200:
            times += "."
        else:
            times += "-"
        if len(times) >= 11:
            print(times)
            return times  
    
def read_morse(keyboard_morse):
    result = []
    letter = ""
    for each in keyboard_morse:
        if each == "/" or each == " ":  #Used to be just "/", but added " ". Can probably do away with punctuation. Too time sensitive and finicky.
            result.append(letter)
            letter = ""
        else:
            letter += each
    result.append(letter)   #to catch the last letter that didn't end with a /
    return result

def alpha_morse(morse_letters):
    """
    morse_letters is a list of strings, each string will be a series of dots or dashes
    eg. ['...', '---', '...']    An output from read_morse function
    Returns
    -------
    A string. A word.

    """
    result = ""
    dict = {".-":"a",
            "-...":"b",
            "-.-.":"c",
            "-..":"d",
            ".":"e",
            "..-.":"f",
            "--.":"g",
            "....":"h",
            "..":"i",
            ".---":"j",
            "-.-":"k",
            ".-..":"l",
            "--":"m",
            "-.":"n",
            "---":"o",
            ".--.":"p",
            "--.-":"q",
            ".-.":"r",
            "...":"s",
            "-":"t",
            "..-":"u",
            "...-":"v",
            ".--":"w",
            "-..-":"x",
            "-.--":"y",
            "--..":"z",
            ".----":"1",
            "..---":"2",
            "...--":"3",
            "....-":"4",
            ".....":"5",
            "-....":"6",
            "--...":"7",
            "---..":"8",
            "----.":"9",
            "-----":"0",
            ".-.-.-":".",
            "--..--":",",
            "..--..":"?",
            ".----.":"'",
            "-.-.--":"!",
            "/":" "}    
    for each in morse_letters:
        try:
            result += dict[each]
        except KeyError:
            result += "[?]"
    print(result)
    return result

def morse(message):
    """
    Takes in a string
    Returns a string of Morse code signals
    """
    message = message.lower()
    dict = {"a":".-", 
            "b":"-...", 
            "c":"-.-.",
            "d":"-..",
            "e":".",
            "f":"..-.",
            "g":"--.",
            "h":"....",
            "i":"..",
            "j":".---",
            "k":"-.-",
            "l":".-..",
            "m":"--",
            "n":"-.",
            "o":"---",
            "p":".--.",
            "q":"--.-",
            "r":".-.",
            "s":"...",
            "t":"-",
            "u":"..-",
            "v":"...-",
            "w":".--",
            "x":"-..-",
            "y":"-.--",
            "z":"--..",
            "1":".----",
            "2":"..---",
            "3":"...--",
            "4":"....-",
            "5":".....",
            "6":"-....",
            "7":"--...",
            "8":"---..",
            "9":"----.",
            "0":"-----",
            ".":".-.-.-",
            ",":"--..--",
            "?":"..--..",
            "'":".----.",
            "!":"-.-.--",
            " ":"/"}
    result = ""
    for char in message:
        try:
            result += dict[char]
        except KeyError:
            result += ""
        result += " "
    print(result)
    result_message = ""
    for char in message:
        result_message += char
        try:
            length = len(dict[char])
        except KeyError:
            length = 0
        result_message += (" " * length)
    print(result_message)
    for char in result:
        if char == ".":
            winsound.Beep(800, 150)
        if char == "-":
            winsound.Beep(800, 450)
        if char == " ":
            time.sleep(0.5)
            
morse("sos")
a = keyboard_morse()
b = read_morse(a)
alpha_morse(b)