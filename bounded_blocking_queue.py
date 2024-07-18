import threading

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def put(self, item):
        with self.lock:
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            self.queue.append(item)
            self.not_empty.notify()

    def multiput(self, items):
        with self.lock:
            for item in items:
                while len(self.queue) == self.capacity:
                    self.not_full.wait()
                self.queue.append(item)
                self.not_empty.notify()

    def take(self):
        with self.lock:
            while not self.queue:
                self.not_empty.wait()
            item = self.queue.pop(0)
            self.not_full.notify()
            return item

    def size(self):
        with self.lock:
            return len(self.queue)
