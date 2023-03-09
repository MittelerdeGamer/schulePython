from tools import *
from Counter import Counter

if __name__ == '__main__':
    print('PyCharm')
    clicker1 = Counter()
    clicker2 = Counter()

    for i in range(0,5):
        clicker1.count()
        for i in range(0,5):
            clicker2.count()

    print(f"Clicker1: {clicker1.getCount()} \nClicker2: {clicker2.getCount()}")




