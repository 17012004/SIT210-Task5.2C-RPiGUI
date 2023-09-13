from tkinter import *
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


def update_led_state():
    selected_led = led_var.get()
    leds = [5, 13, 26]

    for pin in leds:
        if pin == selected_led:
            GPIO.output(pin, GPIO.HIGH)  
        else:
            GPIO.output(pin, GPIO.LOW)   


win = Tk()
win.title("LED Control")
myFont = ('calibri', 26, 'bold')


led_var = IntVar()


led_radio_buttons = {}
led_radio_buttons[5] = Radiobutton(win, text="RED", font=myFont, height=2, width=8, variable=led_var, value=5, command=update_led_state)
led_radio_buttons[13] = Radiobutton(win, text="BLUE", font=myFont, height=2, width=8, variable=led_var, value=13, command=update_led_state)
led_radio_buttons[26] = Radiobutton(win, text="GREEN", font=myFont, height=2, width=8, variable=led_var, value=26, command=update_led_state)

led_var.set(None)

led_radio_buttons[5].grid(row=0, column=0)
led_radio_buttons[13].grid(row=0, column=1)
led_radio_buttons[26].grid(row=0, column=2)

win.mainloop()
