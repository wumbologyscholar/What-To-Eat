# todo - update the README

# Build a program to decide what a group wants to do at that
# moment (ex. Watch tv, study, etc), where they want to eat, etc…,

# import tkinter as tk
import requests
import smtplib

# Steps:
# ask x #of people what they want to eat
num_of_people = input("Welcome to the Indecision Machine.\nHaving"
                      " trouble deciding what to eat for dinner?\nWant"
                      " some help deciding?\nEnter the number of people dining tonight: ")



# call the api that many times, and then get those 4 results back and store them,
response = requests.get(url="http://www.boredapi.com/api/activity/")
response.raise_for_status()

activity = response.json()["activity"]


# then tally the votes from the 4 people and whatever gets more votes is the winner
# (but also include a setting to just pick a random choice from the 4 in the case that
    #  the group still can't decide). Ask for a gmail address (eventually add in support
#  for other email services)

user_email = ""
user_password = ""
while user_email == "":
    user_email = input("\nWhat is your email? (I'll email you the result! :) )\nNote: Only Gmail addresses are accepted: ")
    if user_email != type(str) or "@" not in user_email:
        print("This is not a valid email address. Please try again.")

while user_password == "":
    user_password = input(
        "\nWhat is your password?\nNote: For Gmail addresses, you will have to generate an app password: ")
    if user_password != type(str):
        print("This is not a valid email address. Please try again.")


#  Then email the choice to that email with some kind of message and possibly a picture
    #  if possible.
my_email = "one.hundred.days.of.code.14@gmail.com"
my_password = "sftqimzzilghrpab"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=user_email, msg=f"Subject: Here is your chosen activity!.\n\n{activity}")


#  Eventually make it available as both web app with a tkinter gui (some kind of big picture
    #  logo thing in the middle),in addition to this email CLI verison.











# REST OF TKINTER STUFF
# window = tk.Tk()
# greeting = tk.Label(text="This is my first label.")
# greeting.pack()
#
#
# window.mainloop()






#Things to remember:
# for the email to work, the security settings kinda have to be turned off, so have the recipient make a quick new fake email just to use for this, and then generate an app password