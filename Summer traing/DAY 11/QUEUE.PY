class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def display(self):
        print("Queue: ", self.queue)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Dequeued:", q.dequeue())
q.display()
print("Peek:", q.peek())
print("Size:", q.size())
print("Is Empty:", q.is_empty())