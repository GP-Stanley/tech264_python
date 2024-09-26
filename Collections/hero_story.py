"""Summary

- Write a Python script to write a 'Hero story'
Purpose
- Practice what you've learnt about Python dictionaries
The task

First part

- Define a dictionary called story1. It should have the following keys:
    'start', 'middle' and 'end'
- Print the entire dictionary
- Print the type of your dictionary
- Print only the keys
- Print only the values
- Print the individual values using the keys (individually, lots of print commands)

Second part
Now, let's add a new key:value pair:
    'hero': yourSuperHero

Hints:
    THE MORE CREATIVE THE BETTER
If time
- Improve the program. For example, can you make it a "Choose your own adventure" story?
 """

story1 = {
    "start": "in a faraway land, there was a stubborn, hungry hero named Gina.",
    "middle": "Gina didn't want to go on a quest to Tesco to find the lost treasure of the Lucky Charms.",
    "end": "after many challenges and much moaning, Gina gave into her cravings and found the cereal, returning home as a proud hero."
}

print("The entire dictionary:", story1)                             # print entire dict
print("Type of the dictionary:", type(story1))                      # print data type: <class 'dict'>
print("Keys in the dictionary:", story1.keys())                     # print keys in dict: dict_keys(['start', 'middle', 'end'])
print("Values in the dictionary:", story1.values())                 # print values in dict (the descriptions you wrote)

# The code is printing out parts of a story.
print("On a late Tuesday evening:", story1["start"])                                # story1["start"] retrieves the value associated with the key "start" from the dictionary story1.
print("Faced with a personal challenge of desire and sloth:", story1["middle"])     # you've done the same as above but with the "middle" part.
print("After an hour of debate and:", story1["end"])                                # you've done the same as above but with the "end" part.


# Second part - let's add a new key:value pair: 'hero': yourSuperHero

# Assigning a Value to a Dictionary Key: story1["hero"] = "Gina"
# This line adds a new key-value pair to the story1 dictionary.
# The key is "hero" and the value is "Gina".

story1["hero"] = "Gina"
print(f"Some would argue, {story1["hero"]}, is the hero of the story - normal people wouldn't.")


print("The entire dictionary:", story1)



