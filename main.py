__author__ = 'javon'

import itertools
import math
import heapq

def func():
    options = []
    n = raw_input()
    a,b = n.split()
    a,b = int(a),int(b)
    return (a+b)+(a-b)+(b+a)+(b-a)

evaluations = {"+": lambda num1, num2, ans: (num1 + num2) == ans,
               "-": lambda num1, num2, ans: (num1 - num2) == ans,
               "*": lambda num1, num2, ans: (num1 * num2) == ans,
               "/": lambda num1, num2, ans: (num1 / num2) == ans,
               "%": lambda num1, num2, ans: (num1 % num2) == ans}

def func2():
    options = []

    n = raw_input()
    n = int(n)
    for i in range(0,n):
        j = raw_input()
        options.append(j)

    for option in options:
        a,b,c = option.split()
        a,b,c = int(a),int(b),int(c)
        found = False
        for evaluation in evaluations:
            if evaluations[evaluation](a,b,c):
                found = True
                print "YES"
                break

        if not found:
            print "NO"


def input_num_cases():
    cases = []
    n = int(raw_input())
    for i in range(0,n):
        case = raw_input()
        cases.append(case)
    return cases

def input_cases_until(terminator):
    cases = []
    case = raw_input()
    while case != terminator:
        cases.append(case)
        case = raw_input()
    return cases

def main_func():
    cases = []
    case = raw_input()
    while case != '0':
        cases.append(case)
        case = raw_input()

    for case in cases:
        if int(case) ==1 or int(case) == 2:
            print 0
        else:
            print 4*(int(case) - 2)*3

def alice():
    a = raw_input()
    b = raw_input()
    n,q = a.split()
    n = int(n)
    q = int(q)
    nums = b.split()
    cases = []
    for i in range(0,q):
        j = raw_input()
        cases.append(j)

    for case in cases:
        num1,num2,num3 = case.split()
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        if num1 == 1:
            nums[num2-1] = num3
        if num1 == 2:
            neither = False
            if(num2 != num3):
                increasing = True
                for i in range(num2-1,(num3-1)/2):
                    l = int(nums[i])
                    k = int(nums[i+1])
                    if l>k:
                        neither = True
                        increasing = False
                        break
                    elif l == k:
                        increasing = False
                if not neither:
                    for i in range((num3-1)/2,num3-1):
                        l = int(nums[i])
                        k = int(nums[i+1])
                        if l>k:
                            neither = True
                            increasing = False
                            break
                        elif l == k:
                            increasing = False
            else:
                increasing = True

            if neither:
                print 0
            elif increasing:
                print 2
            else:
                print 1


def thrones():
    string = raw_input()

    found = False
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
    count = 0
    for letter in letters:
        if count != 2:
            if string.count(letter) % 2 != 0:
                count += 1
        else:
            break

    if count != 2:
        found = True

    if not found:
        print("NO")
    else:
        print("YES")

def sum_it_up():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    num_X = int(raw_input())
    array_elements = raw_input().split()
    num_Q = int(raw_input())

    for i in range(0,num_Q):
        raw_input()

    array_elements = map(int,array_elements)

    total = sum(array_elements)
    if num_Q != 0:
        total *= pow(2,num_Q)
    print total%(10**9+7)

def times():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    H = int(raw_input())
    M = int(raw_input())

    numbers = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen','eighteen','nineteen','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine']

    if M == 0:
        print numbers[H-1]+" o' clock"
    elif M == 30:
        print "half past "+str(H)
    elif M > 30:
        index = 60-M-1
        hour = (H+1)%13
        if index == 0:
            print "one minute to "+numbers[hour]
        else:
            print numbers[index]+" minutes to "+numbers[hour]
    else:
        index = 60-M-1
        if index == 0:
            print "one minute past "+numbers[H]
        else:
            print numbers[index]+" minutes past "+numbers[H]


def chess():
    cases = []
    case = raw_input()
    while case != '0 0':
        cases.append(case)
        case = raw_input()

    for case in cases:
        n, m = case.split()
        n, m = int(n), int(m)

def taco():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    days = raw_input()
    days = int(days)
    for day in range(0,days):
        s, m, r, b = raw_input().split()
        s, m, r, b = int(s), int(m), int(r), int(b)
        ingredients = [m,r,b]
        count = 0
        while s > 0:
            ingredients = [ingredient for ingredient in ingredients if ingredient != 0]

            if len(ingredients) >1:
                lowest = min(ingredients)
                index_low = ingredients.index(lowest)
                ingredients[index_low] = lowest - 1

                highest = max(ingredients)
                index_high = ingredients.index(highest)
                ingredients[index_high] = highest - 1

                count += 1
                s -=1
            else:
                break
        print count

