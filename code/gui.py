# -*- coding: utf-8 -*-
# Code Documentation.
from tkinter import*
from tkinter import filedialog 
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter.ttk import Progressbar
from functools import partial
from shutil import copy2
import shutil
import subprocess
import time
import stat
import os

# MainWindow:
#
# Tk initializes this interpreter and creates the root window. 

# Variable: root
# 
# For intitialising GUI and creates the root window.

# Method: title
# 
# Changes title of tkinter root variable.
#

root = Tk()
root.title("Unified-Interface")
# Function: New()
#
# It creates new project.
# 
# def ref():
# 	fileStatsObj = os.stat (projectnameText.get()+"/pre-processing/"+gmshfile.get())
	 
# 	modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
# 	f=open(projectnameText.get()+"/stat")
# 	print(modificationTime)
# 	if f.readline()!=modificationTime:
# 		messagebox.showinfo("info",gmshfile.get()+" has bean changed after pre-processing")

# def refresh_stat():
# 	fileStatsObj = os.stat (projectnameText.get()+"/pre-processing/"+gmshfile.get()) 
# 	modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
# 	#print("written "+modificationTime)
# 	f=open(projectnameText.get()+"/stat","w")
# 	f.write(modificationTime)

def New():  
	# Method: toplevel
	# 
	# Creates the sub window.
	#

	top = Toplevel(root)
	top.title("Create Project")
	top.geometry("600x300+%d+%d" % (root.winfo_rootx() + 600,root.winfo_rooty() + 200))
	# Object: StringVar()
	# 
	# It is object of string class.
	#
	pathname = StringVar()
	# Method: set()
	# 
	# Assign a string value to string object.
	#
	pathname.set(os.getcwd())
	# Function: _browse()
	# 
	# To change the default location of project directories.
	# 
	def _browse():
		# Function: askdirectory()
		# 
		# It ask user to select a directory.
		#
		# Returns:
		# [Link of selected directory.]
		#
		path = askdirectory(title = 'Select folder to save results')
		pathname.set(path)
		# Function: _Create()
		#
		# After creating a project this function creates 3 new directories.
		#
		# *Pre-processing*
		# 
		# *Solver*
		#
		# *Post-processing*
		#
	def _Create():
		try:
			# Method: mkdir()
			# 
			# Creates new directory.
			#
			# Method: get()
			# 
			# Fetches value stored in *StringVar* object.
			# Method: showinfo()
			# 
			# It creates a pop up window to display information.
			#
			# Method: destroy()
			# 
			# It destroy the tikinter variable.
			#
			os.mkdir(pathname.get()+"/"+CreateEntry.get())
			os.mkdir(pathname.get()+"/"+CreateEntry.get()+"/"+"pre-processing")
			os.mkdir(pathname.get()+"/"+CreateEntry.get()+"/"+"post-processing")
			os.mkdir(pathname.get()+"/"+CreateEntry.get()+"/"+"solver")
			messagebox.showinfo("info",CreateEntry.get()+"file created succesfully")
			projectnameText.set(CreateEntry.get())
			projectpathText.set(os.getcwd()+"/"+projectnameText.get())
			top.destroy()
			cmd="./a "+ projectpathText.get()
			# print(cmd)
			#print(projectpathText.get())
			os.system(cmd)
			refresh_submenu()
			#refresh_stat()
			main()
			
		except OSError as error:
			# Method: showerror()
			# 
			# It creates an opo up window to display the errors.
			#
			# Object: Label()
			# 
			# It is used to create widgets.
			#
			# Object: grid()
			# 
			# It is a way of packing widgets in different way.
			#
			messagebox.showerror("Error",projectnameText.get()+" file already exists")
	createlabel = Label(top, text = 'Project name')
	createlabel.grid(row=2, column=0, pady=(50,10), padx=(10,0))
	createlabel = Label(top, text = 'Project location')
	createlabel.grid(row=3, column=0, pady=(10,10), padx=(10,10))
	CreateEntry = Entry(top, bd =1)
	CreateEntry.grid(row=2, column=1, pady=(50,10), padx=(0,0))
	BrowseEntry = Entry(top, textvariable = pathname, bd =1)
	BrowseEntry.grid(row=3, column=1, columnspan= 2, pady=(10,10), padx=(20,20))
	BrowseEntry.config(width=60)
	button = Button(top, height=1, width=20, text="Create", bg='gray97', command=_Create, relief=GROOVE)
	button1 = Button(top, height=1, width=20, text="Browse", bg='gray97', command=_browse, relief=GROOVE)
	button.grid(row=2, column=2, pady=(50,10), padx=(0,20))
	button1.grid(row=4, column=2, pady=(10,10), padx=(0,20))
	top.mainloop()  

