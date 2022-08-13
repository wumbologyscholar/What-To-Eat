# todo - update the README

# Build a program to decide what P wants to cook for dinner, spit out a random recipe
# from the API and email it, the recipe, and the original link (if available)

# import tkinter as tk
import requests
import smtplib
from ascii_art import title


def check_email():
    email_address = ""
    while email_address == "" or email_address != type(str) or "@" not in email_address:
        email_address = input("\nWhat is your email? (I'll email you the result! :) )")
        print("This is not a valid email address. Please try again.")
        return email_address


def send_email():
    my_email = "one.hundred.days.of.code.14@gmail.com"
    my_password = "sftqimzzilghrpab"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=user_email,
                            msg=f"Subject: Here is your chosen meal!.\n\n{meal_choice}\n\n{meal_recipe}\n\n{meal_link}")
    print("All done, check your email for the results! Bon Apetit!")


print(title)

# ask the user if they'd like a meal recommendation
want_food_rec = input("Welcome to P's Indecision Machine.\n\nHaving"
                      " trouble deciding what to cook for dinner?\nWant"
                      " some help deciding?\nPlease type 'y' or 'n': \n")

if want_food_rec.lower() == "y":
    meal_info = []

    # call the api, and store the resulting meal, its recipe, and original link
    response = requests.get(url="https://www.themealdb.com/api/json/v1/1/random.php")
    response.raise_for_status()

    meal_choice = response.json()["meals"][0]["strMeal"]
    meal_recipe = response.json()["meals"][0]["strInstructions"]
    meal_link = response.json()["meals"][0]["strSource"]

    meal_info.append(meal_choice)
    meal_info.append(meal_recipe)
    meal_info.append(meal_link)


    # ask for the user's email address to send the meal info to
    user_email = check_email()

    send_email()

    # Eventually:
        # make it available as both web app with a tkinter gui (some kind of big picture
            #  logo thing in the middle),in addition to this email CLI verison.
        # use beautifulsoup or some other webscraping thing to go to the strSource
            # and grab the picture of the recipe and include it in the email to the perosn

else:
    pass











# REST OF TKINTER STUFF
# window = tk.Tk()
# greeting = tk.Label(text="This is my first label.")
# greeting.pack()
#
#
# window.mainloop()






#Things to remember:
# for the email to work, the security settings kinda have to be turned off,
# so have the recipient make a quick new fake email just to use for this, and then generate an app password
