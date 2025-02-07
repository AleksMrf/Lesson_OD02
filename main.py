class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # Добавляем элемент в верхушку стека
        self.stack.append(item)

    def pop(self):
        # Удаляем и возвращаем верхний элемент стека
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None  # Или можно выбросить исключение

    def peek(self):
        # Возвращаем верхний элемент стека без удаления
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self.stack) == 0

    def size(self):
        # Возвращаем размер стека
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.size())