__author__ = 'javon'


"""
Recursive power implementation O(log n)
"""


def pow_recur(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    elif n % 2 == 0:
        return pow_recur(a, n / 2) * pow_recur(a, n / 2)
    else:
        return a * pow_recur(a, (n - 1) / 2) * pow_recur(a, (n - 1) / 2)


""" power test pow won"""


# if __name__ == "__main__":
#     import timeit
#     print timeit.timeit("pow_recur(1000000,1000000)",setup="from __main__ import pow_recur",number =1)
#     print timeit.timeit("pow(1000000,1000000)",number =1)

""" Stack """


class Stack:
    # global variables here
    stack_count = 0

    def __init__(self, elements):
        Stack.stack_count += 1
        self.items = []
        for el in elements:
            self.push(el)

    def push(self, el):
        self.items.insert(0, el)

    def pop(self):
        return self.items.pop(0)

    def top(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def print_stack(self):
        for item in self.items:
            print(item)


""" stack testing"""


# if __name__ == "__main__":
#     stack1 = Stack([0, 1, 2, 3])
#     stack2 = Stack([4, 5, 6, 7])
#
#     stack1.print_stack()
#     print stack1.pop()
#     stack1.print_stack()


class Queue:
    # global variables here
    queue_count = 0

    def __init__(self, elements):
        Queue.queue_count += 1
        self.items = []
        for el in elements:
            self.enqueue(el)

    def enqueue(self, el):
        self.items.append(el)

    def dequeue(self):
        return self.items.pop(0)

    def top(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def print_queue(self):
        for item in self.items:
            print(item)


# if __name__ == "__main__":
#     queue1 = Queue([0, 1, 2, 3])
#     queue2 = Queue([4, 5, 6, 7])
#
#     print queue2.size()
#     queue2.dequeue()
#     print queue2.size()


class Heap:
    def __init__(self, elements):
        i = len(elements) / 2
        self.currentSize = len(elements)
        self.items = [0] + elements[:]
        while i > 0:
            self.move_down(i)
            i -= 1

    def insert(self, el):
        self.items.append(el)
        self.currentSize += 1
        i = self.currentSize
        while i / 2 > 0:
            if self.items[i] < self.items[i / 2]:
                tmp = self.items[i / 2]
                self.items[i / 2] = self.items[i]
                self.items[i] = tmp
            i /= 2

    def move_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.min_child(i)
            if self.items[i] > self.items[mc]:
                tmp = self.items[i]
                self.items[i] = self.items[mc]
                self.items[mc] = tmp
            i = mc

    def delete_min(self):
        retval = self.items[1]
        self.items[1] = self.items[self.currentSize]
        self.currentSize -= 1
        self.items.pop()
        self.move_down(1)
        return retval

    def min_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.items[i * 2] < self.items[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def print_heap(self):
        for item in self.items[1:]:
            print(item),

    def size(self):
        return self.currentSize


import heapq

""" Priority Queue implented using pythons built in heapq
module but can also use heap class above to implement a heap queue"""


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

        # if __name__ == "__main__":
        #     priority_queue = PriorityQueue()
        #
        #     q = PriorityQueue()
        #     q.push("hello", 1)
        #     q.push("jnfds", 3)
        #     q.push("jnewffds", 2)
        #
        #     print q.pop()
        #     print q.pop()
        #     print q.pop()

        # import unittest
        #
        # class Test(unittest.TestCase):
        #
        #     def test(self):
        #         self.assertEqual(f(3), 4)


""" RBTree and RBNode gotten from the internet works pretty well to me"""


class RBNode(object):
    """
    A node in a red black tree. See Cormen, Leiserson, Rivest, Stein 2nd edition pg 273.
    """

    def __init__(self, key):
        "Construct."
        self._key = key
        self._red = False
        self._left = None
        self._right = None
        self._p = None

    key = property(fget=lambda self: self._key, doc="The node's key")
    red = property(fget=lambda self: self._red, doc="Is the node red?")
    left = property(fget=lambda self: self._left, doc="The node's left child")
    right = property(fget=lambda self: self._right, doc="The node's right child")
    p = property(fget=lambda self: self._p, doc="The node's parent")

    def __str__(self):
        "String representation."
        return str(self.key)

    def __repr__(self):
        "String representation."
        return str(self.key)


class RBTree(object):
    """
    A red black tree. See Cormen, Leiserson, Rivest, Stein 2nd edition pg 273.
    """

    def __init__(self, create_node=RBNode, elements=None):
        "Construct."

        self._nil = create_node(key=None)
        "Our nil node, used for all leaves."

        self._root = self.nil
        "The root of the tree."

        self._create_node = create_node
        "A callable that creates a node."
        if elements != None:
            for el in elements:
                self.insert_key(el)

    root = property(fget=lambda self: self._root, doc="The tree's root node")
    nil = property(fget=lambda self: self._nil, doc="The tree's nil node")

    def search(self, key, x=None):
        """
        Search the subtree rooted at x (or the root if not given) iteratively for the key.
        
        @return: self.nil if it cannot find it.
        """
        if None == x:
            x = self.root
        while x != self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, x=None):
        """
        @return: The minimum value in the subtree rooted at x.
        """
        if None == x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x=None):
        """
        @return: The maximum value in the subtree rooted at x.
        """
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    def insert_key(self, key):
        "Insert the key into the tree."
        self.insert_node(self._create_node(key=key))

    def insert_node(self, z):
        "Insert node z into the tree."
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z._p = y
        if y == self.nil:
            self._root = z
        elif z.key < y.key:
            y._left = z
        else:
            y._right = z
        z._left = self.nil
        z._right = self.nil
        z._red = True
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        "Restore red-black properties after insert."
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self._left_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False

    def _left_rotate(self, x):
        "Left rotate x."
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p._left = y
        else:
            x.p._right = y
        y._left = x
        x._p = y

    def _right_rotate(self, y):
        "Left rotate y."
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._p = y
        x._p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p._right = x
        else:
            y.p._left = x
        x._right = y
        y._p = x

    def check_invariants(self):
        "@return: True iff satisfies all criteria to be red-black tree."

        def is_red_black_node(node):
            "@return: num_black"
            # check has _left and _right or neither
            if (node.left and not node.right) or (node.right and not node.left):
                return 0, False

            # check leaves are black
            if not node.left and not node.right and node.red:
                return 0, False

            # if node is red, check children are black
            if node.red and node.left and node.right:
                if node.left.red or node.right.red:
                    return 0, False

            # descend tree and check black counts are balanced
            if node.left and node.right:

                # check children's parents are correct
                if self.nil != node.left and node != node.left.p:
                    return 0, False
                if self.nil != node.right and node != node.right.p:
                    return 0, False

                # check children are ok
                left_counts, left_ok = is_red_black_node(node.left)
                if not left_ok:
                    return 0, False
                right_counts, right_ok = is_red_black_node(node.right)
                if not right_ok:
                    return 0, False

                # check children's counts are ok
                if left_counts != right_counts:
                    return 0, False
                return left_counts, True
            else:
                return 0, True

        num_black, is_ok = is_red_black_node(self.root)
        return is_ok and not self.root._red


# if __name__ == "__main__":
#     x = RBTree(elements = [5,3,20,7,11,21, 13, 2, 3])
#     print x.search(133)


"""Dynamic programing examples below"""

"""
Problem: given n, find the number of different ways to write n as the sum of 1, 3, 4
Example: for n = 5, the answer is 6
1-dimensional DP

5
= 1+1+1+1+1
= 1+1+3 = 1+3+1 = 3+1+1 = 1+4
= 4+1
"""


def careful_with_poison_stupid_implementation():
    def run_search(n, point, poisons):
        if point[0] == n:
            can_see = [[point[0], point[1] + 1]]
        elif point[1] == n:
            can_see = [[point[0] + 1, point[1]]]
        else:
            can_see = [[point[0] + 1, point[1]], [point[0], point[1] + 1]]

        if point == [n, n]:
            return 1
        elif point in poisons:
            return 0
        else:
            if len(can_see) == 1:
                if can_see[0] in poisons:
                    return 0
                return run_search(n, can_see[0], poisons)
            elif can_see[0] in poisons:
                return run_search(n, can_see[1], poisons)
            elif can_see[1] in poisons:
                return run_search(n, can_see[0], poisons)
            else:
                return run_search(n, can_see[0], poisons) + run_search(n, can_see[1], poisons)

    options = []
    n = int(raw_input())
    while n != 0:
        poison = raw_input()
        poison = poison.split()
        poison[0], poison[1] = int(poison[0]), int(poison[1])
        all_poisons = [[x, y] for x in range(poison[0], poison[0] + 3) for y in range(poison[1], poison[1] + 3)]
        options.append((n, all_poisons))
        n = int(raw_input())

    for option in options:
        n = option[0]
        poisons = option[1]
        start = [0, 0]
        print run_search(n, start, poisons)

from collections import namedtuple
from pprint import pprint as pp


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        #pp(neighbours)

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        #s, u = deque(), dest
        while previous[u]:
            s.pushleft(u)
            u = previous[u]
        s.pushleft(u)
        return s


def careful_with_poison():
    def L(p,q):
        if [p,q] in poisons:
            return 0
        elif p == 0 or q == 0:
            return 1
        else:
            if memory.has_key(str([p,q])):
                return memory[str([p,q])]
            else:
                x = L(p-1,q)
                memory[str([p-1,q])] =x
                y = L(p,q-1)
                memory[str([p,q-1])] =y
                return x + y
    options = []
    n = int(raw_input())
    while n != 0:
        poison = raw_input()
        poison = poison.split()
        poison[0], poison[1] = int(poison[0]), int(poison[1])
        all_poisons = [[x, y] for x in range(poison[0], poison[0] + 3) for y in range(poison[1], poison[1] + 3)]
        options.append((n, all_poisons))
        n = int(raw_input())

    for option in options:
        n = option[0]
        poisons= option[1]
        memory = {}
        print L(n, n) % (pow(10,9) +7)


def number_of_paths_to_point(start,end,through = []):
    m = (pow(10,9)+7)

    count = 1

    for point in through:
        p = point[0] - start[0]
        q = point[1] - start[1]

        tot = p + q
        num2 = tot
        for i in range(1,tot):
            num2 *= (tot-i)
            num2%=m
            # if i+1 == q:
            #     break
        for u in range(0,p):
            num2 /= (p-u)
            num2%=m
        for u in range(0,q):
            num2 /= (q-u)
            num2%=m
        start =point
        count*=(num2%m)

    x = end[0] - start[0]
    y = end[1] - start[1]
    n = x+y
    num = n
    for i in range(1,n):
        num *= (n-i)
        num%=m
        # if i+1 == y:
        #     break
    for u in range(0,x):
        num /= (x-u)
        num%=m
    for u in range(0,y):
        num /= (y-u)
        num%=m
    count *= (num%m)
    return count

import itertools

def careful_with_poison_correct():
    options = []
    n = int(raw_input())
    while n != 0:
        poison = raw_input()
        poison = poison.split()
        poison[0], poison[1] = int(poison[0]), int(poison[1])
        all_poisons = list(([x, y] for x in range(poison[0], poison[0] + 3) for y in range(poison[1], poison[1] + 3)))
        options.append((n, all_poisons))
        n = int(raw_input())

    for option in options:
        n = option[0]
        end = [n,n]
        poisons= option[1]
        start = [0,0]
        total_paths_through_poison = 0
        count = 0
        for i in range(1,10):
            combinations = list((list(x) for x in itertools.combinations(poisons, i)))
            for combination in combinations:
                to_point = number_of_paths_to_point(start,end,combination)
                total_paths_through_poison += (pow(-1,i-1) *to_point)
                count += 1
        total = number_of_paths_to_point(start,end)
        print total - total_paths_through_poison



def popmin(pqueue):
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest

def dijkstra(graph, start):
    pqueue = {}
    dist = {}
    pred = {}

    for v in graph:
        dist[v] = 1000
        pred[v] = -1
        dist[start] = 0
        for v in graph:
            pqueue[v] = dist[v]




def num_ways(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return num_ways(n - 1) + num_ways(n - 3) + num_ways(n - 4)


def careful_with_cow():
    def run_search(n, point, cows):
        if point[0] == 0:
            can_see = [[point[0]+1, point[1]],[point[0]+1,point[1]+1]]
        elif point[0] == 1:
            can_see = [[point[0] - 1, point[1]],[point[0]+1,point[1]+1]]
        else:
            can_see = [[point[0] + 1, point[1]], [point[0]+1, point[1]],[point[0] -1,point[1]+1]]

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
    for i in range(0,n):
        cow_positions = raw_input().split()
        cows.append((int(cow_positions[0])-1, int(cow_positions[1])-1))

    start = [0, 0]
    print run_search(k, start, cows)

def ranges(*nums):
    print nums[3]

if __name__ == "__main__":
    ranges(1,2,3,4,5)



# def main_func():
#     terminator = "0 0"
#     cases = input_num_cases()
#     cases = input_cases_until(terminator)
#     for case in cases:
