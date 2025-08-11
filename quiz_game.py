#Python Quiz-Game

questions = ("How many elements  are in the periodic table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in earyh's atmospher?",
             "How many Bones in the human body?",
             "Which planet in the solar system is hottest?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbin-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter a (A, B, C, D): ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is correct answer!")
        
    question_num += 1
    
    
print("---------------")
print("     RESULT    ")
print("---------------")

print("Answers: ", end = "")

for answer in answers:
    print(answer, end= " ")
    
print()

print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end= " ")
    
print()

score = int(score / len(questions) * 100)
print(f"Your Score is: {score}%")