# Function: Open()
# 
# To open a existing project.
#

def Open():
	top1 = Toplevel(root)
	top1.title("Open Project")
	top1.geometry("400x300+%d+%d" % (root.winfo_rootx() + 600,root.winfo_rooty() + 200))
	# Function: browsefunc()
	# 
	# Helps to browse a project in any other directory.
	#
	def browsefunc():
		pathofdir = askdirectory(title = 'Choose Project')
		projectpathText.set(pathofdir)
		projectnameText.set(pathofdir[pathofdir.rfind("/")+1:])
		currentdir = os.getcwd()
		# Method: chdir()
		# 
		# Changes the directory.
		#
		os.chdir(pathofdir)
		if os.path.isdir("pre-processing"):
			os.chdir(currentdir)
			top1.destroy()
			cmd="./a "+ pathofdir
			# print(cmd)
			# Method: system()
			# 
			# It ask kernel for a new system call.
			#
			os.system(cmd)
			refresh_submenu()
			# refresh_stat()
			main()
			
		else:
			messagebox.showerror("Error","Please select correct Project Directory")
			os.chdir(currentdir)
			# Object: Button()
			# 
			# It creates a button.
			#
	browsebutton = Button(top1, height=1, width=20, text="Browse", bg='gray97', command= browsefunc, relief=GROOVE)
	browsebutton.grid(row=2, column=0, pady=(10,10), padx=(120,20))
	labelText = StringVar()
	labelText.set("Open Project")
	pathlabel = Label(top1, textvariable = labelText)
	pathlabel.grid(row=1, column=0, pady=(100,10), padx=(120,20))

# Function: previous(n)
#
# Helps in getting latest working project.
# 
# Parameters:
#   n - it represent the nth project in recent project file log.
#

def previous(n):
	path=os.getcwd()+"/filelog"
	count = 0
	# counting number of working project in queu
	with open(path, 'r') as f:
	    for line in f:
	        count += 1
	f.close()
	# getting link of desired project and creating command for running script
	f=open(path)
	# Function: range()
	#
	# Creates integer in range from 0 to given parameter.
	#

	for i in range(count-n-1):
		f.readline()
	temp=f.readline()
	pathofdir=temp[:temp.rfind("\n")]
	cmd="./a "+ temp
	# checking selected link is valid or not
	#if valid
	try:
		# Method: rfind()
		# 
		# Finds last occurence of given string.
		#
		projectpathText.set(pathofdir)
		projectnameText.set(pathofdir[pathofdir.rfind("/")+1:])
		pwd=os.getcwd()
		os.chdir(pathofdir)
		os.chdir(pwd)
		messagebox.showinfo("info","Now your working project is "+projectpathText.get())
	#else
	except OSError as error:
			messagebox.showerror("Error",projectpathText.get()+" is no longer available")
			return
	os.system(cmd)
	main()
# Function: OpenGeo(gmshfile,makemshbutton)
#
# Opens the *.geo* file.
#
# Parameters:
#   gmshfile  - contains the name of geo file.
#   makemshbutton - makes the button selectable if geo file is selected successfully othervise it is disable.
# 


def OpenGeo(gmshfile,makemshbutton):
	top1 = Toplevel(root)
	top1.title("Open File(.geo)")
	top1.geometry("400x300+%d+%d" % (root.winfo_rootx() + 600,root.winfo_rooty() + 200))
	def browsefunc():
		# Method: askopenfilename()
		# 
		# It ask to select a file.
		#
		src =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("geo files","*.geo"),("all files","*.*")))
		gmshfile.set(src[src.rfind("/")+1:])
		dest = projectpathText.get()+"/"+"pre-processing"
		# Function: copy2()
		#
		# Copies the given file to specified location.
		#
		copy2(src,dest)
		# Method: config()
		# 
		# set property of widgets.
		#
		makemshbutton.config(state = 'normal')
		top1.destroy()		
	browsebutton = Button(top1, height=1, width=20, text="Browse", bg='gray97', command= browsefunc, relief=GROOVE)
	browsebutton.grid(row=2, column=0, pady=(10,10), padx=(120,20))
	labelText = StringVar()
	labelText.set("Choose a file...")
	pathlabel = Label(top1, textvariable = labelText)
	pathlabel.grid(row=1, column=0, pady=(100,10), padx=(120,20))

