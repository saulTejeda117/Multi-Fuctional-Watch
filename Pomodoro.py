# Pomodoro Tracker Application

import tkinter as tk

# Clock Dependencies
from datetime import datetime, timedelta

def main():
	# Widgets colors
	blackColor = '#000000'
	greenColor = '#43C42A'

	pomodoroWindow = tk.Tk()
	pomodoroWindow.title('Pomodoro Tracker')
	pomodoroWindow.configure(width=500,height=200, bg=blackColor)
	pomodoroWindow.resizable(False, False)

	# Set window screen position using screenwidth
	screen_width = pomodoroWindow.winfo_screenwidth()
	screen_width = screen_width-500
	pomodoroWindow.geometry("500x200+"+str(screen_width)+"+0")

	# Prettier format 00:00
	def format_time(seconds):
		hour = int(seconds / 60 / 60)
		seconds -= hour*60*60
		minutes = int(seconds/60)
		seconds -= minutes*60
		return f"{minutes:02d}:{seconds:02d}"

	def updating_time_units(seconds):
		currentTime = format_time(seconds)
		minuteSelector = pomodoroWindow.nametowidget('time')
		minuteSelector.configure(text=currentTime)

	def counting_down():
		global finishTime
		currentTime = datetime.now()
		totalTime = int((finishTime - currentTime).total_seconds())
		if(totalTime > 0):
			updating_time_units(totalTime)
			pomodoroWindow.after(500, counting_down)	
		else:
			updating_time_units(0)
	
	def start_countDown():
		global finishTime
		# Add 25 minutes to the current time
		nonTime = datetime.now()
		# Convertion of int to a time format
		minutesAdded = timedelta(minutes=pomodoroTime) 
		currentSeconds = (datetime.now() - nonTime + minutesAdded).total_seconds()
		currentTime = format_time(int(currentSeconds))

		finishTime = (datetime.now() + minutesAdded)
		print('Start Count Down')
		counting_down()

	
	pomodoroTime = 25
	breakTime = 5
	breakDelay = 4
	

	# Timer Window Elements
	tk.Label(pomodoroWindow, 
		name = 'time', 
		text='25:00', 
		fg=greenColor, 
		font=('Helvetica',80), 
		bg=blackColor
	).place(x=120,y=10)
	tk.Button(pomodoroWindow, 
		name='start', 
		text='Start', 
		command=lambda:start_countDown(), 
		width=8, font=('Helvetica',14), 
		border = 0, 
		bg = greenColor
	).place(x=150,y=140)
	tk.Button(pomodoroWindow, 
		name='pause', 
		text='Pause', 
		# command=stop_screen, 
		width=8, 
		font=('Helvetica',14), 
		border = 0, 
		bg = greenColor
	).place(x=260,y=140)
	# Always show the window above all
	pomodoroWindow.attributes('-topmost',True)
	pomodoroWindow.mainloop()
if __name__=='__main__':
	main()