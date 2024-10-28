import numpy as np
import random
import time
import matplotlib.pyplot as plt

def generatearray(mode, n):
    if mode == 1:
        array = np.arange(n) # 昇順
    elif mode == 2:
        array = np.arange(n-1, -1, -1) # 降順
    else:
        array = random.sample(range(n), n) # ランダム
    return array

def main():
    loop, mode, len = map(int, input().split())
    
    result = []
    for i in range(loop):
        array = generatearray(mode, len)
        start = time.time()
        array.sort()
        end = time.time()
        result.append(end - start)
    
    print(result)

if __name__ == "__main__":
    main()
