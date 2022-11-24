# Stopwatch Appplication Features:
# -> Start 
# -> Pause
# -> Continue
# -> Restart


# Aspectos a mejorar:
# -> Cambiar el botón de Restart de posición 
# -> Eliminar widgets repetidos
# 	* Hacer Update a elementos ya existentes
# -> Eliminar variables globales
# -> Crear Constantes para widgets que se utilizan varias veces
#
# -> Añadir milesimas de segundo sin que el programa explote (Good Luck!)


# GUI Dependencies
import tkinter as tk

# Clock Dependencies
from datetime import datetime, timedelta

def main():
	# Widgets colors
	blackColor = '#000001'
	greenColor = '#43C42A'



	stopwatchWindow = tk.Tk()
	stopwatchWindow.title('Stop Watch')
	stopwatchWindow.configure(width=500,height=200, bg='#000000')
	stopwatchWindow.resizable(False, False)
	# Set window screen position using screenwidth
	screen_width = stopwatchWindow.winfo_screenwidth()
	screen_width = screen_width-500
	stopwatchWindow.geometry("500x200+"+str(screen_width)+"+0")

	tk.Text(stopwatchWindow, bg=blackColor, bd=0, height=4.5, width=53).place(x=35,y=100)
	
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
		timeLabel = stopwatchWindow.nametowidget('time')
		timeLabel['text']=currentTime
		# Iterates just if its not paused
		if(pause==False):
			stopwatchWindow.after(500,resh_time)
	def continue_counting():
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
			bg = greenColor
		).place(x=150,y=135)
		pauseButton = stopwatchWindow.nametowidget('pause')
		pauseButton['text']='Stop'

		tk.Button(stopwatchWindow, 
			name='restart', 
			text='Restart', 
			command=lambda:restart(), 
			width=8, 
			font=('Helvetica',14), 
			border = 0, 
			bg = greenColor
		).place(x=260,y=135)
	# Get the actual time 
	nonTime = datetime.now()
	currentSeconds = (datetime.now() - nonTime).total_seconds()
	currentTime = format_time(int(currentSeconds))
	# Show current time in screen
	#⏱
	tk.Button(stopwatchWindow, 
		name='return', 
		text='⏎', 
		command=stopwatchWindow.destroy, 
		width=0, 
		font=('arial',24), 
		border = 0, 
		height=-15,
		fg = greenColor,
		bg=blackColor
	).place(x=50,y=122)
	tk.Label(stopwatchWindow, 
		name = 'time', 
		text=currentTime, 
		fg=greenColor, 
		font=('Helvetica',80), 
		bg='#000001'
	).place(x=35,y=10)
	# Start the counting
	tk.Button(stopwatchWindow, 
		name='start', 
		text='Start', 
		command=start_counting, 
		width=8, font=('Helvetica',14), 
		border = 0, 
		bg = greenColor,
		fg='#000001'
	).place(x=150,y=135)
	tk.Button(stopwatchWindow, 
		name='pause', 
		text='Pause', 
		command=stop_screen, 
		width=8, 
		font=('Helvetica',14), 
		border = 0, 
		bg = greenColor
	).place(x=260,y=135)

	



	# Use this to disable the pause button at the begining
	pauseButton = stopwatchWindow.nametowidget('pause')
	pauseButton['state']='disable'
	# Always show the window above all
	stopwatchWindow.attributes('-topmost',True)
	# Make every element with this color transparent
	stopwatchWindow.attributes('-transparentcolor','black')
	# Set opacity window at 80%
	stopwatchWindow.attributes('-alpha',0.8)
	# Hide title bar of the window
	stopwatchWindow.overrideredirect(1)








	stopwatchWindow.mainloop()






if __name__ == '__main__':
    main()
