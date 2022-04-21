# Neil Marcellini
# 4/20/22
# This is a python while loop that acts as a for loop
class ForAsWhileLoop:
    def __init__(self, stop_condition):
        self.stop_condition = stop_condition

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop_condition(0):
            return "looping"
        else:
            raise StopIteration

loop_forever_input = input("Would you like to loop infinitely (y/n)?\n")
loop_forever = True
if loop_forever_input == 'n':
    print("Looping 10 times")
    loop_forever = False
else:
    print("Looping forever")

loop = input("Enter 'while' or 'for-as-while' to run the infinite loop.\n")
if loop == 'for-as-while':
    print("Running for-as-while loop")
    # Here's a for loop as a while loop
    index = 0
    for_as_while_loop = ForAsWhileLoop(lambda x: loop_forever or index < 10)
    for message in for_as_while_loop:
        print(f"{message} index = {index}")
        index += 1
else:
    print("Running while loop")
    # Here's a basic while loop
    index = 0
    keepLooping = True
    while loop_forever or index < 10:
        print(f"looping index = {index}")
        index += 1
