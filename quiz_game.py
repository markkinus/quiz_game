import random

# questions and options
questions = [
    {
    "question": "What is 15 + 10?",
    "options" : ["A. 25", "B. 23", "C. 34", "D. 12"], 
    "answer": "A"
}, 
{
    "question": "What is 13 + 10?",
    "options" : ["A. 25", "B. 23", "C. 34", "D. 12"],
    "answer": "B"
},
{
    "question": "What is 24 + 10?",
    "options" : ["A. 25", "B. 23", "C. 34", "D. 12"],
    "answer": "C"
}
]

# display questions and options

score = 0

random.shuffle(questions)

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (A, B, C, D): ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")

print("\nQuiz completed!")
print(f"Your total score is {score}/{len(questions)}")
