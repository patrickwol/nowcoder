import sys
import queue


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q=queue.PriorityQueue()
    q.put((-3,3))
    q.put((-2,2))
    q.put((-5,5))
    print(q.queue)
    r=map(lambda x:x[1],q.queue)
    print(list(r))

