# used to make pronounce function using sapi voice
from win32com.client import Dispatch 

def pronounce(str):
    '''This function is used to make pronounce any string given to it'''
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    string=input("Enter the string you want to be pronounced\n")
    pronounce(string)   # Now with the help of this function your entered string will be pronounced