# Function: Preprocessing(gmshfile)
#
# Executes the command of pre-processing software (*Gmsh*).
# 
# Parameters:
#   gmshfile  - contains the name of geo file.
#

def Preprocessing(gmshfile):
	gmshfile1 = gmshfile.get()
	mshfile = gmshfile1[:gmshfile1.rfind(".")]+".msh"
	cmd = "gmsh -2 "+ projectpathText.get()+"/pre-processing/"+gmshfile.get()
	currentdir = os.getcwd()
	os.chdir(projectnameText.get())
	os.chdir("pre-processing")
	cmd2 = "gmsh "+mshfile 
	os.system(cmd)
	os.system(cmd2)
	os.chdir(currentdir)
	refresh()
	# refresh_stat()
# Function: Solving(flmlfile)
#
# Executes the command of Solver Software (*Fluidity/Open-FOAM*).
# Parameters:
#   flmlfile - The first argument.
#
def Solving(flmlfile):
	currentdir = os.getcwd()
	os.chdir(projectnameText.get())
	cmd = "fluidity "+"solver/"+flmlfile.get()
	os.system(cmd)
	os.chdir(currentdir)
	os.chdir("2dtank")
	x = [f.name for f in os.scandir() if f.is_file()]
	os.chdir(currentdir)
	for i in x:
		shutil.move("2dtank/"+i ,"2dtank/post-processing/"+i)
	refresh()


# Function: Postprocessing()
#
# It plots the data that we receive from solving.
#
def Postprocessing():
	cmd = "python plot_data.py"
	os.system(cmd)
	refresh()
# Function: main()
#
# After selecting a project it normalise all buttons which are previously in disable state.
#
def main():
	btn1.config(state = 'normal')
	btn2.config(state = 'normal')
	btn3.config(state = 'normal')
	btn4.config(state = 'normal')
	refresh()
	pass
# Function: _CreateGeo()
#
# It creates a new .geo file.
#
def _CreateGeo():
	os.chdir(projectnameText.get())
	os.chdir("pre-processing")
	subprocess.run("gmsh")
	os.chdir("../..")

	pass

# Function: refresh()
#
# It refreshs the status of progress bar.
#

def refresh():
	pathmsh = projectpathText.get()+"/pre-processing/"
	pathvtu = projectpathText.get()+"/post-processing/"
	ref()
	filesmsh = []
	filesvtu = []
	filespara = []
	for r, d, f in os.walk(pathmsh):
		for file in f:
			if '.msh' in file:
				filesmsh.append(file)
	for r, d, f in os.walk(pathvtu):
		for file in f:
			if '.vtu' in file:
				filesvtu.append(file)


	if(len(filesmsh)!=0):
		progress['value'] = 33
	if(len(filesvtu)!=0):
		progress['value'] = 66
	pass

# Function: update_recent_bot(n)
#
# To update the names of recently made buttons.
#

	
def update_recent_bot(n):
	path=os.getcwd()+"/filelog"
	count = 0
	f=open(path,'a')
	f.close()
	# counting number of working project in queu
	with open(path, 'r') as f:
	    for line in f:
	        count += 1
	f.close()
	if(count<n):
		return "nothing"
	# getting link of desired project and creating command for running script
	f=open(path)
	for i in range(count-n):
		f.readline()
	temp=f.readline()
	pathofdir=temp[:temp.rfind("\n")]
	return pathofdir[pathofdir.rfind("/")+1:]
# Function: refresh_submenu()
# 
# It refresh the recent projects in submenu.
#


