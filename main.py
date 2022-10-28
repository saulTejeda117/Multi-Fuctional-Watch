# Multifunctional Clock Application Features:
# -> Clock
# 	-> Stopwatch
# 	-> Timer
# 	-> Pomodoro
# 	-> Alarm Clock

# Functions files import
from Stopwatch import main as stopwath
from Timer import main as timer
from AlarmClock import main as alarmClock
from Pomodoro import main as pomodoro

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
	
	# Set window screen position using screenwidth
	screen_width = mainWindow.winfo_screenwidth()
	screen_width = screen_width-500
	mainWindow.geometry("500x200+"+str(screen_width)+"+0")

	def call_stopwatch():
		mainWindow.destroy()
		stopwath()
		main()
	def call_timer():
		mainWindow.destroy()
		timer()
		main()
	def call_alarmClock():
		mainWindow.destroy()
		alarmClock()
		main()
	def call_pomodoro():
		mainWindow.destroy()
		pomodoro()
		main()

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
	# Always show the window above all
	mainWindow.attributes('-topmost',True)
	show_currentTime()
	mainWindow.mainloop()
if __name__ == '__main__':
    main()
