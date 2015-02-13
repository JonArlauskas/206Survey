#!/usr/bin/python
import urllib
import cgi
form = cgi.FieldStorage()
def main():

#open url link for reading the survey titles and questions
	link = "http://cs.mcgill.ca/~lvancr/cgi-bin/survey.ssv"
	f = urllib.urlopen(link)
	myfile = f.read()
	mywords = myfile.split(" ")
	title = mywords[0]
	title = title.replace("&"," ")
	questions = mywords[1:]
	questions = [s.replace("&"," ") for s in questions]
	
#print html content
	print("Content-Type: text/html\n\n") 

	print("""

	<html>
	<head>
	<title> goSurvey</title>
	<link rel="stylesheet" href="http://cs.mcgill.ca/~jarlau/style.css">
	</head>
	
	
	<body bgcolor="white" text="blue">
	<center><a href="index.html" title="Return Home" id="logo">
	<img src="http://cs.mcgill.ca/~jarlau/goSurvey_Logo.png" alt="Logo" height="110" width="504"/>
	</a></center>
	
	<ul id="nav">
	        <li><a href="http://www.cs.mcgill.ca/~rlawso2/index.html">Home page</a>
	        <li><a href="http://www.cs.mcgill.ca/~rlawso2/login.html">Login</a>
	        <li><a href="http://www.cs.mcgill.ca/~jarlau/index.html">Take Survey</a>
	</ul> """)
	print("""
	<font face="helvetica" size="6"color="orange">
	Take Survey:""") 
	print title
	qCount = 0
	print("""</font><p>
	<form action="./results.py" method = "get"> """)	

#print out the submitted questions along with radio buttons
	for p in questions:
		qCount = (qCount+1)
		print p
		print("""<p>""")
		print ("""<input type="radio" name=%d value="1">Strongly Agree</br>""") %(qCount)
		print("""<input type="radio" name=%d value="2">Agree</br>""") %(qCount)
		print("""<input type="radio" name=%d value="3">Disagree</br>""") %(qCount)
		print("""<input type="radio" name=%d value="4">Strongly Disagree</br>""") %(qCount) 
		print("""
		<p>
		<p>
		""")
	print("""
	<input type="submit" value="Submit">
	</form>

	
	
	
	</body>
	</html>""")
main()	
