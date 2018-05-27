'''
A program to read a website and pick out particular words
for comparison
'''

import urllib.request

def web():

    link = "https://www.washingtonpost.com/politics/i-told-everybody-this-is-what-i-was-going-to-do-why-trump-torpedoed-obamas-iran-deal/2018/05/08/a1d39a68-52f0-11e8-9c91-7dab596e8252_story.html?noredirect=on&utm_term=.98bee192b3b3"

    trump = 0
    obama = 0
    
    with urllib.request.urlopen(link) as response:
        myfile = response.read()

    text = link.split()

    
    for i in text:
        if i.upper() == "TRUMP":
            trump += 1
        elif i.upper() == "OBAMA":
            obama += 1

    print("Trump: ", trump)
    print("Obama: ", obama)

web()
