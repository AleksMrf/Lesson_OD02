class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Добавляем элемент в конец очереди
        self.queue.append(item)

    def dequeue(self):
        # Удаляем и возвращаем первый элемент очереди
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None  # Или можно выбросить исключение

    def front(self):
        # Возвращаем первый элемент очереди без удаления
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return len(self.queue) == 0

    def size(self):
        # Возвращаем размер очереди
        return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.front())
print(queue.size())