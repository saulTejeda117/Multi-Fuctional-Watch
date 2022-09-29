# Alarm Clock Function
#
# GUI Dependencies
import tkinter as tk
# Events Schedule Dependencies
# import schedule
# Search file
import os
def main():
	alaramWindow = tk.Tk()
	# MainWindow Features
	alaramWindow.title('Alarm Clock')
	alaramWindow.configure(width=500, height=200, bg='#000000')
	alaramWindow.resizable(False, False)
	def show_alarm_list():
		fileExists = os.path.exists('EventList.txt')
		if (fileExists == True):
			with open("EventList.txt") as f: 
				lines = f.readlines()
		else:
		    with open("EventList.txt", "w") as f: f.write(hours[h]+':'+minutes[m]+':'+seconds[s]+'\n')
		i = 0
		# Create Screen Elements of the Alarm
		while(len(lines)>i):

			print(lines[i])
			i+=1
	show_alarm_list()
	tk.Button(alaramWindow, name='add', text='Add Alarm', command=lambda:set_alarm(), width=8, font=('Helvetica',12), border = 0, bg = '#43C42A').place(x=260,y=155)
	def set_alarm():
		alaramWindow.destroy()
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
		def save_alarm(alarmName):
			global h
			global m
			global s
			fileExists = os.path.exists('EventList.txt')
			if (fileExists == True):
			    with open("EventList.txt", "a") as f:
			        f.write(alarmName+' '+hours[h]+':'+minutes[m]+':'+seconds[s]+'\n')
			else:
			    with open("EventList.txt", "w") as f:
			        f.write(alarmName+' '+hours[h]+':'+minutes[m]+':'+seconds[s]+'\n')
			setAlarmWindow.destroy()
			main()
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
		# Alarm 
		tk.Label(setAlarmWindow, text = 'Alarm Label: ', font=('Helvetica',12), fg='#43C42A', bg='#000000').place(x=150,y=90)
		tk.Entry(setAlarmWindow, name = 'alarmEntry', width=18, bg='#43C42A').place(x=250,y=90)
		# "Repit it every" Drop Down Menu
		tk.Label(setAlarmWindow, text= 'Repit  Alarm: ', font=('Helvetica',12), fg='#43C42A', bg='#000000').place(x=150,y=120)
		selectionEvent = tk.StringVar(setAlarmWindow)
		event_repetition = ['Once','Every Day','Every Week','Every Weekend'] 

		selectionEvent.set(event_repetition[0])
		dropDownMenu = tk.OptionMenu(setAlarmWindow, selectionEvent, *event_repetition)
		dropDownMenu.config(bg='black')
		dropDownMenu.place(x=250,y=120)
		
		dropDownMenu['width']=12
		dropDownMenu["highlightthickness"]=0
		dropDownMenu["border"]=1
		dropDownMenu['activebackground']='#000000'
		dropDownMenu['activeforeground']='#43C42A'
		dropDownMenu['bg']='#000000'
		dropDownMenu['foreground']='#43C42A'
		dropDownMenu['height']=1

		# Get data from entryAlarm
		alarmEntry = setAlarmWindow.nametowidget('alarmEntry')
		# Save Alarm Button
		tk.Button(setAlarmWindow, name='save', text='Save', command=lambda:save_alarm(alarmEntry.get()), width=8, font=('Helvetica',12), border = 0, bg = '#43C42A').place(x=150,y=160)
		# Return to Alarm List Window
		tk.Button(setAlarmWindow, name='check', text='Alarms', command=lambda:stop_screen(), width=8, font=('Helvetica',12), border = 0, bg = '#43C42A').place(x=260,y=160)
		setAlarmWindow.mainloop()
	alaramWindow.mainloop()
main()