def careful_with_cow():
    def run_search(n, point, cows):
        if point[0] == 0:
            can_see = [[point[0], point[1]+1],[point[0]+1,point[1]+1]]
        elif point[0] == 3:
            can_see = [[point[0] - 1, point[1]+1],[point[0],point[1]+1]]
        else:
            can_see = [[point[0] + 1, point[1]+1], [point[0], point[1]+1],[point[0] -1,point[1]+1]]

        if point[1] == n:
            if point[0] == 0:
                return 1
            else:
                return 0
        elif point in cows:
            return 0
        else:
            if len(can_see) == 2:
                return run_search(n, can_see[0], cows) + run_search(n, can_see[1], cows)
            else:
                return run_search(n, can_see[0], cows) + run_search(n, can_see[1], cows) + run_search(n, can_see[2], cows)

    cows = []
    k,n = raw_input().split()
    k,n = int(k),int(n)
    for i in range(0,n):
        cow_positions = raw_input().split()
        cows.append([int(cow_positions[0])-1, int(cow_positions[1])-1])

    start = [0, 0]
    print run_search(k-1, start, cows) % (pow(10,9) +7)

def prediction():
    cases = int(raw_input())
    for i in range(0,cases):
        num_players, num_competitions = raw_input().split()
        num_players, num_competitions = int(num_players),int(num_competitions)
        player_dict = {}
        actual_results = []

        for j in range(0,num_players):
            name = raw_input()
            player_dict[name] = {}

            player = player_dict[name]
            player["predictions"] = []
            player["score"] = 0
            for k in range(0,num_competitions):
                predictions = raw_input().split()
                player["predictions"].append((int(predictions[0]),int(predictions[1])))

        #find score
        l = 0
        max_players = []
        max_score = 0
        unknowns = []
        for m in range(0, num_competitions):
            results = raw_input().split()
            if results[0] != "?":
                S1 = int(results[0])
                S2 = int(results[1])
                for key in player_dict:
                    player = player_dict[key]
                    P1 = player["predictions"][l][0]
                    P2 = player["predictions"][l][1]
                    if P1 == S1 and P2 == S2:
                        player["score"] += 25
                    else:
                        if (P1 > P2 and S1 > S2) or (P1 < P2 and S1 < S2):
                            player["score"] += 10
                        player["score"] += max(0, 5 - abs(S1 - P1))
                        player["score"] += max(0, 5 - abs(S2 - P2))
                        player["score"] += max(0, 5 - abs((P1-P2) - (S1 - S2)))
                    if player["score"] == max_score:
                        max_players += [key]
                    elif player["score"] > max_score:
                        max_players = [key]
                        max_score = player["score"]
            else:
                unknowns += [l]
            l += 1

        official_max_players = []
        official_max_players = max_players[:]
        official_max_score = max_score
        for key in player_dict:
            if key not in official_max_players:
                max_score = official_max_score
                for index in unknowns:
                    player1 = player_dict[key]
                    results = player1["predictions"][index]
                    S1 = int(results[0])
                    S2 = int(results[1])
                    for key1 in player_dict:
                        player = player_dict[key1]
                        P1 = player["predictions"][index][0]
                        P2 = player["predictions"][index][1]
                        if P1 == S1 and P2 == S2:
                            player["score"] += 25
                        else:
                            if (P1 > P2 and S1 > S2) or (P1 < P2 and S1 < S2):
                                player["score"] += 10
                            player["score"] += max(0, 5 - abs(S1 - P1))
                            player["score"] += max(0, 5 - abs(S2 - P2))
                            player["score"] += max(0, 5 - abs((P1-P2) - (S1 - S2)))
                        if player["score"] == max_score:
                            max_players += [key1]
                        elif player["score"] > max_score:
                            max_players = [key1]
                            max_score = player["score"]
                official_max_players += max_players

        official_max_players = list(set(official_max_players))
        official_max_players = sorted(official_max_players)
        for player in official_max_players:
            print player,
        print

def zoom():
    columns = int(raw_input())
    rows = int(raw_input())
    num_chars = int(raw_input())
    chars = {}
    for j in range(0,num_chars):
        name = raw_input()
        chars[name] = []
        for i in range(0,rows):
            entry = raw_input()
            if len(entry) == 0:
                entry = columns * " "
            chars[name].append(entry)

    x = int(raw_input())
    for i in range(0,x):
        word = raw_input()

        for m in range(0,rows):
            line = ""
            for letter in word:
                representation = chars[letter]
                line += representation[m]
            print line


