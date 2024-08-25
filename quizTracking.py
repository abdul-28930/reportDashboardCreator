import sqlite3
import time
import randomQuestion
import random

def create_connection():
    conn = sqlite3.connect('quiz_data.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS global_stats (
                        username TEXT PRIMARY KEY,
                        marks INTEGER,
                        time_taken TEXT,
                        correct_answers INTEGER,
                        incorrect_answers INTEGER,
                        skipped_answers INTEGER,
                        percentile REAL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_performance (
                        username TEXT,
                        marks INTEGER,
                        time_taken TEXT,
                        correct_answers INTEGER,
                        incorrect_answers INTEGER,
                        skipped_answers INTEGER
                    )''')
    conn.commit()

def track_performance(username):
    num_questions = 5
    quiz = randomQuestion.generate_quiz(num_questions)
    correct = 0
    incorrect = 0
    skipped = 0
    start_time = time.time()

    print("Answer the following questions:")
    for i, q in enumerate(quiz):
        print(f"Question {i+1}: {q['question']}")
        for j, answer in enumerate(q['answers']):
            print(f"  {j+1}. {answer}")
        user_answer = input("Enter the number of your answer (or 'skip' to skip): ")
        if user_answer.lower() == 'skip':
            skipped += 1
        else:
            try:
                if q['answers'][int(user_answer) - 1] == q['correct']:
                    correct += 1
                else:
                    incorrect += 1
            except (IndexError, ValueError):
                print("Invalid input, skipping question.")
                skipped += 1

    time_taken = time.strftime("%Mm %Ss", time.gmtime(time.time() - start_time))
    marks = correct

    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT OR REPLACE INTO global_stats (username, marks, time_taken, correct_answers, incorrect_answers, skipped_answers) VALUES (?, ?, ?, ?, ?, ?)",
                   (username, marks, time_taken, correct, incorrect, skipped))
    conn.commit()

    print("Performance tracked successfully.")
    calculate_percentile()  

def calculate_percentile():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT username, marks FROM global_stats ORDER BY marks DESC")
    all_users = cursor.fetchall()

    total_users = len(all_users)
    if total_users == 0:
        return  
    
    for i, (username, marks) in enumerate(all_users):
        rank = i + 1
        percentile = ((total_users - rank) / total_users) * 100
        cursor.execute("UPDATE global_stats SET percentile=? WHERE username=?", (percentile, username))
    conn.commit()


def main(username):
    create_tables()
    track_performance(username)
    calculate_percentile()
