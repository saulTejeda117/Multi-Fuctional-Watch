# Timer Application Features:
# -> Time Selector
# -> Start 
# -> Play an alarm sound

# <------UNCOMMENT ALL 'MIXER' OCCURRENCES TO PLAY ALARM SOUND!!!!!------->

# GUI Dependencies
import tkinter as tk
from tkinter import messagebox

# Play Sound Dependencies
#from pygame import mixer

# Clock Dependencies
from datetime import datetime, timedelta


# Aspectos a mejorar:
# -> Añadir Bucles para acortar la declaración de elementos repetidos
# -> Eliminar variables globales
# -> Crear Constantes para widgets que se utilizan varias veces
#
# -> Añadir Funciones de Pausa, Reinicio y Continuar



def main():
	# Widgets colors
	blackColor = '#000000'
	greenColor = '#43C42A'
	
	#mixer.init()
	timerWindow = tk.Tk()
	# timerWindow features
	timerWindow.title('Timer')
	timerWindow.configure(width=500, height=200, bg='#000000')
	timerWindow.resizable(False, False)

	# Set window screen position using screenwidth
	screen_width = timerWindow.winfo_screenwidth()
	screen_width = screen_width-500
	timerWindow.geometry("500x200+"+str(screen_width)+"+0")

	hours = []
	minutes = []
	seconds = []
	i=0
	while (i<60):
		if(i<24):
			hours.append(f"{i:02d}")
		minutes.append(f"{i:02d}")
		seconds.append(f"{i:02d}")
		i+=1
	global h
	global m
	global s
	def updating_time_units(seconds):
		hour = int(seconds / 60 / 60)
		seconds -= hour*60*60
		minutes = int(seconds/60)
		seconds -= minutes*60

		hourSelector = timerWindow.nametowidget('hourSelector')
		hourSelector.configure(text=f"{hour:02d}")

		minuteSelector = timerWindow.nametowidget('minuteSelector')
		minuteSelector.configure(text=f"{minutes:02d}")

		secondsSelector = timerWindow.nametowidget('secondsSelector')
		secondsSelector.configure(text=f"{seconds:02d}")
	def restart_timer():
		# Time variables
		restart = False
		while(restart != True):
			# playsound('beep.mp3', False)
			# mixer.music.load("beep_OyPVftio.mp3")
			# mixer.music.play(-1)
			restart = messagebox.askokcancel(message="¿Desea continuar?", title="Reinicio")
			if(restart == True):
				# mixer.music.stop()
				restart = True
				timerWindow.destroy()
				main()
			else:
				# mixer.music.stop()
				restart = True
				timerWindow.destroy()
	def counting_down():
		global finishTime
		currentTime = datetime.now()
		totalTime = int((finishTime - currentTime).total_seconds())
		if(totalTime > 0):
			updating_time_units(totalTime)
			timerWindow.after(500, counting_down)	
		else:
			updating_time_units(0)
			restart_timer()
			
	def start_count_down():
		# Time variables
		global h
		global m
		global s
		# End Time
		global finishTime
		# print(h,':',m,':',s)
		hoursAdded = timedelta(hours=h,minutes=m,seconds=s) 
		# print(hoursAdded)
		finishTime = (datetime.now() + hoursAdded)
		# print(datetime.now(),'*****',finishTime)
		counting_down()
		
	# This function get 1/-1 and the time unit to configure with this parameter
	def change_time_unit(time, timeUnit):
		global h
		global m
		global s
		if(timeUnit == 0):
			hourSelector = timerWindow.nametowidget('hourSelector')
			if(h<0):
				h=23
				hourShown = hours[h]
			elif(h==23 and time==1):
				h = 0
				hourShown = hours[h]
			else:
				h = h + time
				hourShown = hours[h]
			hourSelector.configure(text=hourShown)
		elif(timeUnit == 1):
			minuteSelector = timerWindow.nametowidget('minuteSelector')
			if(m<0):
				m = 59
				mintesShown = minutes[m]
			if(m==59 and time==1):
				m = 0
				mintesShown = minutes[m]
			else:
				m = m + time
				mintesShown = minutes[m]
			minuteSelector.configure(text=mintesShown)
		else:
			secondsSelector = timerWindow.nametowidget('secondsSelector')
			if(s<0):
				s = 59
				secondsShown = seconds[s]
			if(s==59 and time==1):
				s = 0
				secondsShown = seconds[s]
			else:
				s = s + time
				secondsShown = seconds[s]
			secondsSelector.configure(text=secondsShown)
	h = 0
	m = 0
	s = 0
	# Up Selectors
	tk.Button(timerWindow, 
		text = '⯅', 
		font=('Helvetica',20), 
		fg='#43C42A', 
		bg='#000000', 
		border= 0, 
		height=0, 
		command = lambda: change_time_unit(1,0)
	).place(x=120,y=0)
	tk.Button(timerWindow, 
		text = '⯅', 
		font=('Helvetica',20), 
		fg='#43C42A', 
		bg='#000000', 
		border= 0, 
		height=0, 
		command = lambda: change_time_unit(1,1)
	).place(x=227,y=0)
	tk.Button(timerWindow, 
		text = '⯅', 
		font=('Helvetica',20), 
		fg='#43C42A', 
		bg='#000000', 
		border= 0, 
		height=0, 
		command = lambda: change_time_unit(1,2)
	).place(x=330,y=0)
	# Down Selectors
	tk.Button(timerWindow, 
		text = '⯆', 
		font=('Helvetica',20), 
		fg='#43C42A', 
		bg='#000000', 
		border= 0, 
		height=0, 
		command = lambda: change_time_unit(-1,0)
	).place(x=120,y=103)
	tk.Button(timerWindow, 
		text = '⯆', 
		font=('Helvetica',20), 
		fg='#43C42A', 
		bg='#000000', 
		border= 0, 
		height=0, 
		command = lambda: change_time_unit(-1,1)
	).place(x=227,y=103)
	tk.Button(timerWindow, 
		text = '⯆', 
		font=('Helvetica',20), 
		fg='#43C42A', 
		bg='#000000', 
		border= 0, 
		height=0, 
		command = lambda: change_time_unit(-1,2)
	).place(x=330,y=103)
	# Show time elements
	tk.Label(timerWindow, 
		text = hours[h], 
		name='hourSelector', 
		font=('Helvetica',55), 
		fg='#43C42A', 
		bg='#000000'
	).place(x=100,y=35)
	tk.Label(timerWindow, 
		text = ':', 
		font=('Helvetica',45), 
		fg='#43C42A', 
		bg='#000000'
	).place(x=185,y=35)
	tk.Label(timerWindow, 
		text = minutes[m], 
		name='minuteSelector', 
		font=('Helvetica',55), 
		fg='#43C42A', 
		bg='#000000'
	).place(x=205,y=35)
	tk.Label(timerWindow, 
		text = ':', 
		font=('Helvetica',45), 
		fg='#43C42A', 
		bg='#000000'
	).place(x=290,y=35)
	tk.Label(timerWindow, 
		text = seconds[s], 
		name='secondsSelector', 
		font=('Helvetica',55), 
		fg='#43C42A', 
		bg='#000000'
	).place(x=310,y=35)
	# Start Button
	tk.Button(timerWindow, 
		text='Start', 
		name='start', 
		font=('Helvetica',12), 
		border=0, 
		width=8, 
		fg='#000000', 
		bg='#43C42A', 
		command=start_count_down
	).place(x=210,y=155)
	# Always show the window above all
	timerWindow.attributes('-topmost',True)
	timerWindow.mainloop()
if __name__ == '__main__':
    main()
