# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
X = map(int, raw_input().strip().split())

sumX = sum(X)
countX = len(X)
mid = (countX-1) / 2

mean = 0
median = 0
mode = 0

X.sort()

# mean
mean = float(sumX) / countX

# median
if countX % 2 == 0:
    median = (X[mid] + X[mid+1]) / 2.0
else:
    median = X[mid]

# mode
frequency = {}
max_frequency = X[0]

for i in X:
    if i not in frequency:
        frequency[i] = 0
    frequency[i] += 1
    if max_frequency in frequency and frequency[i] > frequency[max_frequency]:
        max_frequency = i

mode = max_frequency

print mean
print median
print mode