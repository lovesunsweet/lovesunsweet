#!/usr/bin/env python3

import sys

def calculator():
    for argv in sys.argv[1:]:
        try:
            num, z = argv.split(':')
            z = int(z)
        except:
            print("Parameter Error")
        m = z * 0.835 - 3500
        if m <= 0:
            tax = 0
        elif m <= 1500:
            tax = m * 0.03
        elif m <= 4500:
            tax = m * 0.1 - 105
        elif m <= 9000:
            tax = m * 0.2 - 555
        elif m <= 35000:
            tax = m * 0.25 - 1005
        elif m <= 55000:
            tax = m * 0.3 - 2755
        elif m <= 80000:
            tax = m * 0.35 - 5505
        else:
            tax = m *0.45 - 13505 
        print("{}:{:.2f}".format(num, z * 0.835 - tax))
    
if __name__ == '__main__':
    calculator()
