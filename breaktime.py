import webbrowser
import time
import datetime

print "This program started on :" +time.ctime()

total_breaks=3
break_count=0
while(break_count<total_breaks):
    time.sleep(30)
    print "Break Reminder for every 60 seconds:" +time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=9cHXA6l4e4Q")
    break_count=break_count+1;
    
    
