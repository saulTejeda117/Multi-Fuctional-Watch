# Multifunctional Clock Features:
# -> Stopwatch
# -> Timer
# -> Pomodoro
# -> Alarm Clock

from Stopwatch import main as stopwath
from Timer import main as timer
from AlarmClock import main as alarmClock

# GUI Dependencies
import tkinter as tk

# Clock Dependencies
import time

def main():
	# Widgets colors
	blackColor = '#000000'
	greenColor = '#43C42A'

	mainWindow = tk.Tk()
	mainWindow.title('Multi-Functional Watch')
	mainWindow.configure(width=500,height=200, bg=blackColor)
	mainWindow.resizable(False, False)

	def call_stopwatch():
		mainWindow.destroy()
		stopwath()
	def call_timer():
		mainWindow.destroy()
		timer()
	def call_alarmClock():
		mainWindow.destroy()
		alarmClock()
	def call_pomodoro():
		print('call_pomodoro')

	# Stopwatch/Timer/Pomodoro/AlarmClock Buttons 
	tk.Button(mainWindow, 
		text='Stopwatch',
		fg=greenColor, 
		bg=blackColor, 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground=greenColor,
		command = call_stopwatch
	).place(x=40,y=150)
	tk.Button(mainWindow, 
		text='Timer',
		fg=greenColor, 
		bg=blackColor, 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground=greenColor,
		command = call_timer
	).place(x=150,y=150)
	tk.Button(mainWindow, 
		text='Alarm Clock',
		fg=greenColor, 
		bg=blackColor, 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground=greenColor,
		command = call_alarmClock
	).place(x=260,y=150)
	tk.Button(mainWindow, 
		text='Pomodoro',
		fg=greenColor,
		bg=blackColor, 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground=greenColor,
		command = call_pomodoro
	).place(x=370,y=150)

	# Bucle function to update clock
	def show_currentTime():
		# Get current Date/Time/Year
		today = time.ctime()
		today = today.split()
		# Show only the current time
		tk.Label(mainWindow, 
			text=today[3], 
			fg=greenColor, 
			bg=blackColor, 
			font=('Helvetica', 80)
		).place(x=35,y=10)
		# Iteration of the function
		mainWindow.after(500, show_currentTime)
	show_currentTime()
	mainWindow.mainloop()

if __name__ == '__main__':
    main()
