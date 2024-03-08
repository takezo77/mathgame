# math_game_IQ_test

import tkinter as tk
import random

class MathQuizApp:
    def __init__(self, master, total_problems=10, initial_time_limit=30):
        self.master = master
        self.total_problems = total_problems
        self.current_problem_index = 0
        self.correct_count = 0
        self.time_limit = initial_time_limit
        self.time_left = 0
        self.timer_running = False

        self.master.title("算数知能テスト")

        self.label_problem = tk.Label(self.master, text="", font=("Helvetica", 16))
        self.label_problem.pack(pady=20)

        self.label_instruction = tk.Label(self.master, text="答えを入力してください", font=("Helvetica", 14))
        
        self.label_instruction.pack(pady=10)
        
        self.entry_answer = tk.Entry(self.master, font=("Helvetica", 14))
        self.entry_answer.pack(pady=10)
        
        self.button_submit = tk.Button(self.master, text="回答する", command=self.check_answer, state=tk.DISABLED)
        self.button_submit.pack(pady=10)
        
        self.label_time = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.label_time.pack(pady=10)

        self.label_result = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.label_result.pack(pady=10)
        
       

        self.button_start = tk.Button(self.master, text="開始", command=self.start_quiz)
        self.button_start.pack(pady=10)

        self.button_retry = tk.Button(self.master, text="もう一度やる", command=self.retry_quiz, state=tk.DISABLED)
        self.button_retry.pack(pady=10)

        

    def generate_addition_problem(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 + num2
        return f"{num1} + {num2} = ?", answer

    def generate_subtraction_problem(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, num1)
        answer = num1 - num2
        return f"{num1} - {num2} = ?", answer

    def generate_multiplication_problem(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 * num2
        return f"{num1} × {num2} = ?", answer

    def generate_problem(self):
        if self.current_problem_index < self.total_problems:
            problem_type = random.choice(["addition", "subtraction", "multiplication"])
            if problem_type == "addition":
                problem, self.answer = self.generate_addition_problem()
            elif problem_type == "subtraction":
                problem, self.answer = self.generate_subtraction_problem()
            elif problem_type == "multiplication":
                problem, self.answer = self.generate_multiplication_problem()

            self.label_problem.config(text=problem)
            self.entry_answer.delete(0, tk.END)  # エントリをクリア
            self.label_result.config(text="")
            self.start_timer()
        else:
            self.show_result()

    def start_quiz(self):
        self.button_start.config(state=tk.DISABLED)
        self.button_submit.config(state=tk.NORMAL)
        self.button_retry.config(state=tk.NORMAL)
        self.generate_problem()

    def check_answer(self):
        if self.timer_running:
            self.stop_timer()
            user_input = self.entry_answer.get()
            user_answer = int(user_input) if user_input.isdigit() else None

            if user_answer == self.answer:
                self.correct_count += 1
                self.label_result.config(text="正解！", fg="green")
            else:
                self.label_result.config(text=f"不正解。正解は {self.answer} です。", fg="red")

            self.current_problem_index += 1
            self.update_time_label()
            self.generate_problem()

    def show_result(self):
        score = int((self.correct_count / self.total_problems) * 100)
        if score == 100:
            message = "あなたの知能はノイマンと同じくらいです！"
        elif score == 90: 
            message = "あなたの知能はアインシュタインと同じくらいです！"          
        elif score == 80:
            message = "あなたの知能はインテリと同じくらいです！"
        elif 70 >= score >= 50:
            message = "あなたの知能は凡人と同じくらいです！"
        elif 40 >= score >= 30:
            message = "あなたの知能はチンパンジーと同じくらいです！"
        elif 20 >= score >= 10:
            message = "あなたの知能はカラスと同じくらいです！"
        elif score == 0: 
            message = "あなたの知能はゴキブリと同じくらいです！"

        result_text = f"正解数: {self.correct_count}/{self.total_problems}\nスコア: {score}/100\n{message}"
        self.label_result.config(text=result_text)
        self.button_submit.config(state=tk.DISABLED)
        self.button_retry.config(state=tk.NORMAL)

    def start_timer(self):
        self.time_left = self.time_limit
        self.timer_running = True
        self.update_time_label()
        self.master.after(1000, self.update_timer)

    def update_timer(self):
        if self.timer_running:
            self.time_left -= 1
            self.update_time_label()
            if self.time_left > 0:
                self.master.after(1000, self.update_timer)
            else:
                self.label_result.config(text="時間切れ！", fg="red")
                self.current_problem_index += 1
                self.generate_problem()

    def stop_timer(self):
        self.timer_running = False

    def update_time_label(self):
        self.label_time.config(text=f"残り時間: {self.time_left}秒")

    def retry_quiz(self):
        self.current_problem_index = 0
        self.correct_count = 0
        self.button_start.config(state=tk.NORMAL)
        self.button_submit.config(state=tk.DISABLED)
        self.button_retry.config(state=tk.DISABLED)
        self.time_limit = 30  # 制限時間を初期値にリセット
        self.generate_problem()

# アプリケーションの起動コード
if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
