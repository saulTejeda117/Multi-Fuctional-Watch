# Alarm Clock Function

# GUI Dependencies
import tkinter as tk

# Events Schedule Dependencies
# import schedule

def main():
	def set_alarm():
		setAlarmWindow = tk.Tk()
		# setAlarmWindow features
		setAlarmWindow.title('Alarm Clock')
		setAlarmWindow.configure(width=500, height=200, bg='#000000')
		setAlarmWindow.resizable(False, False)
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
		def save_alarm():
			global h
			global m
			global s
			print(hours[h], ':', minutes[m], ':', seconds[s])
		def change_time_unit(time, timeUnit):
			global h
			global m
			global s
			if(timeUnit == 0):
				hourSelector = setAlarmWindow.nametowidget('hourSelector')
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
				minuteSelector = setAlarmWindow.nametowidget('minuteSelector')
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
				secondsSelector = setAlarmWindow.nametowidget('secondsSelector')
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
		# Up Buttons
		tk.Button(setAlarmWindow, text = '⯅', font=('Helvetica',12), fg='#43C42A', bg='#000000', border= 0, height=0, command = lambda: change_time_unit(1,0)).place(x=185,y=0)
		tk.Button(setAlarmWindow, text = '⯅', font=('Helvetica',12), fg='#43C42A', bg='#000000', border= 0, height=0, command = lambda: change_time_unit(1,1)).place(x=235,y=0)
		tk.Button(setAlarmWindow, text = '⯅', font=('Helvetica',12), fg='#43C42A', bg='#000000', border= 0, height=0, command = lambda: change_time_unit(1,2)).place(x=285,y=0)
		# Down Buttons
		tk.Button(setAlarmWindow, text = '⯆', font=('Helvetica',12), fg='#43C42A', bg='#000000', border= 0, height=0, command = lambda: change_time_unit(-1,0)).place(x=185,y=60)
		tk.Button(setAlarmWindow, text = '⯆', font=('Helvetica',12), fg='#43C42A', bg='#000000', border= 0, height=0, command = lambda: change_time_unit(-1,1)).place(x=235,y=60)
		tk.Button(setAlarmWindow, text = '⯆', font=('Helvetica',12), fg='#43C42A', bg='#000000', border= 0, height=0, command = lambda: change_time_unit(-1,2)).place(x=285,y=60)
		# Show time elements
		tk.Label(setAlarmWindow, text = hours[h], name='hourSelector', font=('Helvetica',25), fg='#43C42A', bg='#000000').place(x=175,y=22)
		tk.Label(setAlarmWindow, text = ':', font=('Helvetica',15), fg='#43C42A', bg='#000000').place(x=215,y=27)
		tk.Label(setAlarmWindow, text = minutes[m], name='minuteSelector', font=('Helvetica',25), fg='#43C42A', bg='#000000').place(x=225,y=22)
		tk.Label(setAlarmWindow, text = ':', font=('Helvetica',15), fg='#43C42A', bg='#000000').place(x=265,y=27)
		tk.Label(setAlarmWindow, text = seconds[s], name='secondsSelector', font=('Helvetica',25), fg='#43C42A', bg='#000000').place(x=275,y=22)
		# "Repit it every" Menu
		tk.Label(setAlarmWindow, text= 'Repit Alarm: ', font=('Helvetica',10), fg='#43C42A', bg='#000000').place(x=150,y=85)
		selectionEvent = tk.StringVar(setAlarmWindow)
		event_repetition = ['Once','Every Day','Every Week','Every Weekend'] 
		selectionEvent.set(event_repetition[0])
		tk.OptionMenu(setAlarmWindow, event_repetition, *event_repetition).place(x=250,y=85)
		# Start Button
		tk.Button(setAlarmWindow, name='save', text='Save', command=lambda:save_alarm(), width=8, font=('Helvetica',12), border = 0, bg = '#43C42A').place(x=150,y=155)
		tk.Button(setAlarmWindow, name='check', text='Alarms', command=lambda:stop_screen(), width=8, font=('Helvetica',12), border = 0, bg = '#43C42A').place(x=260,y=155)
		setAlarmWindow.mainloop()

main()