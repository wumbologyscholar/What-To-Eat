# todo - update the README
# todo - include docstrings for all classes and methods except init

# Build a program to decide what P (+ any number of extra friends) wants to cook for dinner, spit out a random recipe
# from the API and email it, the recipe, and the original link (if available)

import requests
import smtplib
from ascii_art import title


class Cook:
    def __init__(self, cook_name, cook_email, meal, recipe):
        self._cook_name = cook_name
        self._meal = meal
        self._recipe = recipe
        self._cook_email = cook_email
        self._catalog_of_cooks = {}  # keys = names, values = objects

    def get_cook_name(self):
        return self._cook_name

    def get_meal(self):
        return self._meal

    def get_recipe(self):
        return self._recipe

    def get_email(self):
        return self._cook_email

    def add_cook_to_catalog(self, name_of_cook):
        self._catalog_of_cooks[name_of_cook] = self

    def delete_cook_from_catalog(self, cook_object):
        del self._catalog_of_cooks[cook_object.get_name()]

    def send_meal_email(self, user_email):
        from_email = "p.indecision.machine@gmail.com"
        from_email_pass = "cuxnzqpcjcflnyur"
        email_message = f"Subject: Here is your chosen meal!\n{self._meal}\n{self._recipe}"  # want to also send {meal_link}, but doesn't work

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=from_email_pass)
            connection.sendmail(from_addr=from_email, to_addrs=user_email,
                                msg=email_message)
        print("All done, check your email for the results! Bon Apetit!")


def choose_random_meal():
    # randomly choose a meal for the cook
    response = requests.get(url="https://www.themealdb.com/api/json/v1/1/random.php")
    response.raise_for_status()

    meal_choice = response.json()["meals"][0]["strMeal"]
    meal_recipe = response.json()["meals"][0]["strInstructions"]
    meal_link = response.json()["meals"][0]["strSource"]  # todo - fix bug - problem with utf encoding of link

    meal_info = [meal_choice, meal_recipe] # eventually find out how to make meal_link work, UTF-8 encoding problems

    return meal_info


print(title)

# ask the user if they'd like a meal recommendation
want_food_rec = input("Welcome to P's Indecision Machine.\n\nHaving"
                      " trouble deciding what to cook for dinner?\nWhether"
                      " alone or with friends, I can help!\nWant"
                      " some help deciding?\nPlease type 'y' or 'n': \n")

if want_food_rec.lower() == "y":

    # ask how many people will be cooking today, make an object for each
    # one of them (ask for name and email)
    num_cooks = int(input("How many cooks do we have with us today?\nI'll"
                          " provide a different recipe for each of you.\n"))

    for each_cook in range(num_cooks):
        # ask name
        current_cook_name = input("What is this cook's name?:\n")
        # ask email
        current_cook_email = input("What is this cook's email address? (I'll email you the result!):\n")

        # check to make sure email is correct format
        while "@" not in current_cook_email: #todo - eventually beef up the validation of email addresses
            print("This is not a valid email address. Please try again.")
            current_cook_email = input("What is this cook's email address?:\n")

        # choose a random meal for this cook
        choose_random_meal()
        # initialize Cook object with name and email
        cook = Cook(current_cook_name, current_cook_email, choose_random_meal()[0], choose_random_meal()[1])
        # add cook to the catalog of cooks
        cook.add_cook_to_catalog(current_cook_name)
        # send email with meal
        cook.send_meal_email(current_cook_email)

else:
    pass






# Eventually:
    # make it available as both web app with a tkinter gui (some kind of big picture
        #  logo thing in the middle),in addition to this email CLI verison.
    # use beautifulsoup or some other webscraping thing to go to the strSource
        # and grab the picture of the recipe and include it in the email to the perosn




# REST OF TKINTER STUFF
# window = tk.Tk()
# greeting = tk.Label(text="This is my first label.")
# greeting.pack()
#
#
# window.mainloop()
