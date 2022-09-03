# basic ascii animation in python
import os, time
w, h, count = 11, 11, 0
def func(char, radius):
    a, b = 5, 5
    array_map = [['-' for x in range(w)] for y in range(h)]
    for i in range(h):
        for j in range(w):
            if abs((j-a)**2 + (i-b)**2 - radius**2) < 2.2**2:
                array_map[i][j] = char
    for line in array_map:
        print(' '.join(line))
while True:
    count = 0 if count == 5 else count + 1
    func("$", count) if count % 2 == 0 else func("#", count)
    time.sleep(0.5)
    os.system('cls')
    

