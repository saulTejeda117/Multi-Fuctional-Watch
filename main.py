# Multifunctional Clock Application Features:
# -> Clock
# 	-> Stopwatch
# 	-> Timer
# 	-> Alarm Clock
# 	-> Pomodoro Tracker

# New Features:
# -> Add a fucntion that changes the interface theme color
# it would be contained in window's menu bar.


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
	blackColor = '#000001'
	greenColor = '#43C42A'

	mainWindow = tk.Tk()
	mainWindow.title('Multi-Functional Watch')
	mainWindow.configure(width=500,height=200, bg='#000000')
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
	tk.Text(mainWindow, bg=blackColor, bd=0, height=4.5, width=53).place(x=35,y=100)
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
	).place(x=40,y=135)
	tk.Button(mainWindow, 
		text='Timer',
		fg=greenColor, 
		bg=blackColor, 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground=greenColor,
		command = call_timer
	).place(x=145,y=135)
	tk.Button(mainWindow, 
		text='Alarm Clock',
		fg=greenColor, 
		bg=blackColor, 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground=greenColor,
		command = call_alarmClock
	).place(x=250,y=135)
	tk.Button(mainWindow, 
		name='pomodoro',
		text='Pomodoro',
		fg=greenColor,
		bg=blackColor, 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground=greenColor,
		command = call_pomodoro
	).place(x=355,y=135)
	# Bucle function to update clock
	def show_currentTime():
		# Get current Date/Time/Year
		today = time.ctime()
		today = today.split()
		# Show only the current time
		tk.Label(mainWindow, 
			text=today[3], 
			fg=greenColor, 
			bg='#000001', 
			font=('Helvetica', 80)
		).place(x=35,y=10)
		# Iteration of the function
		mainWindow.after(500, show_currentTime)
	# Always show the window above all
	mainWindow.attributes('-topmost',True)

	# Make every element with this color transparent
	mainWindow.attributes('-transparentcolor','black')
	# Set opacity window at 80%
	mainWindow.attributes('-alpha',0.8)
	# Hide title bar of the window
	mainWindow.overrideredirect(1)
	show_currentTime()
	
	mainWindow.mainloop()

if __name__ == '__main__':
    main()
