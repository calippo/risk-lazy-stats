import random
import seaborn
import matplotlib.pylab as plt

def throw(n):
    return [random.randint(1, 6) for i in xrange(n)]

def run(attack_outcome, defence_outcome):
    import operator
    from collections import Counter
    min_length = min(len(attack_outcome), len(defence_outcome))
    sorted_attack = sorted(attack_outcome, reverse=True)[:min_length]
    sorted_defence = sorted(defence_outcome, reverse=True)[:min_length]
    outcome = map(operator.sub, sorted_attack, sorted_defence)
    attack_wins = [True if o > 0 else False for o in outcome]
    return Counter(attack_wins)

def simulation(attack, defence):
    while(True):
        outcome = run(throw(min(3, attack)), throw(min(3, defence)))
        attack_wins, defence_wins = outcome[True], outcome[False]
        attack -= defence_wins
        defence -= attack_wins
        if attack == 0:
            return 0
        elif defence == 0:
            return 1
        elif attack < 0 or defence < 0:
            raise Exception("hm... this is not supposed to happen")

def single_step(attack, defence):
    n, c = 10000, 0
    for i in xrange(n):
        c += simulation(attack, defence)
    return float(c)/n

if __name__ == "__main__":
    for i in range(1,5):
        print i
        x = range(1, 20)
        y = [single_step(j, i) for j in x]
        plt.plot(x, y, lw = 3, label="defence tanks number:" + str(i))
    plt.ylabel("attacker win probability")
    plt.xlabel("attack tanks number")
    plt.legend(loc = 'center right')
    plt.show()
