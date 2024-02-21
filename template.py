letter = '''Dear NAME,
 Our company congrats you on your selection
 <|Date|>'''

name = input("Enter your name\n")
date = input("Enter Date\n")

letter = letter.replace("NAME",name)
letter = letter.replace("<|Date|>",date)
print(letter)