__author__ = 'javon'


import Queue


class MutableQueue(Queue.Queue):
    def change(self, index, new_item):
        with self.mutex:
            self.queue[index] = new_item

    def show(self, index):
        with self.mutex:
            return self.queue[index]


def ranges_with_queue(upvotes, N, K):
    i = 1
    count = 0
    helper1 = MutableQueue(Queue.Queue)
    helper2 = MutableQueue(Queue.Queue)

    n = N - K + 1

    if len(upvotes) == 1:
        print 0
        return

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
    if len(upvotes) > 2:
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
    else:
        print (helper1.get() - helper1.get())


if __name__ == "__main__":
    N,K = raw_input().split()
    upvotes = raw_input().split()
    upvotes= [int(x) for x in upvotes]
    ranges_with_queue(upvotes,int(N),int(K))