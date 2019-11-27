import datetime
import time

#welcoming the user
name = raw_input("What is your name? ")
print "Hello, " + name, "Time to play hangman!"
print "
"

print("Hello World")
now = datetime.datetime.now()
print("Current date and time is ")
print(now.strftime("%A, %d-%m-%Y : %H:%M"))

for i in range(5):
  print(i)
