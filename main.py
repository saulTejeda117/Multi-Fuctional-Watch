# Main Multifunctional Watch

import tkinter as tk



def main():
	# MainWindow widgets
	mainWindow = tk.Tk()
	mainWindow.title('Stop Watch')
	mainWindow.configure(width=500,height=200, bg='#000000')
	mainWindow.resizable(False, False)
	
	def call_timer():
		print('a')
	def call_stopwatch():
		print('b')
	def call_alarm():
		print('c')
	def call_pomodoro():
		print('d')

	# Main fuctionalities:
	# -> Stopwatch
	# -> Timer
	# -> Alarm Clock
	# -> Pomodoro

	tk.Button(mainWindow, name='stopwatch', text='Stopwatch', command=lambda:call_stopwatch(), width=10, font=('Helvetica',14),fg = '#43C42A', bg='#000000', border = 2).place(x=5,y=10)
	tk.Button(mainWindow, name='timer', text='Timer', command=lambda:call_timer(), width=10, font=('Helvetica',14), border = 0, bg = '#43C42A').place(x=130,y=10)
	tk.Button(mainWindow, name='alarm', text='Alarm Clock', command=lambda:call_alarm(), width=10, font=('Helvetica',14), border = 0, bg = '#43C42A').place(x=255,y=10)
	tk.Button(mainWindow, name='pomodoro', text='Pomodoro', command=lambda:call_pomodoro(), width=10, font=('Helvetica',14), border = 0, bg = '#43C42A').place(x=380,y=10)
	mainWindow.mainloop()
main()