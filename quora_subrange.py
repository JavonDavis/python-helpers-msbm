# __author__ = 'javon'
#
#
# #function to determine the size of a segment tree
# def getSegmentTreeSize(N):
#      size = 1
#      while size < N:
#              size = size << 1
#      return size << 1
#
# #Node class
# class SegmentTreeNode:
#
#     def assignLeaf(self, value):
#
#     def merge(self,left, right):
#
#     def getValue(self):
#
#
# nodes = []
#
# def buildTree(lst, start, lo, hi):
#
#     if lo == hi:
#         nodes[start].assignLeaf(lst[lo])
#         return;
#
#     left = 2 *start
#     right = left + 1
#     mid = (lo+hi)/2
#     buildTree(lst,left,lo,mid)
#     buildTree(lst,right,mid+1,hi)
#     nodes[start].merge(nodes[left],nodes[right])




def ranges(upvotes, N, K):
    i = 1
    count = 0
    helper1 = {}
    helper2 = {}

    n = N - K + 1

    if upvotes[0] < upvotes[1]:
        helper1.extend([1, 0])
        helper2.extend([1, 0])
    elif upvotes[0] > upvotes[1]:
        helper1.extend([0, 1])
        helper2.extend([0, 1])
    else:
        helper1.extend([1, 1])
        helper2.extend([1, 1])

    helper_count = 2

    while count != K:
        if upvotes[i] < upvotes[i + 1]:
            increasing = True
            decreasing = False
        elif upvotes[i] > upvotes[i + 1]:
            increasing = False
            decreasing = True
        else:
            increasing = True
            decreasing = True

        both = False
        if increasing and decreasing:
            both = True

        for m in range(0, helper_count):
            if increasing and m % 2 == 0:
                helper1[m] += (1 + helper2[m])
                helper2[m] += 1
                if not both:
                    helper2[m + 1] = 0
            if decreasing and m % 2 != 0:
                helper1[m] += (1 + helper2[m])
                helper2[m] += 1
                if not both:
                    helper2[m - 1] = 0

        if increasing and decreasing:
            helper1.extend([1, 1])
            helper2.extend([1, 1])
        elif increasing:
            helper1.extend([1, 0])
            helper2.extend([1, 0])
        elif decreasing:
            helper1.extend([0, 1])
            helper2.extend([0, 1])
        helper_count += 2
        if helper_count == 2 * (n - 1):
            helper2.pop(0)
            helper2.pop(0)
            print (helper1.pop(0) - helper1.pop(0))
            helper_count -= 2
            count += 1
        i += 1

import Queue


class MutatableQueue(Queue.Queue):
    def change(self, index, new_item):
        with self.mutex:
            self.queue[index] = new_item

    def show(self, index):
        with self.mutex:
            return self.queue[index]


def ranges_with_queue(upvotes, N, K):
    i = 1
    count = 0
    helper1 = MutatableQueue(Queue.Queue)
    helper2 = MutatableQueue(Queue.Queue)

    n = N - K + 1

    if upvotes[0] < upvotes[1]:
        helper1.put(1)
        helper1.put(0)
        helper2.put(1)
        helper2.put(0)
    elif upvotes[0] > upvotes[1]:
        helper1.put(0)
        helper1.put(1)
        helper2.put(0)
        helper2.put(1)
    else:
        helper1.put(1)
        helper1.put(1)
        helper2.put(1)
        helper2.put(1)

    helper_count = 2

    while count != K:
        if upvotes[i] < upvotes[i + 1]:
            increasing = True
            decreasing = False
        elif upvotes[i] > upvotes[i + 1]:
            increasing = False
            decreasing = True
        else:
            increasing = True
            decreasing = True

        both = False
        if increasing and decreasing:
            both = True

        for m in range(0, helper_count):
            if increasing and m % 2 == 0:
                helper1.change(m, helper1.show(m) + 1 + helper2.show(m))
                helper2.change(m, helper2.show(m) +1)
                if not both:
                    helper2.change(m+1, 0)
            if decreasing and m % 2 != 0:
                helper1.change(m, helper1.show(m) + 1 + helper2.show(m))
                helper2.change(m, helper2.show(m) +1)
                if not both:
                    helper2.change(m -1, helper2.show(m) +1)

        if increasing and decreasing:
            helper1.put(1)
            helper1.put(1)
            helper2.put(1)
            helper2.put(1)
        elif increasing:
            helper1.put(1)
            helper1.put(0)
            helper2.put(1)
            helper2.put(0)
        elif decreasing:
            helper1.put(0)
            helper1.put(1)
            helper2.put(0)
            helper2.put(1)
        helper_count += 2
        if helper_count == 2 * (n - 1):
            helper2.get()
            helper2.get()
            print (helper1.get() - helper1.get())
            helper_count -= 2
            count += 1
        i += 1


if __name__ == "__main__":
    N,K = raw_input().split()
    upvotes = raw_input().split()
    upvotes= [int(x) for x in upvotes]
    ranges_with_queue(upvotes,int(N),int(K))