def refresh_submenu():
	Recent_1.set(update_recent_bot(1))
	Recent_2.set(update_recent_bot(2))
	if Recent_1.get()=="nothing":
		# Method: entryconfigure()
		# 
		# Sets property of entry.
		#
		submenu.entryconfigure(1,state=DISABLED,label="no recent1")
	else:
		submenu.entryconfigure(1,label="R1:- "+Recent_1.get(),state='normal')
	if Recent_2.get()=="nothing":
		submenu.entryconfigure(2,state=DISABLED,label="no recent2")
	else:
		submenu.entryconfigure(2,label="R2:- "+Recent_2.get(),state='normal')
# Function: deletepre(gmshoption1,gmshoption2,geolable,popupMenu,gmshcheck,geobutton,geobutton1,makemshbutton):
#
#  It deletes the widgets of *pre-processing* window.
#

def deletepre(gmshoption1,gmshoption2,geolable,popupMenu,gmshcheck,geobutton,geobutton1,makemshbutton):
	gmshoption1.destroy()
	gmshoption2.destroy()
	geolable.destroy()
	popupMenu.destroy()
	gmshcheck.destroy()
	geobutton.destroy()
	geobutton1.destroy()
	makemshbutton.destroy()
	usingsolver()

# Function: deletesolver(solveroption1,solveroption2,solverlable,solverbutton,solverbutton1,popupMenu1,popupMenu2,solvebutton)
# 
# It deletes the widgets of *solver* window.
#
def deletesolver(solveroption1,solveroption2,solverlable,solverbutton,solverbutton1,popupMenu1,popupMenu2,solvebutton):
	solveroption1.destroy()
	solveroption2.destroy()
	solverlable.destroy()
	popupMenu1.destroy()
	popupMenu2.destroy()
	solvebutton.destroy()
	solverbutton.destroy()
	solverbutton1.destroy()
	usingpost()

# Function: usingpre()
#
# It open the pre-processing window.
#

def usingpre():
	gmshfile = StringVar()
	gmshfile.set("Choose your .geo file")
	gmsh1 = StringVar()
	geoavailvar = IntVar()
	btn1.config(relief=SUNKEN)
	btn2.config(relief=RAISED)
	btn3.config(relief=RAISED)
	rightframe.grid()
	choices = { '2-dimensional','3-dimensional'}
	gmsh1.set('2-dimensional')

	# Function: change_dropdown(*args)
	# 
	# To change the contents of drop down menu.
	#
	
	def change_dropdown(*args):
		print( gmsh1.get() )

	gmsh1.trace('w', change_dropdown)

	softwarelabel = Label(rightframe,text = 'GMSH',width = 130, height=0,anchor = CENTER, font=("Helvetica", 20),highlightbackground="black",highlightthickness=1)
	gmshoption1 = Label(rightframe,text = 'Mesh Format',width = 50, height=5,anchor = CENTER, font=("Times", 16))
	gmshoption2 = Label(rightframe,text = 'Geo file available',width = 50, height=2,anchor = CENTER ,font=("Times", 16))
	geolable = Label(rightframe,textvariable = gmshfile,width = 60, height=2,anchor = CENTER, font=("Times", 12))
	popupMenu = OptionMenu(rightframe, gmsh1, *choices)
	gmshcheck = Checkbutton(rightframe, variable= geoavailvar,width=2,height=2)
	makemshbutton = Button(rightframe, height=2, width=20, text="Create mesh", command=partial(Preprocessing,gmshfile), relief=RAISED,bg="lightgreen",fg="black",state=DISABLED)
	geobutton = Button(rightframe, height=1, width=20, text="Browse", command=partial(OpenGeo,gmshfile,makemshbutton), relief=GROOVE)
	geobutton1 = Button(rightframe, height=1, width=20, text="Create",  command=_CreateGeo, relief=GROOVE)
	continuebutton = Button(rightframe, height=2, width=20, text="Continue", command= partial(deletepre,gmshoption1,gmshoption2,geolable,popupMenu,gmshcheck,geobutton,geobutton1,makemshbutton), relief=RAISED,bg="red",fg="white")

	softwarelabel.grid(row = 0,sticky="we",padx=(0,1200))
	gmshoption1.grid(row = 1,sticky="nw")
	gmshoption2.grid(row = 2,sticky="nw")
	popupMenu.grid(row = 1,padx=340 ,sticky="w")
	gmshcheck.grid(row=2,sticky="w",padx=390)
	currentdir = os.getcwd()
	# os.chdir(projectnameText.get())
	# os.chdir("pre-processing")
	path = projectpathText.get()+"/pre-processing/"
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			if '.geo' in file:
				files.append(file)
	if (len(files)==0):
		geolable.grid(row = 2,sticky="w",padx=500)
		geobutton.grid(row = 2,sticky="w",padx=890)
		geobutton1.grid(row = 2,sticky="w",padx=1090)
		gmshcheck.deselect()
	elif (len(files)==1):
		gmshcheck.select()
		gmshfile.set(files[0])
		geolable.grid(row = 2,sticky="w",padx=500)
		makemshbutton.config(state = 'normal')
	else :
		messagebox.showerror("Error","Your Project(pre-processing) Directory cannot contain more than one .geo file")
	makemshbutton.grid(row = 3,sticky="nw",padx=170,pady=30)
	continuebutton.grid(row = 4,sticky="nw",padx=170,pady=570)
	pass
