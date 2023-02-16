import timeit
mem = {}
def func(n):
    if n in mem:
        return mem[n] 
    if n == 0 or n == 1:
        return n
    mem[n] = func(n-1) + func(n-2)
    return mem[n]

def main():
    n = 35
    time = timeit.timeit(lambda: func(n), number=1)
    print(f"Time taken to find fib {n} is {time} seconds and the number is {func(n)}")


if __name__ == "__main__":
    main()
