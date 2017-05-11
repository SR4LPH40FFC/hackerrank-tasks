# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(raw_input())
N = map(int, raw_input().strip().split())
W = map(int, raw_input().strip().split())

weighted_sum = 0
for i in range(len(N)):
    weighted_sum += N[i] * W[i]

weighted_mean = weighted_sum / float(sum(W))

print weighted_mean


# 5
# 10 20 30 40 50
# 2 3 4 5 6
#
# (20+60+120+200+300) / (2+3+4+5+6) = 700 / 20 = 35.0