# Function: usingsolver()
#
# It open the solver software window.
#
def usingsolver():
	solverdrop1 = StringVar()
	solverdrop2 = StringVar()
	flmlfile = StringVar()
	flmlfile.set("Choose your .flml file")
	btn2.config(relief=SUNKEN)
	btn1.config(relief=RAISED)
	btn3.config(relief=RAISED)
	rightframe.grid_remove()
	rightframe.grid()
	choices1 = { 'Series','Parallel'}
	solverdrop1.set('Parallel')
	choices2 = { '1','2','3','4'}
	solverdrop2.set('4')
	def change_dropdown1(*args):
		print( solverdrop1.get() )

	solverdrop1.trace('w', change_dropdown1)

	def change_dropdown2(*args):
		print( solverdrop2.get() )

	solverdrop1.trace('w', change_dropdown2)

	softwarelabel1 = Label(rightframe,text = 'Fluidity',width = 100, height=0,anchor = W, font=("Helvetica", 20),highlightbackground="black",highlightthickness=1)
	softwarelabel2 = Label(rightframe,text = 'OpenFoam',width = 100, height=0,anchor = W, font=("Helvetica", 20),highlightbackground="black",highlightthickness=1)
	solveroption1 = Label(rightframe,text = 'Processor Usage',width = 50, height=5,anchor = CENTER, font=("Times", 16))
	solveroption2 = Label(rightframe,text = 'Number of Processor',width = 50, height=2,anchor = CENTER ,font=("Times", 16))
	solverlable = Label(rightframe,textvariable = flmlfile,width = 60, height=2,anchor = CENTER, font=("Times", 12))
	solverbutton = Button(rightframe, height=1, width=20, text="Browse", command=OpenGeo, relief=GROOVE)
	solverbutton1 = Button(rightframe, height=1, width=20, text="Create",  command=_CreateGeo, relief=GROOVE)
	#solveroption3 = Label(rightframe,text = 'Timestep',width = 50, height=5,anchor = CENTER, font=("Times", 16))
	#solveroption4 = Label(rightframe,text = 'Simulation',width = 50, height=2,anchor = CENTER ,font=("Times", 16))
	popupMenu1 = OptionMenu(rightframe, solverdrop1, *choices1)
	popupMenu2 = OptionMenu(rightframe, solverdrop2, *choices2)
	#BrowseEntry1 = Entry(rightframe)
	#BrowseEntry2 = Entry(rightframe)
	
	solvebutton = Button(rightframe, height=2, width=20, text="Solver", command=partial(Solving,flmlfile), relief=RAISED,bg="lightgreen",fg="black",state=DISABLED)
	continuebutton = Button(rightframe, height=2, width=20, text="Continue", command=partial(deletesolver,solveroption1,solveroption2,solverlable,solverbutton,solverbutton1,popupMenu1,popupMenu2,solvebutton), relief=RAISED,bg="red",fg="white")
	change_dropdown1(*args)

	softwarelabel1.grid(row = 0,sticky="w",padx=(00,500))
	softwarelabel2.grid(row = 0,sticky="w",padx=(800,600))
	solveroption1.grid(row = 1,sticky="nw")
	solveroption2.grid(row = 2,sticky="nw")
	#solveroption3.grid(row = 1,sticky="nw",padx=500)
	#solveroption4.grid(row = 2,sticky="nw",padx=500)
	popupMenu1.grid(row = 1,padx=390 ,sticky="w")
	popupMenu2.grid(row = 2,padx=390 ,sticky="w")
	path = projectpathText.get()+"/solver/"
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			if '.flml' in file:
				files.append(file)
	if (len(files)==0):
		solverlable.grid(row = 2,sticky="w",padx=500)
		solverbutton.grid(row = 2,sticky="w",padx=890)
		solverbutton1.grid(row = 2,sticky="w",padx=1090)
		#gmshcheck.deselect()
	elif (len(files)==1):
		#gmshcheck.select()
		flmlfile.set(files[0])
		solverlable.grid(row = 2,sticky="w",padx=500)
		solvebutton.config(state = 'normal')
	else :
		messagebox.showerror("Error","Your Project(solver) Directory cannot contain more than one .flml file")
	
	#BrowseEntry1.grid(row = 1,padx=940 ,sticky="w")
	#BrowseEntry2.grid(row = 2,padx=940 ,sticky="w")

	solvebutton.grid(row = 3,sticky="nw",padx=170,pady=30)
	continuebutton.grid(row = 4,sticky="nw",padx=170,pady=570)
	pass

