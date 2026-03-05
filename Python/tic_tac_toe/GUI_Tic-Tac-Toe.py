import tkinter as tk
from tkinter import messagebox

currentplayer='X'

def on_click(i):
    if board[i]==' ':
        board[i]=currentplayer
        button[i].config(text=currentplayer)
        if check_win(board,currentplayer):
            disable_buttons()
            messagebox.showinfo("Game Over",f"Player {currentplayer} Wins!")
        elif ' ' not in board:
            disable_buttons()
            messagebox.showinfo("Game Over","It's a Draw!")
        else:
            change_player()

def change_player():
    global currentplayer
    if currentplayer=='X':
        currentplayer='O'
    else:
        currentplayer='X'

def disable_buttons():
    for b in button:
        b.config(state="disabled")

def check_win(board, currentplayer):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == currentplayer:
            return True
    return False
    

board=[' ']*9
button=[]

window=tk.Tk()
window.title("Tic Tac Toe")
for k in range(0,9):
    btn=tk.Button(window,text=' ',width=5,height=2,font=("Arial", 24),command=lambda i=k:on_click(i))

    r=k // 3
    c=k % 3
    btn.grid(row=r, column=c, padx=5, pady=5)
    button.append(btn)


window.mainloop()