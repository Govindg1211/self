import random

# List of random questions
questions = [
    "What's your favorite color?",
    "If you could have any superpower, what would it be?",
    "What's your go-to comfort food?",
    "If you were an animal, which one would you be?",
    "What's the most embarrassing thing you've ever done?",
]

# List of playful responses
responses = [
    "Interesting choice! Did you pick that color because it matches your personality? Just kidding!",
    "Ah, the classic choice! I see you want to be able to fly away from awkward situations!",
    "Comfort food, huh? So, you're saying you eat your feelings? Totally relatable!",
    "An animal, really? I was thinking more along the lines of a couch potato!",
    "Embarrassing moments are just life’s way of keeping us humble. Or maybe it just likes to laugh at us!",
]

def ask_questions():
    print("Let's have some fun! I'll ask you some questions.")
    
    for question in questions:
        input(question + " ")
        # Randomly select a response for each question
        response = random.choice(responses)
        print(response)

if __name__ == "__main__":
    ask_questions()