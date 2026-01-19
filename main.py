
def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C) Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B) 4"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "B) Jupiter"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
            "answer": "C) William Shakespeare"
        },
        {
            "question": "What is the boiling point of water?",
            "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"],
            "answer": "B) 100°C"
        }
    ]
    score = 0

    for index, q in enumerate(questions):
        # print(index, q)
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ")
        if user_answer.upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
        
    print(f"Your final score is {score} out of {len(questions)}")

run_quiz()
