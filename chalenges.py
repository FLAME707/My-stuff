import os
import time
os.system('clear')
numch = int(input('''which project would you like to load?
1: age calculator
2: paragraph generator
3: turf cost calculator
6: zombie counter
>>>Enter project number_'''))
if numch == 6:
    os.system('clear')
    print("welcome to zombie counter...")
    time.sleep(1)
    start = int(input("how many zombies would you like to start with?_"))
    amount = int(input("how many people does a zombie efect each day?_"))
    days = int(input("how many days has it been since day 1?_"))
    print("accourding to my calculations...")
    time.sleep(1)
    ans = start
    for i in range(days):
        ans = (ans*amount)  
    print("there are now", ans, "zombies")
if numch == 1:
    os.system('clear')
    print("welcome to age calculator...")
    time.sleep(1)
    age = int(input("how many years old are you?_"))
    print("accourding to my calculations...")
    time.sleep(1)
    days_alive = age*365
    decades_alive = int(age/10)
    weeks_alive = int(days_alive/7)
    minutes_alive = int(days_alive*1440)
    print("you have been alive", days_alive, "days")
    if decades_alive == 1:
         print("you have been alive", decades_alive, "decade")
    else:
      print("you have been alive", decades_alive, "decades")
    print("you have been alive", weeks_alive, "weeks")
    print("you have been alive", minutes_alive, "minutes")
    print("you have been alive", minutes_alive*60, "seconds")
if numch == 2:
    os.system('clear')
    print("welcome to paragraph generator...")
    time.sleep(1)
    name = input("give me a name_")
    verb = input("give me a verb ending with 'ing'_")
    ad = input("give me a noun_")
    emo = input("give me an emotion_")
    body = input("give me a body part, (eyes, head, etc...)_")
    place = input("give me a place_")
    print(name, "went to the", place, "and saw a man", verb + ", and felt", emo + ",", "so", name, "decided to throw a", ad, "at the mans", body + ".")
if numch == 3:
    os.system('clear')
    print("welcome to turf cost calculator...")
    time.sleep(1)
    length = int(input("what it the length of the field in feet?_"))
    width = int(input("what is the width of your field in feet?_"))
    scost = int(input("what is the cost in dollars per square foot of the turf?_"))

    print("accourding to my calculations...")
    time.sleep(1)
    print("the area of the field is", length*width, "square feet")
    print("the perimiter of the field is", (length+width)*2, "feet")
    print("the total cost of the turf field is", (length*width)*scost, "dollars")
print("<done!>")   
