import sys


def myfunction(mystring):
    print(mystring)


if __name__ == '__main__':
     args=sys.argv
     globals()[args[1]](*args[2:])
