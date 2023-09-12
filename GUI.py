from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, GPIO.LOW)

win = Tk()
win.title("LED Control")
myFont = ('calibri', 26, 'bold')

def LEDOn(pin):
    print(f"LED button {pin} pressed")
    if GPIO.input(pin):
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)
    update_button_text(pin)

def update_button_text(pin):
    if pin == 5:
        LedButton["RED"] = "LED ON" if GPIO.input(pin) else "LED OFF"
    elif pin == 13:
        LedButton["BLUE"] = "LED ON" if GPIO.input(pin) else "LED OFF"
    elif pin == 26:
        LedButton["GREEN"] = "LED ON" if GPIO.input(pin) else "LED OFF"

LedButton = {}
LedButton[5] = Button(win, text="RED", font=myFont, height=2, width=8, command=lambda: LEDOn(5))
LedButton[13] = Button(win, text="BLUE", font=myFont, height=2, width=8, command=lambda: LEDOn(13))
LedButton[26] = Button(win, text="GREEN", font=myFont, height=2, width=8, command=lambda: LEDOn(26))

LedButton[5].grid(row=0, column=0)
LedButton[13].grid(row=0, column=1)
LedButton[26].grid(row=0, column=2)

win.mainloop()
    



