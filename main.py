import acc
import quizTracking
import dashboard

def main():
    username = acc.main()  
    if username:
        quizTracking.main(username)  

        
        conn = quizTracking.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_performance WHERE username=?", (username,))
        user_performance = cursor.fetchone()
        
        cursor.execute("SELECT percentile FROM global_stats WHERE username=?", (username,))
        user_percentile = cursor.fetchone()
        
        if user_performance and user_percentile:
            quiz_data = {
                "rank": 0,  # dummy placeholder value 
                "total_users": 0,  # dummy placeholder value
                "percentile": user_percentile[0],
                "marks": user_performance[1],
                "total_questions": 5,  
                "time_taken": user_performance[2],
                "correct": user_performance[3],
                "incorrect": user_performance[4],
                "skipped": user_performance[5]
            }
            
            # Calculate and set rank and total_users
            cursor.execute("SELECT COUNT(*) FROM global_stats")
            total_users = cursor.fetchone()[0]
            
            if total_users > 0:
                cursor.execute("SELECT COUNT(*) FROM global_stats WHERE marks > (SELECT marks FROM global_stats WHERE username=?)", (username,))
                rank = cursor.fetchone()[0] + 1  # Rank is 1-based
                quiz_data["rank"] = rank
                quiz_data["total_users"] = total_users
            
            dashboard.create_dashboard(quiz_data)
        else:
            print("No performance or percentile data found for the user.")
    else:
        print("Failed to login or register.")

if __name__ == "__main__":
    main()
