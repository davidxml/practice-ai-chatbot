# writing the logics for chatbot greeting
""" Chatbot meant to greet, would need
- Name
- Time of the day
"""

# step 1 --> Hey there, what's the name?
print("Hey there, what's the name?")

# step 2 --> accepts user's name
name = input("name: ")
print(name)

# step 3 --> Tell python to say "Hi" with your name
print("Hi " + name)

# step 4 --> Get the time of the 
time_of_the_day = input("What time of the day is it?: ")

# step 5 --> Greet with all data provided 
print(f"Yeah! Hey {name}, Good {time_of_the_day}. It's nice to have you in here.")