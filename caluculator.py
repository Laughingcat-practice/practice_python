import tkinter as tk

def add_to_entry(char):
    entry.insert(tk.END, char)

#計算処理
def caluculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')

#全削除
def delete():
    entry.delete(0, tk.END)

#最後の1文字だけを削除
def delete_last():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1]) # 最後の1文字を削除した内容を挿入

#キーボード入力
def handle_keypress(event):
    key = event.char
    keysym = event.keysym
    #入力可能な文字
    allowed_chars = '0123456789+-*/.=()'

    if key in allowed_chars:
        add_to_entry(key)
    elif keysym == 'Return':
        caluculate()
    elif keysym == 'Backspace':
        delete_last()
    elif key.lower() == 'c':
        delete()

    return 'break'

#ウインドウの作成
root = tk.Tk()

# ウィジットの配置
entry = tk.Entry(root, width=25, font=('Arial', 20))
#入力可能なテキストボックスの作成
entry.grid(row=0, column=0, columnspan=4)

#ボタンの作成
#ボタンを１つずつ作成する場合
# btn_7 = tk.Button(root, text = '7', font=('Arial', 20), width = 5, height = 2)
# btn_7.grid(row = 1, column = 0)
# btn_8 = tk.Button(root, text = '8', font=('Arial', 20), width = 5, height = 2)
# btn_8.grid(row = 1, column = 1)
# btn_9 = tk.Button(root, text = '9', font=('Arial', 20), width = 5, height = 2)
# btn_9.grid(row = 1, column = 2)
# btn_wari = tk.Button(root, text = '/', font=('Arial', 20), width = 5, height = 2)
# btn_wari.grid(row = 1, column = 3)

#ボタンを複数まとめて作成
buttons = [
    ['C', '⌫', ' ', ' '],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+']
]

for row in range(len(buttons)):
    for col in range(len(buttons[row])):
        char = buttons[row][col]
        if char == '=':
            cmd= caluculate
        elif char == 'C':
            cmd= delete
        elif char == '⌫':
            cmd= delete_last
        elif char == " ":
            continue
        else:
            cmd = lambda c=char: add_to_entry(c)

        btn = tk.Button(root, text=char, width=5, height=2, command = cmd)
        btn.grid(row=row + 1, column=col)

entry.bind('<KeyPress>', handle_keypress)
#メインループ
root.mainloop()
