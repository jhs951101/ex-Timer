import threading

maxCount = 5
count = 0

def startTimer():
        global count
        
        timer = threading.Timer(0.5, startTimer)
        timer.start()
        
        count += 1
        print(count)
        
        if count >= maxCount:
                timer.cancel()

startTimer()