# Function: usingpost()
# 
# It open the post processing software window.
#
def usingpost():
	postdrop1 = StringVar()
	postdrop2 = StringVar()
	btn3.config(relief=SUNKEN)
	btn2.config(relief=RAISED)
	btn1.config(relief=RAISED)
	rightframe.grid_remove()
	rightframe.grid()
	choices1 = { 'Volume fraction','Pressure','Velocity'}
	postdrop1.set('Velocity')
	choices2 = { 'debris','frout'}
	postdrop2.set('debris')
	
	def change_dropdown1(*args):
		print( postdrop1.get() )

	postdrop1.trace('w', change_dropdown1)

	def change_dropdown2(*args):
		print( postdrop2.get() )

	postdrop1.trace('w', change_dropdown2)

	postlabel1 = Label(rightframe,text = 'Paraview',width = 100, height=0,anchor = W, font=("Helvetica", 20),highlightbackground="black",highlightthickness=1)
	postlabel2 = Label(rightframe,text = 'Python',width = 100, height=0,anchor = W, font=("Helvetica", 20),highlightbackground="black",highlightthickness=1)
	postoption1 = Label(rightframe,text = 'Animation',width = 50, height=5,anchor = CENTER, font=("Times", 16))
	postoption2 = Label(rightframe,text = 'Plot',width = 50, height=2,anchor = CENTER ,font=("Times", 16))
	postlable3 = Label(rightframe,text = 'Choose your .vtu file',width = 60, height=2,anchor = CENTER, font=("Times", 12))
	postbutton = Button(rightframe, height=1, width=20, text="Browse", command=OpenGeo, relief=GROOVE)
	popupMenu1 = OptionMenu(rightframe, postdrop1, *choices1)
	popupMenu2 = OptionMenu(rightframe, postdrop2, *choices2)
	viewbutton = Button(rightframe, height=2, width=20, text="Play",command = Postprocessing, relief=RAISED,bg="lightgreen",fg="black")
	continuebutton = Button(rightframe, height=2, width=20, text="Exit", command=root.quit, relief=RAISED,bg="red",fg="white")



	postlabel1.grid(row = 0,sticky="w",padx=(00,500))
	postlabel2.grid(row = 0,sticky="w",padx=(800,600))
	postoption1.grid(row = 1,sticky="nw")
	postoption2.grid(row = 2,sticky="nw")
	popupMenu1.grid(row = 1,padx=390 ,sticky="w")
	popupMenu2.grid(row = 2,padx=390 ,sticky="w")
	postlable3.grid(row = 2,sticky="w",padx=500)
	postbutton.grid(row = 2,sticky="w",padx=890)



	viewbutton.grid(row = 3,sticky="nw",padx=170,pady=30)
	continuebutton.grid(row = 4,sticky="nw",padx=170,pady=570)
	pass

# Variables: projectnameText 
# It stores the name of project
#
# Variables: projectpathText 
# It stores the path of project
# 
# Variables: Recent_1
# It contains the first label of recent projects.
#
# It open the post processing software window.
projectnameText = StringVar()
projectpathText = StringVar()
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 

