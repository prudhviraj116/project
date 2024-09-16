'''x=[10,20,30,40,50,60]
y=x[2::-1]
y.extend(x[-1:-4:-1])
print(y)'''
'''list=[1,2,3]
string="sam"
output=(string+''+str(i)for i in list.split())
print(output)'''
#print('hello world')
'''a="sam"
b=143
print(a+str(b))'''
'''s='mahesh'
p=s[5::-1]
print(p)'''
'''sentence = "my name is prudhvi"
word_count = len(sentence.split())
print("Word count:", word_count)'''

'''sentence = "my name is prudhvi"
character_count = len(sentence)
print("Character count:", character_count)'''
'''sentence = "my name is prudhvi"
converted_sentence = ""

for char in sentence:
    # Check if the character is a lowercase letter
    if 'a' <= char <= 'z':
        # Convert the lowercase letter to uppercase by subtracting 32 from its ASCII value
        converted_char = chr(ord(char) - 32)
    else:
        # Leave non-letter characters unchanged
        converted_char = char
    
    # Append the converted character to the new sentence
    converted_sentence += converted_char

print("Converted sentence:", converted_sentence)'''

'''class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Example usage
my_account = ATM(1000)
print("Current balance:", my_account.check_balance())
my_account.deposit(500)
print("Current balance after deposit:", my_account.check_balance())
my_account.withdraw(200)
print("Current balance after withdrawal:", my_account.check_balance())'''
'''class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print("Area of circle:", circle.area())
print("Perimeter of circle:", circle.perimeter())'''
# Iterate over a range of numbers
#for i in range(5):
    #print(i)  # Output: 0, 1, 2, 3, 4

# Iterate over a range with start and stop
#for i in range(2, 6):
   # print(i)  # Output: 2, 3, 4, 5

# Iterate over a range with start, stop, and step
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9




