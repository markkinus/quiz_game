import random

# questions and options
questions = [
    {
        "question": "What is 15 + 10?",
        "options": ["A. 25", "B. 23", "C. 34", "D. 12"],
        "answer": "A"
    },
    {
        "question": "What is 13 + 10?",
        "options": ["A. 25", "B. 23", "C. 34", "D. 12"],
        "answer": "B"
    },
    {
        "question": "What is 24 + 10?",
        "options": ["A. 25", "B. 23", "C. 34", "D. 12"],
        "answer": "C"
    }
]


score = 0

random.shuffle(questions)

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    while True:
        try:
            answer = input("Enter your answer (A, B, C, D): ").upper()

            if answer not in ["A", "B", "C", "D"]:
                raise ValueError("Choose A, B, C, or D.")

            break

        except ValueError as e:
            print(e)

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")

print("\nQuiz completed!")
print(f"Your total score is {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Your percentage is {percentage:.2f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 50:
    print("Good!")
else:
    print("Try Again!")