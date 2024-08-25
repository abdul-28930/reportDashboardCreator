import random #dummy generator for testing purposes

def generate_quiz(num_questions):
    questions = [
        {"question": "What is the capital of France?", "answers": ["Paris", "London", "Rome", "Berlin"], "correct": "Paris"},
        {"question": "What is 2 + 2?", "answers": ["3", "4", "5", "6"], "correct": "4"},
        {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Mars", "Jupiter", "Saturn"], "correct": "Jupiter"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answers": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "Jane Austen"], "correct": "Harper Lee"},
        {"question": "What is the chemical symbol for water?", "answers": ["H2O", "O2", "CO2", "NaCl"], "correct": "H2O"},
    ]

    quiz = random.sample(questions, num_questions)
    return quiz

def display_quiz(quiz):
    for i, q in enumerate(quiz):
        print(f"Question {i+1}: {q['question']}")
        for j, answer in enumerate(q['answers']):
            print(f"  {j+1}. {answer}")
        print()

if __name__ == "__main__":
    num_questions = 3  
    quiz = generate_quiz(num_questions)
    display_quiz(quiz)
