class MyTime:

    def __init__(self,h,m,s):
        totalsecs = h*3600 + m*60 + s
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return ("The time is {0}:{1}:{2}"
              .format(self.hours,self.minutes,self.seconds))

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def to_seconds(self):
        """Returns seconds represented by me"""
        return (self.hours * 3600 + self.minutes * 60 + self.seconds)

    def after(self, time2):
        """Same as gt"""
        return self.to_seconds() > time2.to_seconds()

    def between(self,t1,t2):
        """Returns true if I am between t1 and t2, assuming t1 < t2"""
        return t1.to_seconds <= self.to_seconds() < t2.to_seconds

    def increment(self,seconds):
        return MyTime(0,0,self.to_seconds() + seconds)

tim1 = MyTime(11,59,30)

def add_time(t1,t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0,0,secs)


def increment(t,seconds):
    t.seconds += seconds

    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes += 60

    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1

current_time = MyTime(9,14,30)

from unit_test import test

