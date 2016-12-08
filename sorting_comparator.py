  # Enter your code here. Read input from STDIN. Print output to STDOUT


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return repr((self.name, self.score))

    def comparator(a, b):
        if (a.name < b.name):
            return (b.score - a.score) * 10000 - 1 # 10000 is just some large value to account for -1 (or +1) added
        elif (a.name > b.name):
            return (b.score - a.score) * 10000 + 1
        else:
            return b.score - a.score


n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score


