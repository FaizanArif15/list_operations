from random import *

def extend_list(list1,list2):
    list1.extend(list2)
    return list1

def main():
    list1 = [randint(0,100) for i in range(10)]
    list2 = [randint(0,100) for i in range(10)]
    print(extend_list(list1,list2))
main()