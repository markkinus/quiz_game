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

    try:  # CORRECT: inside the loop
        answer = input("Enter your answer (A, B, C, D): ").upper()

        if answer not in ["A", "B", "C", "D"]:
            raise ValueError("Invalid option. Choose A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")

    except ValueError as e:
        print(e)

print("\nQuiz completed!")
print(f"Your total score is {score}/{len(questions)}")

