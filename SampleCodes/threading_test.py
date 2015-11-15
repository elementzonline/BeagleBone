__author__ = 'dhanish'

import threading
import time

class mythread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print 'starting ', self.name
        printtime(self.name,self.counter,2)
        print 'exciting ' , self.name

def printtime(threadName,counter,delay):
    count = 0
    while count < counter:
        time.sleep(delay)
        print threadName , time.ctime(time.time())
        count += 1


thread1 = mythread(1,"Thread-1-",3)
thread2 = mythread(1,"Thread-2-",1)

thread1.start()
thread2.start()

thread1.join()
print 'thread1 joined'
thread2.join()
print 'thread2 joined'

print 'Main code excited'
