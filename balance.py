#!/bin/python
from datetime import date
import sys

def getDate():
    td =  date.today()
    return "%s-%s-%s" % (td.year, td.month, td.day)


def add(cost, apply):
    out = "%s,\t %s,\t %s" % ( getDate(), cost, apply)
    f = open( "balance.txt", "w+")
    f.write(out)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) > 3:
        if sys.argv[1] == "add":
            cost = sys.argv[2]
            apply = sys.argv[3]
            add(cost, apply)
        if sys.argv[2] == "summary":
            summary()

    else:
        print "usage: python balance.py add cost apply"