def snakes_and_bunnies():
    n = int(raw_input())
    b_r = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    s_r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    config = []
    bunnies = {}
    snakes = {}
    for i in range(0,n):
        if i % 2 == 0:
            config = list(raw_input()) + config
        else:
            characters = list(raw_input())
            characters.reverse()
            config = characters + config

    config = [0] + config
    for alpha in s_r:
        indexes = [s for s,v in enumerate(config) if v == alpha]
        if len(indexes) > 0:
            snakes[indexes[1]] = indexes[0]

    for digit in b_r:
        indexes = [s for s,v in enumerate(config) if v == digit]
        if len(indexes) > 0:
            bunnies[indexes[0]] = indexes[1]
    num_of_players = int(raw_input())
    players = {}

    for i in range(1,num_of_players+1):
        players[i] = 0

    current_player = 1
    roll1 = raw_input()
    double = False
    snake = False

    while roll1:
        try:
            roll1 = int(roll1)
        except EOFError:
            break
        if not double:
            try:
                roll2 = int(raw_input())
            except EOFError:
                break
            total = roll1 + roll2
            players[current_player] += total

            if snakes.has_key(players[current_player]):
                players[current_player] = snakes[players[current_player]]
                snake = True
            elif bunnies.has_key(players[current_player]):
                players[current_player] = bunnies[players[current_player]]

            while players.values().count(players[current_player]) > 1:
                players[current_player] += 1
                if snake and snakes.has_key(players[current_player]):
                    print "PLAYER "+str(current_player)+" WINS BY EVIL CYCLE!"
                    exit()
                if snakes.has_key(players[current_player]):
                    players[current_player] = snakes[players[current_player]]
                    snake = True
                elif bunnies.has_key(players[current_player]):
                    players[current_player] = bunnies[players[current_player]]

            snake = False

            if players[current_player] >= pow(n,2):
                for i in range(1,num_of_players+1):
                    if players[i] > pow(n,2):
                        print str(pow(n,2))
                    else:
                        print str(players[i]),
                exit()

            if roll1 == roll2:
                double = True
            else:
                current_player += 1
                if current_player > num_of_players:
                    current_player -= num_of_players
        else:

            total = roll1
            players[current_player] += total

            if snakes.has_key(players[current_player]):
                players[current_player] = snakes[players[current_player]]
                snake = True
            elif bunnies.has_key(players[current_player]):
                players[current_player] = bunnies[players[current_player]]

            while players.values().count(players[current_player]) > 1:
                players[current_player] += 1
                if snake and snakes.has_key(players[current_player]):
                    print "PLAYER "+str(current_player)+" WINS BY EVIL CYCLE!"
                    exit()
                if snakes.has_key(players[current_player]):
                    players[current_player] = snakes[players[current_player]]
                    snake = True
                elif bunnies.has_key(players[current_player]):
                    players[current_player] = bunnies[players[current_player]]

            snake = False

            if players[current_player] >= pow(n,2):
                for i in range(1,num_of_players+1):
                    if players[i] > pow(n,2):
                        print str(pow(n,2))
                    else:
                        print str(players[i]),
                exit()

            current_player += 1
            if current_player > num_of_players:
                current_player -= num_of_players
            double = False
        try:
            roll1 = raw_input()
        except EOFError:
            break
    for i in range(1,num_of_players+1):
        print str(players[i]),

from collections import Counter
def dictionary():
    n = int(raw_input())
    for i in range(0,n):
        num_words, num_candidates = raw_input().split()
        num_words,num_candidates = int(num_words),int(num_candidates)
        letters = {}
        for j in range(0,num_words):
            word = raw_input()
            counter = Counter(word)
            for letter in word:
                val = counter[letter]
                if letter in letters:
                    if val > letters[letter]:
                        letters[letter] = val
                else:
                    letters[letter] = val

        for k in range(0,num_candidates):
            candidate = raw_input()
            counter = Counter(candidate)
            valid = True
            perfect = True
            not_valid_count = 0
            for letter in letters:
                real_letter_count = letters[letter]
                candidate_letter_count = counter[letter]
                if real_letter_count > candidate_letter_count:
                    valid = False
                    not_valid_count += (real_letter_count - candidate_letter_count)
                elif real_letter_count < candidate_letter_count:
                    perfect = False

            if valid:
                print "Yes",
                perfect = perfect and (set(letters.keys()) == set(candidate))
                if perfect:
                    print "Yes"
                else:
                    print "No"
            else:
                print "No",
                print str(not_valid_count)


def gremlins():
    t = int(raw_input())
    for i in range(0,t):
        case = raw_input().split()
        num_switches = int(case[0])
        num_primes = int(case[1])+2
        on_list = []
        for j in range(2,num_primes):
            prime = int(case[j])
            multiplier = 1
            while prime * multiplier <= num_switches:
                x = prime * multiplier
                if x in on_list:
                    on_list.remove(x)
                else:
                    on_list.append(x)
                multiplier += 1
        print len(on_list)

