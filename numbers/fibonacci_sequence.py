"""
Outputs the Fibonacci Sequence up to a given limit
"""

def fibo(up_to):
    a = 0
    b = 1
    for __ in range(up_to):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    import sys
    import time
    start_time = time.clock() #change to .time() for linux
    ans = fibo(int(sys.argv[1]))
    print(ans)
    print("--- %d digits ---" % len(str(ans)))
    print("--- %s seconds ---" % round(time.clock() - start_time, 2)) #change to .time() for linux