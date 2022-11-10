# Pomodoro Tracker Application Features:
# -> Counting Pomodoro Iterations
# -> Break times
# -> Start 
# -> Pause
# -> Continue
# -> Restart

# GUI Dependencies
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
		global numPomodoros
		global breakDelay
		currentTime = format_time(seconds)
		print(seconds)
		if(seconds==0 and breakDelay<3):
			numPomodoros+=1
			breakDelay+=1
			print('No. Pomodoros:',numPomodoros,', ', breakDelay)
			start_countDown()
		elif(breakDelay==4):
			print('Dalay Moderfoca')
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
		pauseButton = pomodoroWindow.nametowidget('pause')
		pauseButton['state'] = 'normal'
		counting_down()

	def restart():
		pomodoroWindow.destroy()
		main()

	def stop_screen():
		global stoppedTime
		global pause 
		pause = True
		startButton = pomodoroWindow.nametowidget('start')
		startButton['state']='disable'
		tk.Button(pomodoroWindow, 
			name='continue', 
			text='Continue', 
			#command=continue_counting, 
			width=8, font=('Helvetica',14), 
			border = 0, 
			bg = greenColor
		).place(x=260,y=140)
		pauseButton = pomodoroWindow.nametowidget('pause')
		pauseButton['text']='Stop'
		tk.Button(pomodoroWindow, 
			name='restart', 
			text='Restart', 
			#command=restart, 
			width=8, 
			font=('Helvetica',14), 
			border = 0, 
			bg = greenColor
		).place(x=150,y=140)



	global numPomodoros
	global breakDelay
	pomodoroTime = 25
	numPomodoros = 0
	breakTime = 5
	breakDelay = 0

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
		command=stop_screen, 
		width=8, 
		font=('Helvetica',14), 
		border = 0, 
		bg = greenColor
	).place(x=260,y=140)
	pauseButton = pomodoroWindow.nametowidget('pause')
	pauseButton['state'] = 'disabled'
	# Always show the window above all
	pomodoroWindow.attributes('-topmost',True)
	pomodoroWindow.mainloop()
if __name__=='__main__':
	main()