
# ---------------------------------------------------------
# pyinstaller
# Pythonでファイルをexe化する
# pyinstaller pythonファイル名 [--onefile] [--noconsole]
# buildとdistというフォルダが作成される。distフォルダにexeファイルが置かれる。
# .specはビルド方法について記述されたテキストファイル
# オプション
# onefile ：ファイルを1つにまとめる。基本的に指定。
# noconsole ：実行時にコンソールの表示を抑制する。
# debug all ：デバッグ出力。exe化に失敗したときなどの調査。
# clean ：キャッシュを削除する。
# icon ：アイコンファイルのパスを指定する。
# name ：exeファイル名を指定する。
# ---------------------------------------------------------
# venv
# 仮想環境を構築し、requestsとpyinstallerをインストールする
# python -m venv venv
# venv\Scripts\activate
# pip install requests
# pip install pyinstaller
# ---------------------------------------------------------
# Tkinterライブラリ（Python標準）
# https://python.keicode.com/advanced/tkinter.php
# ---------------------------------------------------------

import tkinter
import pyautogui

#終了処理s
def Quit(val):
    root.quit()
    root.destroy()

#ボタンクリック：ラベル変更テスト
def Label_Change(val):
    Static1['text']=val

# ALT+TAB⇒キー入力（writeは日本語が入力できないので注意する）
def Paste(val):
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')
    pyautogui.write(val)

###################################
# ※インポートされた際にプログラムが動かないようにする
# __name__ => モジュール名文字列に置き換わる
# 直接実行した場合は 「__main__」 に置き換わる（インポートの時は import xxxx になる）
if __name__ == "__main__":
    #オブジェクト生成
    root = tkinter.Tk()
    #ウィンドウ タイトル名
    root.title("ウィンドウタイトル")
    #ウィンドウ サイズ
    root.geometry("150x600")

#    #EditBox
#    FileEditBox = tkinter.Entry(width = 15)
#    FileEditBox.grid(row = 1, column = 1)

    #ボタン幅
    ButtonWidth = 15

    #ラベル
    Static1 = tkinter.Label(text=u'サンプルツール', foreground='#000000')
    Static1.place(x=10, y=20)

    #ボタンオブジェクト：ラベルチェンジ
    Button = tkinter.Button(text=u'ラベルチェンジ', width=ButtonWidth,  command = lambda: Label_Change('テスト') )
    Button.place(x=10, y=50)

    #ボタンオブジェクト：キー操作
    Button = tkinter.Button(text=u'キー操作', width=ButtonWidth,  command = lambda: Paste('this test msg') )
    Button.place(x=10, y=80)


    #ボタンオブジェクト：終了
    Button = tkinter.Button(text=u'終了', width=ButtonWidth,  command = lambda: Quit(11) )
    Button.place(x=10, y=550)

    #イベントループ
    root.mainloop()


