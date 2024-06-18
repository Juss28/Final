import random

# Define a list of questions and answers
quiz_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What element does 'O' represent on the periodic table?", "answer": "Oxygen"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "What year did the Titanic sink?", "answer": "1912"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    # Add more questions as needed
]

# Shuffle questions to make the quiz more dynamic
random.shuffle(quiz_questions)

def run_quiz():
    score = 0
    user_answers = []

    for i, q in enumerate(quiz_questions, start=1):
        print(f"Question {i}: {q['question']}")
        user_answer = input("Your answer: ").strip()
        user_answers.append({"question": q["question"], "user_answer": user_answer, "correct_answer": q["answer"]})

        if user_answer.lower() == q["answer"].lower():
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {q['answer']}.\n")

    print("\nQuiz completed!")
    print(f"Your final score is {score}/{len(quiz_questions)}\n")

    # Display the user's answers and the correct answers
    print("Here are your answers:")
    for ans in user_answers:
        print(f"Question: {ans['question']}")
        print(f"Your answer: {ans['user_answer']}")
        print(f"Correct answer: {ans['correct_answer']}\n")

if __name__ == "__main__":
    run_quiz()
