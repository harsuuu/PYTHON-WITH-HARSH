letter = '''Dear <|name|>
          you are selected for this job
          <|date|>'''
name = input("Enter name :")
date = input("Enter date :")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)