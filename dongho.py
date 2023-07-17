import tkinter as tk
import time
from tkinter import simpledialog
import playsound

class App:
    def __init__(self, master):

        self.master = master
        master.title("Đồng hồ")
        self.current_time_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.current_time_label.pack()

        self.time_label = tk.Label(master, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Bắt đầu", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(master, text="Dừng lại", command=self.stop)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(master, text="Đặt lại", command=self.reset)
        self.reset_button.pack(side="left")

        self.set_timer_button = tk.Button(master, text="Đặt hẹn giờ", command=self.set_timer)
        self.set_timer_button.pack(side="left")
        self.quit_button = tk.Button(master, text="Thoát", command=master.quit)
        self.quit_button.pack(side="right")
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.timer_seconds = None
        self.time_label.config(bg="pink", fg="yellow")
        self.current_time_label.config(bg="pink",fg="black")
        self.start_button.config(bg="pink",fg="black")
        self.stop_button.config(bg="pink",fg="black")
        self.reset_button.config(bg="pink",fg="black")
        self.set_timer_button.config(bg="pink",fg="black")
        self.quit_button.config(bg="pink",fg="black")
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.update()

    def update(self):
        current_time_string = time.strftime("%H:%M:%S", time.localtime())
        self.current_time_label.config(text=current_time_string)
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.time_string = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
            self.time_label.config(text=self.time_string)
            if self.timer_seconds is not None:
                time_left = self.timer_seconds - int(self.elapsed_time)
                if time_left <= 0:
                    self.time_label.config(text="HẾT GIỜ!")
                    self.is_running = False
                elif time_left <= 60:
                    self.time_label.config(fg="red")
                else:
                    self.time_label.config(fg="black")
                self.time_label.after(1000, self.update)
        if self.timer_seconds is not None:
            time_left = self.timer_seconds - int(self.elapsed_time)
            if time_left <= 0:
                self.time_label.config(text="HẾT GIỜ!")
                self.is_running = False
                playsound.playsound("file.mp3")
            elif time_left <= 60:
                self.time_label.config(fg="red")
            else:
                self.time_label.config(fg="black")
            self.time_label.after(1000, self.update)
        else:
            time_left = 0
    def stop_sound(self):
        playsound.playsound(None)

    def stop(self):
        if self.is_running:
            self.is_running = False
        self.stop_sound()
    def reset(self):
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")
        self.time_label.config(fg="black")
        self.timer_seconds = None

    def set_timer(self):
        self.is_running = False
        self.timer_seconds = simpledialog.askinteger("Đặt hẹn giờ", "Nhập số giây:")
        if self.timer_seconds is not None:
            self.elapsed_time = 0
            self.start_time = time.time()
            self.time_label.config(text=self.timer_seconds)
            self.update()

root = tk.Tk()
app = App(root)
root.mainloop()
