import RPi.GPIO as GPIO
import MFRC522
import signal
import time

import tkinter as tk
from tkinter import font
import requests
 
continue_reading = True
 
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
 
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
 
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
 
# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")
 
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
 
        # Print UID
        print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+','+str(uid[4]))  
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
       
        # var uid
        var3 = [193,95,26,49,181]
        var1 = [177,124,98,16,191]
        var2 = [136,4,48,127,195]
        
        #coba
        if uid == var1:
            print("kartu 1")
            
            root = tk.Tk()
            label = tk.Label(root, text="berhasil", font=('Likhan',25), bg='green')
            label.pack()
            root.mainloop()
            

        elif uid == var2:
            print("kartu 2")
        elif uid == var3:
            print("kartu 3")
        else:
            print("kartu salah")
