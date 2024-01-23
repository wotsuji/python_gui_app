from datetime import datetime
import tkinter as tk


class CurrentClock:
    """現在時刻 表示時計 クラス"""

    def __init__(
        self, window_size="250x100", window_title="Current Clock", resizable={"width": False, "height": False}
    ):
        """初期化"""
        self.job_id = None
        self.root = None
        self.label = None
        self.window_size = window_size
        self.window_title = window_title
        self.resizable = resizable

    def time_renew(self):
        """時計更新メソッド"""
        self.label["text"] = datetime.now().strftime("%H:%M:%S")
        self.job_id = self.root.after(999, self.time_renew)

    def clock_show(self):
        """時計表示メソッド"""
        # Tkinter
        self.root = tk.Tk()
        self.root.geometry(self.window_size)  # ウィンドウサイズ
        self.root.title(self.window_title)  # タイトル
        self.root.resizable(**self.resizable)  # 縦横固定

        # ラベル作成
        frame = tk.Frame(self.root)
        self.label = tk.Label(
            frame, text="", anchor=tk.CENTER, font=("メイリオ", 32), fg="WHITE", bg="GRAY", relief=tk.RIDGE, bd=4
        )
        self.label.pack(padx=18, pady=18, fill=tk.X)
        frame.pack()

        self.time_renew()
        self.root.mainloop()


if __name__ == "__main__":
    CurrentClock().clock_show()
