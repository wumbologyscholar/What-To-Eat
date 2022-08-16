# Welcome to What To Eat, aka, P's Indecision Machine. 

This is a command-line program, written in Python3 and utilizing TheMealDB API, to allow
groups of any size to each be assigned a randomly chosen recipe/ meal to cook, and then
email each cook their meal selection.

## -----Description-----
First, the group is prompted to enter the number of individuals planning to cook dishes,
then, each cook is asked to input their name and email address, and the program assigns
each cook a random recipe, which is then emailed to them.

## -----Project Inspiration-----
The motivation behind this project was someone in my life who, at times, has trouble
deciding what to eat. She has a real love of cooking, so using principles of OOP learned
from my introductory class in CS, as well as some obtained from my own individual research,
I created this program to help her to decide more easily, and also support her passion for
cooking (especially with friends) even further.

I built this project alone from scratch, but would love to collaborate if someone would like :)


## -----How to Install and Run the Project-----
A relatively recent version of Python3 is needed to run this program (this was built using 3.10),
as well as the packages "requests" and "smtplib" are also needed (in addition to the ascii art
located in the ascii_art.py file). To send the email containing the meal recipe, the from email
address will have to have multiple security settings that need to lowered, and in the case of a
gmail from email address, you will have to turn on 2-Factor Authentication, and then generate an
"App Password" (the option to generate this only appears after turning on 2FA) to use in the program
where it asks for "from_email_pass".

## -----Challenges Faced-----
I initially wrote a working version of this program using linear programming, but realized
that, due to there being multiple attributes about each cook I wanted to be able to access
(name, email, meal, recipe, list of all cooks), as well the lack of being able to use this
program with friends, I pivoted, and decided to incorporate object-oriented principles to
fix these issues. Additionally, I am relatively new to the field of programming, so any
feedback/ constructive criticism is very welcome! :)

## -----To Do-----
Future updates I plan to include are:
-updates to this README
    -include instructions on how to run this program on another person's machine?

-a GUI (possibly using tkinter or a similar python package)

-web scraping using BeautifulSoup to include more relevant info about the recipe and webpage
    in the sent email

-support for not just recipes, but also activities as well (possibly utilizing BoredAPI)

-bug fixes - still working on an issue where the URL to the recipe is not able to be included
    in the email to the user due to certain characters experiencing UTF-8 encoding issues

-more tests to better ensure the format of the input email address is valid (ensure it is a string,
contains "@", etc.)
