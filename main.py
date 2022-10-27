# Multifunctional Clock Features:
# -> Stopwatch
# -> Timer
# -> Pomodoro
# -> Alarm Clock

from Stopwatch import main as stopwath
from Timer import main as timer

# GUI Dependencies
import tkinter as tk
# Clock Dependencies
import time

def main():
	# MainWindow widgets
	mainWindow = tk.Tk()
	mainWindow.title('Multi-Functional Watch')
	mainWindow.configure(width=500,height=200, bg='#000000')
	mainWindow.resizable(False, False)
	def call_stopwatch():
		mainWindow.destroy()
		stopwath()
	def call_timer():
		mainWindow.destroy()
		timer()
	def call_alarmClock():
		print('call_alarmClock')
	def call_pomodoro():
		print('call_pomodoro')

	# Stopwatch/Timer/Pomodoro/AlarmClock Buttons 
	tk.Button(mainWindow, 
		text='Stopwatch',
		fg='#43C42A', 
		bg='#000000', 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground='#43C42A',
		command = call_stopwatch
	).place(x=40,y=150)
	tk.Button(mainWindow, 
		text='Timer',
		fg='#43C42A', 
		bg='#000000', 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground='#43C42A',
		command = call_timer
	).place(x=150,y=150)
	tk.Button(mainWindow, 
		text='Alarm Clock',
		fg='#43C42A', 
		bg='#000000', 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground='#43C42A',
		command = call_alarmClock
	).place(x=260,y=150)
	tk.Button(mainWindow, 
		text='Pomodoro',
		fg='#43C42A',
		bg='#000000', 
		font=('Helvetica', 12), 
		width=10,
		border=1,
		activebackground='#43C42A',
		command = call_pomodoro
	).place(x=370,y=150)

	# Get/Print Current Time
	def show_currentTime():
		today = time.ctime()
		today = today.split()
		# Clock Label
		tk.Label(mainWindow, 
			text=today[3], 
			fg='#43C42A', 
			bg='#000000', 
			font=('Helvetica', 80)
		).place(x=35,y=10)
		mainWindow.after(500, show_currentTime)
	show_currentTime()
	mainWindow.mainloop()

if __name__ == '__main__':
    main()
