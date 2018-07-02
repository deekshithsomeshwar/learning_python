import webbrowser
import time #delay the loop
import random


while True:
    sites = random.choice(['google.com','codeacademy.com','hackerrank.com'])
    visit = "http://{}" .format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5,20)
    time.sleep(seconds)
