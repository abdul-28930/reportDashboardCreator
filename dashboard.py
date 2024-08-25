import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def create_dashboard(data):
    root = tk.Tk()
    root.title("Quiz Dashboard")

    # font and alignments
    font_title = ("Helvetica", 16, "bold")
    font_labels = ("Helvetica", 12)
    
    # text on dashboard
    tk.Label(root, text=f"Rank (based on first attempt)", font=font_labels).grid(row=0, column=0, sticky="w", padx=20)
    tk.Label(root, text=f"{data['rank']}/{data['total_users']}", font=font_labels).grid(row=0, column=1, sticky="e", padx=20)

    tk.Label(root, text="Percentile (based on first attempt)", font=font_labels).grid(row=1, column=0, sticky="w", padx=20)
    tk.Label(root, text=f"{data['percentile']}%", font=font_labels).grid(row=1, column=1, sticky="e", padx=20)

    tk.Label(root, text="Your Marks", font=font_labels).grid(row=2, column=0, sticky="w", padx=20)
    tk.Label(root, text=f"{data['marks']}/{data['total_questions']}", font=font_labels).grid(row=2, column=1, sticky="e", padx=20)

    tk.Label(root, text="Time Taken", font=font_labels).grid(row=3, column=0, sticky="w", padx=20)
    tk.Label(root, text=data['time_taken'], font=font_labels).grid(row=3, column=1, sticky="e", padx=20)

    tk.Label(root, text="Correct Questions", font=font_labels).grid(row=4, column=0, sticky="w", padx=20)
    tk.Label(root, text=data['correct'], font=font_labels).grid(row=4, column=1, sticky="e", padx=20)

    tk.Label(root, text="Incorrect Questions", font=font_labels).grid(row=5, column=0, sticky="w", padx=20)
    tk.Label(root, text=data['incorrect'], font=font_labels).grid(row=5, column=1, sticky="e", padx=20)

    tk.Label(root, text="Skipped Questions", font=font_labels).grid(row=6, column=0, sticky="w", padx=20)
    tk.Label(root, text=data['skipped'], font=font_labels).grid(row=6, column=1, sticky="e", padx=20)

    # bar plot code
    fig, ax = plt.subplots(figsize=(6, 2))
    categories = ["Total", "Correct", "Incorrect", "Skipped"]
    values = [data['total_questions'], data['correct'], data['incorrect'], data['skipped']]
    colors = ["#1f77b4", "#2ca02c", "#d62728", "#8c564b"]

    ax.barh(categories, values, color=colors)
    ax.set_xlim(0, data['total_questions'])
    ax.set_xlabel("Questions")
    
    for i, v in enumerate(values):
        ax.text(v + 0.1, i, str(v), color="black", va="center", fontweight="bold")

    # tkinter windows pops up
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=7, padx=20, pady=10)
    canvas.draw()

    root.mainloop()

if __name__ == "__main__":
    quiz_data = {
        "rank": 1772,
        "total_users": 3133,
        "percentile": 43.00,
        "marks": 11,
        "total_questions": 20,
        "time_taken": "24m 57s",
        "correct": 11,
        "incorrect": 9,
        "skipped": 0
    }

    create_dashboard(quiz_data)