def gremlins_better():
    t = int(raw_input())
    for i in range(0,t):
        case = raw_input().split()
        num_switches = int(case[0])
        num_primes = int(case[1])+2
        on_map = {}
        for j in range(2,num_primes):
            prime = int(case[j])
            multiplier = 1
            while prime * multiplier <= num_switches:
                x = prime * multiplier
                if x in on_map:
                    on_map[x] += 1
                else:
                    on_map[x] = 1
                multiplier += 1
        print len([i for i in on_map.values() if i %2 != 0 ])

# Enter your code here. Read input from STDIN. Print output to STDOUT
def f(*args):
    alice_score,bob_score,draw,n = args[0],args[1],args[2],args[3]
    if n >= 4:
        x = n/4
        xx = n%4
        bob_score += x*2
        alice_score += x
        draw += x

        if xx == 1:
            bob_score += 1
        elif xx == 2:
            bob_score += 2
        elif xx == 3:
            bob_score += 2
            alice_score += 1
    else:
        if n == 1:
            bob_score += 1
        elif n == 2:
            bob_score += 2
        elif n == 3:
            bob_score += 2
            alice_score += 1
    return alice_score, bob_score,draw

def mystery():
    cases = raw_input()
    cases = int(cases)
    S, P, R, L, K = "Scissors", "Paper", "Rock", "Lizard", "Spock"
    for i in range(0, cases):
        alice, bob, n = raw_input().split()
        n = int(n)
        alice_score, bob_score,draw = 0,0,0
        if (alice == R or alice == S) and bob == K:
            alice_score,bob_score, draw = f(alice_score,bob_score,draw,n)

        elif alice == K and bob == K:
            if n == 1:
                draw+=1
            elif n == 2:
                draw += 2
            else:
                draw+=2
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-2)
        elif (alice == L and bob == L) or (alice == P and bob == P):
            if n == 1:
                draw+=1
            else:
                draw+=1
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-1)
        elif alice == R and bob == R:
            if n == 1:
                draw+=1
            elif n == 2:
                draw += 1
                alice_score += 1
            elif n == 3:
                draw += 2
                alice_score += 1
            else:
                draw += 2
                alice_score += 1
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-3)
        elif alice == S and bob == S:
            if n == 1:
                draw+=1
            elif n == 2:
                draw += 2
            elif n == 3:
                draw += 3
            else:
                draw += 3
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-3)
        elif (alice == L or alice == S) and bob == R:
            if n == 1:
                bob_score +=1
            elif n == 2:
                bob_score +=1
                alice_score += 1
            elif n == 3:
                bob_score +=1
                alice_score += 1
                draw += 1
            else:
                bob_score +=1
                alice_score += 1
                draw += 1
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-3)
        elif ((alice == K or alice == R) and bob == P) or ((alice == P or alice == K) and bob == L):
            if n == 1:
                bob_score += 1
            else:
                bob_score += 1
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-1)
        elif alice == L and bob == K:
            alice_score = 1
            alice_score *= n
        elif alice == P and bob == K:
            if n == 1:
                alice_score+=1
            elif n == 2:
                alice_score+=1
                draw += 1
            else:
                alice_score = 1
                alice_score *= (n-2)
                draw += 1
                alice_score +=1

        elif alice == L and bob == P:
            if n == 1:
                alice_score += 1
            else:
                alice_score = 1
                alice_score *= (n-1)
                alice_score+=1
        elif alice == S and bob == L:
            if n == 1:
                alice_score += 1
            if n == 2:
                alice_score += 1
                draw += 1
            if n == 3:
                alice_score += 1
                draw += 2
            if n == 4:
                alice_score += 1
                draw += 3
            else:
                alice_score += 1
                draw += 3
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-4)

        elif (alice == R and bob == L) or (alice == S and bob == P):
            if n == 1:
                alice_score += 1
            else:
                alice_score += 1
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-1)

        elif alice == K and bob == S:
            if n == 1:
                alice_score += 1
            elif n == 2:
                alice_score += 1
                draw += 1
            elif n == 3:
                alice_score += 1
                draw += 2
            else:
                alice_score += 1
                draw += 2
                alice_score,bob_score, draw = f(alice_score,bob_score,draw,n-3)

        elif alice == R and bob == S:
            if n == 1:
                alice_score += 1
            else:
                alice_score += 1
                alice_score, bob_score, draw = f(alice_score, bob_score, draw, n-1)

        if alice_score > bob_score:
            print "Alice wins, by winning " + str(alice_score) + " game(s) and tying " + str(draw) + " game(s)"
        elif bob_score > alice_score:
            print "Bob wins, by winning " + str(bob_score) + " game(s) and tying " + str(draw) + " game(s)"
        else:
            print "Alice and Bob tie, each winning " + str(alice_score) + " game(s) and tying " + str(draw) + " game(s)"


if __name__ == "__main__":
    #function to run goes here
    mystery()