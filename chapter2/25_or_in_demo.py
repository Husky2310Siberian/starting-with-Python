from random import choice

choice = 'q'

if choice == 'q' or choice == 'Q':
    print("OK")
else:
    print("ERROR")

# more efficient
if choice in ('q', 'Q'):
    print("OK")
else:
    print("ERROR")