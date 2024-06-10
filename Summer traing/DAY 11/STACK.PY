# The functions associated with stack are:

# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

# Python program to
# demonstrate stack implementation
# using list

# stack = []

# # append() function to push
# # element in the stack
# stack.append(input())
# stack.append(input())
# stack.append(input())

# print('Initial stack')
# print(stack)

# # pop() function to pop
# # element from stack in
# # LIFO order
# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


# print('\nStack after elements are popped:')
# print("empty:" ,stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty






#example 2:


def create_stack():
    stack = []
    return stack
def check_empty(stack):
    return len(stack) == 0
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))