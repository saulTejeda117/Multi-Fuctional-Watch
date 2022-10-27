# Stopwatch Function

# GUI Dependencies
import tkinter as tk
# Clock Dependencies
from datetime import datetime, timedelta

def main():
	stopwatchWindow = tk.Tk()
	stopwatchWindow.title('Stop Watch')
	stopwatchWindow.configure(width=500,height=200, bg='#000000')
	stopwatchWindow.resizable(False, False)
	# Prettier format 00:00:00
	def format_time(seconds):
		hour = int(seconds / 60 / 60)
		seconds -= hour*60*60
		minutes = int(seconds/60)
		seconds -= minutes*60
		return f"{hour:02d}:{minutes:02d}:{seconds:02d}"
	# Iterative fuction update time in screen
	def resh_time():
		global beginTime
		global stoppedTime
		global pause 
		global currentSeconds
		currentSeconds = (datetime.now() - beginTime).total_seconds()
		stoppedTime = datetime.now() 
		currentTime = format_time(int(currentSeconds))
		tk.Label(stopwatchWindow, 
			name = 'time', 
			text=currentTime, 
			fg='#43C42A', 
			font=('Helvetica',80), 
			bg='#000000'
		).place(x=35,y=10)
		# Iterates just if its not paused
		if(pause==False):
			stopwatchWindow.after(500,resh_time)
	def continue_counting():
		global stoppedTime
		global currentSeconds
		global beginTime
		global pause
		# Convert the elapsed time into a seconds format to get
		# a new begin time when the program is paused and then 
		# make the current time operation
		currentSeconds = timedelta(seconds=currentSeconds)
		beginTime = (datetime.now() - currentSeconds)
		currentTime = (datetime.now() - beginTime).total_seconds()
		currentTime = format_time(int(currentTime))
		# Widgets Restart/Continue Elimination
		continueButton = stopwatchWindow.nametowidget('continue')
		continueButton.destroy()
		pauseRestart= stopwatchWindow.nametowidget('restart')
		pauseRestart.destroy()
		startButton = stopwatchWindow.nametowidget('start')
		startButton['state']='normal'
		pauseButton = stopwatchWindow.nametowidget('pause')
		pauseButton['text']='Pause'
		# Change the programs state to continue
		pause = False
		resh_time()
	def start_counting():
		global beginTime
		global pause
		pause = False
		beginTime = datetime.now()
		pauseButton = stopwatchWindow.nametowidget('pause')
		pauseButton['state']='normal'
		pauseButton = stopwatchWindow.nametowidget('start')
		pauseButton['text']='Restart'
		resh_time()
	def restart():
		stopwatchWindow.destroy()
		main()
	# The program shows this when "pause" was clicked
	def stop_screen():
		global stoppedTime
		global pause 
		pause = True
		startButton = stopwatchWindow.nametowidget('start')
		startButton['state']='disable'
		tk.Button(stopwatchWindow, 
			name='continue', 
			text='Continue', 
			command=continue_counting, 
			width=8, font=('Helvetica',14), 
			border = 0, 
			bg = '#43C42A'
		).place(x=150,y=140)
		pauseButton = stopwatchWindow.nametowidget('pause')
		pauseButton['text']='Stop'
		tk.Button(stopwatchWindow, 
			name='restart', 
			text='Restart', 
			command=lambda:restart(), 
			width=8, 
			font=('Helvetica',14), 
			border = 0, 
			bg = '#43C42A'
		).place(x=260,y=140)
	# Get the actual time 
	nonTime = datetime.now()
	currentSeconds = (datetime.now() - nonTime).total_seconds()
	currentTime = format_time(int(currentSeconds))
	# Show current time in screen
	tk.Label(stopwatchWindow, 
		name = 'time', 
		text=currentTime, 
		fg='#43C42A', 
		font=('Helvetica',80), 
		bg='#000000'
	).place(x=35,y=10)
	# Start the counting
	tk.Button(stopwatchWindow, 
		name='start', 
		text='Start', 
		command=start_counting, 
		width=8, font=('Helvetica',14), 
		border = 0, 
		bg = '#43C42A'
	).place(x=150,y=140)
	tk.Button(stopwatchWindow, 
		name='pause', 
		text='Pause', 
		command=stop_screen, 
		width=8, 
		font=('Helvetica',14), 
		border = 0, 
		bg = '#43C42A'
	).place(x=260,y=140)
	# Use this to disable the pause button at the begining
	pauseButton = stopwatchWindow.nametowidget('pause')
	pauseButton['state']='disable'
	stopwatchWindow.mainloop()
if __name__ == '__main__':
    main()
