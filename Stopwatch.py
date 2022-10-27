# Stopwatch 

# GUI Dependencies
import tkinter as tk
# Clock Dependencies
from datetime import datetime, timedelta

def main():
	# MainWindow widgets
	mainWindow = tk.Tk()
	mainWindow.title('Stop Watch')
	mainWindow.configure(width=500,height=200, bg='#000000')
	mainWindow.resizable(False, False)

	# Counting time 
	def format_time(seconds):
		hour = int(seconds / 60 / 60)
		seconds -= hour*60*60
		minutes = int(seconds/60)
		seconds -= minutes*60
		return f"{hour:02d}:{minutes:02d}:{seconds:02d}"
		
	def resh_time():
		global beginTime
		global stoppedTime
		global pause 
		global currentSeconds
		currentSeconds = (datetime.now() - beginTime).total_seconds()
		print('*',currentSeconds)
		stoppedTime = datetime.now() 
		currentTime = format_time(int(currentSeconds))
		tk.Label(mainWindow, name = 'time', text=currentTime, fg='#43C42A', font=('Helvetica',80), bg='#000000').place(x=35,y=10)
		if(pause==False):
			mainWindow.after(500,resh_time)

	def continue_counting():
		global stoppedTime
		global currentSeconds
		global beginTime
		global pause

		currentSeconds = timedelta(seconds=currentSeconds)
		beginTime = (datetime.now() - currentSeconds)
		currentTime = (datetime.now() - beginTime).total_seconds()
		currentTime = format_time(int(currentTime))

		continueButton = mainWindow.nametowidget('continue')
		continueButton.destroy()
		startButton = mainWindow.nametowidget('start')
		startButton['state']='normal'
		pause = False
		startButton = mainWindow.nametowidget('pause')
		startButton['text']='Pause'
		resh_time()

	def start_counting():
		global beginTime
		global pause
		pause = False
		beginTime = datetime.now()
		pauseButton = mainWindow.nametowidget('pause')
		pauseButton['state']='normal'
		pauseButton = mainWindow.nametowidget('start')
		pauseButton['text']='Restart'

		resh_time()

	def show_something():
		print('Cosa')
	def restart():
		mainWindow.destroy()
		main()
	def stop_screen():
		global stoppedTime
		global pause 
		pause = True
		startButton = mainWindow.nametowidget('start')
		startButton['state']='disable'
		tk.Button(mainWindow, name='continue', text='Continue', command=lambda:continue_counting(), width=8, font=('Helvetica',14), border = 0, bg = '#43C42A').place(x=150,y=140)
		pauseButton = mainWindow.nametowidget('pause')
		pauseButton['text']='Stop'
		tk.Button(mainWindow, name='restart', text='Restart', command=restart(), width=8, font=('Helvetica',14), border = 0, bg = '#43C42A').place(x=260,y=140)
		

	# Get the actual time 
	nonTime = datetime.now()
	currentSeconds = (datetime.now() - nonTime).total_seconds()
	currentTime = format_time(int(currentSeconds))
	# # Show current time in screen
	tk.Label(mainWindow, name = 'time', text=currentTime, fg='#43C42A', font=('Helvetica',80), bg='#000000').place(x=35,y=10)

	# Start the counting
	tk.Button(mainWindow, name='start', text='Start', command=lambda:start_counting(), width=8, font=('Helvetica',14), border = 0, bg = '#43C42A').place(x=150,y=140)

	# Pause the counting
	tk.Button(mainWindow, name='pause', text='Pause', command=lambda:stop_screen(), width=8, font=('Helvetica',14), border = 0, bg = '#43C42A').place(x=260,y=140)
	pauseButton = mainWindow.nametowidget('pause')
	pauseButton['state']='disable'
	mainWindow.mainloop()
if __name__ == '__main__':
    main()
