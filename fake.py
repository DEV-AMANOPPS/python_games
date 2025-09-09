import random

subjects=[
    "The cat", "A dog", "The bird", "A fish", "The elephant", "automate",
    "The robot", "The programmer", "The teacher", "The student"
]
actions = [
    "jumps over", "runs around", "flies above", "swims in", "dances with",
    "writes code for", "teaches", "learns from", "builds", "creates"
]

places = [
    "the fence", "the park", "the sky", "the ocean", "the dance floor",
    "the computer", "the classroom", "the library", "the city", "the world"
]

# start the headline generation loop here
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS:{subject} {action} {place}!"
    print("\n" + headline)
    # end the headline generation loop here
    user_input = input("\nWould you like to generate another headline? (y/n): ").strip().lower()
    if user_input == 'n':
        print(" thank you for generating the headlines.Goodbye!")
        break