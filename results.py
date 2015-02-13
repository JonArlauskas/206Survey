#!/usr/bin/python

import urllib
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

def main():
	
	f = open ('results.ssv', 'a+')

#open url with survey questions, put into two lists		
	link = "http://cs.mcgill.ca/~lvancr/cgi-bin/survey.ssv"
	g = urllib.urlopen(link)
	myfile = g.read()
	mywords = myfile.split(" ")
	title = mywords[0]
	title = title.replace("&"," ")
	questions = mywords[1:]
	questions = [s.replace("&"," ") for s in questions]

#iterate through form values and append to ssv file
	for x in range(1, len(questions) + 1):
		if form.getvalue("%d" % x):
			temp = form.getvalue("%d" % x)
                	f.write((temp + " "))
			#lines = f.readlines()
        		#for line in lines:
                		#answers = line.split(" ")
		else:
			break
	f.write("\r\n")
	
	f.close()	

#open file again, this time for reading only
	answers = []
	fi = open('results.ssv', 'r')
	m = fi.readlines()
	numOfLines = 0
	for line in m:
		if len(line)>0:
			data = line.split()
			answers.append((data))
			numOfLines+=1
		else:
			break
	num = numOfLines - 1
	size = len(answers) - 1
	
#generate html script	
	print("Content-Type: text/html\n\n")

	print("""
	
	<html>

	<head>
	<title> goSurvey</title>
	<link rel="stylesheet" href="http://cs.mcgill.ca/~jarlau/style.css">
	</head>

	<body>
	<body bgcolor="white" text="blue">

	<center><a href="index.html" title="Return Home" id="logo">
	<img src="http://cs.mcgill.ca/~jarlau/goSurvey_Logo.png" alt="Logo" height="110" width="504"/>
	</a></center>

	<ul id="nav">
        	<li><a href="http://www.cs.mcgill.ca/~rlawso2/index.html">Home page</a>
        	<li><a href="http://www.cs.mcgill.ca/~rlawso2/login.html">Login</a>
        	<li><a href="http://www.cs.mcgill.ca/~jarlau/cgi-bin/survey.py">Take Survey</a>
	</ul> """)
	print("""
	<font face="helvetica" size="6"color="orange">
	</br><u>Results Page</u>
	<p> Survey:""")
	print title
	print("""</font>
	<p>
	<p>""")

#	print(""" List of Questions:""")
 #       print("""<p>""")
  #      for r in questions:
   #     	print "\n".join(questions)

#Print out the results totals
	for d in range(0, len(questions)):
	
		print("""<b>""")
		print("""Question Number:""")
		print d
		print("""<p>""")
		print("""</b>""")
		print("""<p><p>""")
		SA = 0
		A = 0
		D = 0
		SD = 0
		#t=0
		#w=t+1
	 	#for r in questions:
		#	print questions[t:w]
		#	t=t+1
		#	w=w+1			
		print("""<p>""")
		print("""Strongly Agree:""")
		y = 0
		for z in range(0, numOfLines):
			if int(answers[z][d]) == 1:
				SA+=1
		print SA
		print("""</br>Agree:""")
		a = 0
		for z in range(0, numOfLines):
                        if int(answers[z][d]) == 2:
                                A+=1
		print A
		print("""</br>Disagree:""")
		b = 0
		for z in range(0, numOfLines):
                        if int(answers[z][d]) == 3:
                                D+=1
		print D
		print("""</br>Strongly Disagree:""")
		c = 0
		for z in range(0, numOfLines):
                        if int(answers[z][d]) == 4:
                                SD+=1
		print SD
		print("""<p>
		<p>""")
		avg = float(SA*1 + A*2 + D*3 + SD*4)/float(SA+A+D+SD) 
		print("""
		<b>Average</b>:""")
		print float(avg)
		print "</br>"
		print "<p>"
	print(""" </br>
	<form method="link"action=http://cs.mcgill.ca/~rlawso2/>
	<input type="submit" value="Return Home">
	</form>
	""")
	print("""	
	</body>

	</html> """)

main ()

