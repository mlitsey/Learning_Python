# 01. write a class that prints the word for the number you provide
#     as a property between 1 and 20
#
# 02. for example, if you assign a property value of 15, a method
#     in the class should write the word 'fifteen'

# as a bonus, try to do it in the shortest and most effective
# manner possible...

from sys import exit

class __number__():
    def to_word(self, in_num):
        words = ('one', 'two', 'three', 'four', 'five', 'six',
                 'seven', 'eight', 'nine', 'ten', 'eleven',
                 'twelve', 'thirteen', 'fourteen', 'fifteen', 
                 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                 'twenty')
        if in_num < 1 or in_num > 21:
            print(f"{in_num}")
        else:
            print(f"{in_num} is {words[in_num-1]}")

def main():
    toword = __number__()
    while True:
        print("Enter a number. 0 to exit.")
        num = int(input("Number: "))
        if num == 0:
            break
        elif num == '' or num == None:
            continue
        else:
            toword.to_word(int(num))
    
    exit

main()