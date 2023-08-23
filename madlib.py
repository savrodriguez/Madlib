# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!



print("\033[1mOne October Night\033[1m")

line_1 = input("Adjective:")
line_2 = input("Motion:")
line_3 = input("Reaction:")
line_4 = input("Greeting:")
line_5 = input("A Passage of Time:")
line_6 = input("Noun:")
line_7 = input("Name:")
line_8 = input("Holiday:")

print(f"It was a \033[1m{line_1}\033[1m, late October night.")
print(f"I woke up to the sound of \033[1m{line_2}\033[1m footsteps across the floorboards.")
print(f"I was \033[1m{line_3}\033[1m to say the least. '\033[1m{line_4}\033[1m is someone there?' I yelled.") 
print(f"No reply. \033[1m{line_5}\033[1m later, what sounded like \033[1m{line_6}\033[1m was thrown at my window.")
print(f"\033[1m{line_7}\033[1m came into my room while I was bedridden with fear,") 
print(f"'It's \033[1m{line_8}\033[1m, why are you sleeping?'")


# split up sentences so it didn't appear overwhelming on 1 line of code. hope that's okay 



































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")