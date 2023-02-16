import timeit
import matplotlib.pyplot as plt

mem = {}
def func(n):
    if n in mem:
        return mem[n] 
    if n == 0 or n == 1:
        return n
    mem[n] = func(n-1) + func(n-2)
    return mem[n]


def recfib(n):
    if n == 0 or n == 1:
        return n
    else:
        return recfib(n-1) + recfib(n-2)

def main():
    n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    timelist = []
    rectimelist = []
    for i in n:
        time = timeit.timeit(lambda: func(i), number=1) 
        timelist.append(time)
        rectime = timeit.timeit(lambda: recfib(i), number=1)
        rectimelist.append(rectime)
    
    plt.plot(n, timelist, label = "Dynamic Programming")
    plt.plot(n, rectimelist, label = "Recursion")
    plt.xlabel('n')
    plt.ylabel('Time')
    plt.title('Time taken to find fib n')
    plt.legend()
    plt.show()
            
        
    print(timelist)
    print(rectimelist)

if __name__ == "__main__":
    main()
'''
time = timeit.timeit(lambda: fib(i), number=1) 
timelist.append(time)
rectime = timeit.timeit(lambda: recfib(i), number=1)
rectimelist.append(rectime)
''' 