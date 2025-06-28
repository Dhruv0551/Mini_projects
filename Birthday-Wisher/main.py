##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib
import random

letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]

letterChoice = random.choice(letter_list)

pdData = pd.read_csv("birthdays.csv")
bdDict = pdData.to_dict(orient="records")

currentMonth = dt.datetime.now().month
currentDay = dt.datetime.now().day

for i in range(0,len(bdDict)):
    if bdDict[i]["month"] == currentMonth and bdDict[i]["day"] == currentDay:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            password = "Your Password"
            my_email = "Test@gmail.com"
            with open(f"letter_templates/{letterChoice}","r") as chosenLetter:
                readLetter = chosenLetter.read()
            updatedLetter = readLetter.replace("[NAME]",bdDict[i]["name"])
            connection.login(my_email,password)
            connection.sendmail(from_addr=my_email,to_addrs=bdDict[i]["email"],msg=f"Subject:Happy Birthday\n\n{updatedLetter}")