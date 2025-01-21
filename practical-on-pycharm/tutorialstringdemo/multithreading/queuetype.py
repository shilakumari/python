import queue


#FIFO Fashion
q = queue.Queue()
q.put(400)
q.put(100)
q.put(500)
q.put(50)
while not q.empty():
    print(q.get(), end=' ')
print()

#LIFO Fashion
lq = queue.LifoQueue()
lq.put(400)
lq.put(100)
lq.put(500)
lq.put(50)
while not lq.empty():
    print(lq.get(), end=' ')
print()

#Priority Based on data
pq = queue.PriorityQueue()
pq.put(400)
pq.put(100)
pq.put(500)
pq.put(50)
while not pq.empty():
    print(pq.get(), end=' ')
print()


#In Tuple, based on numeric value priority goes in PriorityQueue
pq1 = queue.PriorityQueue()
pq1.put((400, "Bharat"))
pq1.put((100, "Bob"))
pq1.put((500, "Surya"))
pq1.put((50, "Gauri"))
while not pq1.empty():
    #print(pq1.get(), end=' ')
    print(pq1.get()[1], end=' ')

print()


