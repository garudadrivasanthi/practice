# Create a queue using list
queue = []

# Enqueue elements
queue.append('A')
queue.append('B')
queue.append('C')

# View current elements
print("Queue elements:", queue)

# Dequeue (inefficient: O(n) time)
first = queue.pop(1)
print("Dequeued:", first)

# View updated queue
print("Queue after dequeue:", queue)