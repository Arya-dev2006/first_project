import time
name = "Flowwreak"
current=(time.strftime("%H:%M:%S"))
currenttime=int(time.strftime("%H"))
if currenttime >= 4 and currenttime <12:
    print("Good Mornng Mr."+name,"its",current,"in the clock, you should start working ")
elif currenttime >=12 and currenttime<16:
    print("Good Afternoon Mr."+name,"its",current,"in the clock, you should stop working and take a break")
elif currenttime>=16 and currenttime<19:
    print("Good Evening Mr."+name,"its",current,"in the clock, you should again start working ")
else:
    print("Good Night Mr."+name,"its",current,"in the clock, you can rest now for a while")
    



