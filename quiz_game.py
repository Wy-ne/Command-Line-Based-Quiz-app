import random # this lets us mix up the question order

# Each question is a simple list with 6 items in this order:
# [question text, option A, option B, option C, option D, correct letter]
questions = [
    ["What is the capital of France?", "London", "Paris", "Rome", "Berlin", "B"],
    ["Which planet is known as the Red planet?", "Venus", "Jupiter", "Mars", "Saturn", "C"],
    ["What is 12 * 8?", "88", "92", "104", "96", "D"],
    ["What is the square root of 144?", "10", "12", "14", "16", "B"],
    ["In which year did World War Two end?", "1943", "1944", "1945", "1946", "C"],
    ["Who was the first president of USA?", "Lincoln", "Jefferson", "Washington", "Adams", "C"],
    
]

random.shuffle(questions) # mix up the order of questions

# Get ready to play
score = 0 # The player's points starts at zero
question_number = 1 # Keeps track of which question we are on

print("WELCOME TO THE QUIZ GAME!")
print("Answer the question by typing A, B, C or D")

# Ask each question one by one (This is the loop)
for q in questions: # Loop through the list; each time, q = one question
    # Show the question and the 4 options
    print("Question", question_number, ":", q[0]) # q[0] is the question text
    print(" A:", q[1]) # q[1] is option A
    print(" B:", q[2]) # q[2] is option B
    print(" C:", q[3]) # q[3] is option C
    print(" D:", q[4]) # q[4] is option D

    answer = input("Your answer: ") # Get what the user typed
    answer = answer.strip() # Removes any extra space
    answer = answer.upper() # Turn answers in a capital letter

    # Check the answer is really A, B, C or D
    while answer not in ("A", "B", "C", "D"): 
        answer = input("Please type only A, B, C or D: ")

    # Check if the answer is right (this is the IF Statement)
    if answer == q[5]: # q[5] is the correct letter
        print("Correct!")
        score += 1 # Increment the score by one point
    else:
        print("Wrong! The correct answer was", q[5])

    question_number = question_number + 1 # move to the next question number

    # Final Score and feedback
    total = len(questions) # How many questions they were
    percent = round(score / total * 100) # Convert the score to a percentage

    print("Quiz finished!")
    print("You scored", score, "out of", total, "(", percent, "%)")

    if percent >= 80:
        print("Feedback: Excellent!")
    elif percent >= 50:
        print("Feedback: Good")
    else:
        print("Feedback: Try Again")