submenu = Menu(filemenu)
Recent_1=StringVar()
Recent_2=StringVar()
#submenu.add_command(label="Recent 2",command=partial(previous,1))		
submenu.add_command(label="no recent",command=partial(previous,0))
submenu.add_command(label="no recent",command=partial(previous,1))
#submenu.add_command(label="refresh",command=partial(ref))
refresh_submenu()
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New Project' , command = New, font=('Verdana', 10)) 
filemenu.add_command(label='Open Project', command = Open, font=('Verdana', 10) ) 
filemenu.add_separator() 
filemenu.add_cascade(label='Recent Projects', menu = submenu, font=('Verdana', 10) ) 
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit, font=('Verdana', 10)) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About', font=('Verdana', 10)) 
helpmenu.add_command(label='Documentation', font=('Verdana', 10)) 

root.geometry("1600x900")
var1 = IntVar()
var2 = IntVar() 
var3 = IntVar() 
var4 = IntVar() 
var5 = IntVar() 
var6 = IntVar() 
var7 = IntVar() 
var8 = IntVar() 
var9 = IntVar()


topframe = Frame(root,height=14)
bottomframe = Frame(root,height=950)
leftframe  = Frame(bottomframe,width=400,height=950,highlightbackground="black",highlightthickness=1,bg='#bababa')
rightframe  = Frame(bottomframe,width=1640,height=950,highlightbackground="black",highlightthickness=1)


topframe.grid(row=0,sticky="nsew")
bottomframe.grid(row=0,sticky="nsew")
leftframe.grid(column=0,row=1,sticky="nw")
rightframe.grid(column=1,row=1,sticky="nw")



btn1 = Button(leftframe, text = "Pre-Processor", command = usingpre,state = DISABLED, height = 3,width = 40)  
btn2 = Button(leftframe, text = "Solver", command = usingsolver,state = DISABLED,  height = 3,width = 40)  
btn3 = Button(leftframe, text = "Post-Processor", command = usingpost,state = DISABLED,  height = 3,width = 40)  
btn4 = Button(leftframe, text = "Refresh Progress", state = DISABLED, command = refresh,  height = 2,width = 20) 
proglabel0 = Label(leftframe,text = "*********Project-Name*********",anchor = CENTER ,font=("Times", 16),bg='#bababa')
proglabel1 = Label(leftframe,textvariable=projectnameText,anchor = CENTER ,font=("Times", 16),bg='#bababa')
proglabel2 = Label(leftframe,text = "******************************" ,anchor = CENTER ,font=("Times", 16),bg='#bababa') 
prog1 = Label(leftframe,text = 'post-processing',anchor = CENTER ,font=("Times", 16),bg='#bababa')
prog2 = Label(leftframe,text = 'solving',anchor = CENTER ,font=("Times", 16),bg='#bababa')
prog3 = Label(leftframe,text = 'pre-processing',anchor = CENTER ,font=("Times", 16),bg='#bababa')
software = Label(leftframe,text = "Unified-Interface for CFD Softwares" ,anchor = CENTER ,font=("cosmic", 16),bg='#bababa',wraplength=250) 

progress = Progressbar(leftframe, orient = VERTICAL, length = 270, mode = 'determinate') 


btn1.grid(row =0)
btn2.grid(row =1)
btn3.grid(row =2)
proglabel0.grid(row = 3, pady =10)
proglabel1.grid(row = 4, pady =10)
proglabel2.grid(row = 5, pady =10)
btn4.grid(row =6,pady = (100,0))
progress.grid(pady = 30, padx=(265,0), row = 7,rowspan = 3)
prog1.grid(row = 7, pady =(80,30))
prog2.grid(row = 8, pady =(20,20))
prog3.grid(row = 9, pady =(30,100))
software.grid(row = 10, pady =(120,20))

# mshfile = StringVar()
# projectnameText = StringVar()
# projectpathText = StringVar()
# projectnameText.set("Please Open a Project")
# projectpathText.set("**Project-LOCATION**")
# namelabel = Label(leftframe, textvariable = projectnameText)
# pathlabel = Label(rightframe, textvariable = projectpathText)
# namelabel.pack(pady = 5)
# pathlabel.pack(pady = 5)

root.mainloop()
