# SB_5410_HW1.1
Scott Bing BSSD5410 Homework Assignment #1
08/21/2020

Homework Due before 10PM Mon.
Send me an email from an address that you will check throughout the semester. When there are class announcements such as changes in assignment date or content, you will receive a group email alerting you about such things.

Send an email with the answers to questions 1-3 to jlee.nmhu@gmail.com

Give your email the subject as shown below depending on which level of the course you are in.
BSSD 3410 Homework 1.1 or
BSSD 5410 Homework 1.1

1.	Having read about Bubble Sort from above, tell me in your email the Big O complexity of an iterative Bubble Sort implementation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**O(n2) one inner sort  O(n) * one outer sort O(n) = O(n2); however, if the input data is already sorted it just needs to make one pass visiting each input element  	O(n)**

2.	Research and explain in your email what Big Theta and Big Omega are and how they relate to Big O.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Summary**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Big Ω &rarr; Ω(n)) - Best Case Scenario**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Big O &rarr; O(n) - Worst Case Scenario**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Big θ &rarr; θ(n)  - Average Case**<br>

3.	Answer these 4 questions in your email:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.	What is the Big O notation for the complexity of printing the value of each element in an array?<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**__O(n)__**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.	What is the Big O notation for the complexity of doubling the value of each element in an array?<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**__O(2n)__**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.	What is the Big O notation for the complexity of doubling the value of just the third element in an array of length 10?<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**__O(n) – the doubling operation is constant time O(1)__**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d.	Given an algorithm that uses a for loop to look at every word in an alphabetized array of strings. What would be the Big O notation for the complexity of using that for loop to do a search for the word A. A is in the alphabetized dictionary. This may seem like the same answer as c, but it is not.<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**O(1)  if the list is sorted ‘A’ would be the first word**<br><br>
4.	Install Python’s package manager PIP on your machine and bring it to class next time.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.	You should have pip from your installation of Python3.  You can type pip - -version to see if you are dealing with a pip in your python 3 folder or python 2. You may need to type pip3
- - version to see your pip3 install, in which case you will always need to type pip3 when any documentation lists pip.
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**C:\Users\sbing>python --version**<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Python 3.8.5**<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**C:\Users\sbing>pip3 --version**<Br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**pip 20.2.2 for (python 3.8)**<br>

	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.	Now install the requests module using pip. Here is a link talking about how to do it.
	https://www.w3schools.com/python/module_requests.asp

	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**C:\Users\sbing>pip3 install requests**<br>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Successfully installed certifi-2020.6.20 chardet-3.0.4 idna-2.10 requests-2.24.0 urllib3-1.25.10**


5.	Generate an array of 200 random integers instead of the hardcoded arr and see rerun your program. You probably want to remove the print statements for the number of operations.

6.	All of your projects should be named with your initials, the course number, and the homework number. For me, this project would be JL-5410-HW1.1 Do not use my initials. Create a GitHub account and share the code from #5 above with me. My username is jleessd

