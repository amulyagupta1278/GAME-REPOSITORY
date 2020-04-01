from tkinter import *
import random
from PIL import Image, ImageTk

yc=0
rc=0
def printt(args):
	moves=['r', 'p', 's']
	player_wins=['pr', 'sp', 'rs']
	global yc
	global rc

	
	player_move=args
	
	computer_move=random.choice(moves)
	label4['text']=player_move
	label5['text']=computer_move

	if player_move==computer_move:
		label6['text']='Tie'
	elif player_move+computer_move in player_wins:
		label6['text']='You Win'
		yc=yc+1
		yc_s=str(yc)
		label8['text']='You: '+yc_s
	else:
		label6['text']='You Loose'
		rc=rc+1
		rc_s=str(rc)
		label9['text']='Robo: '+rc_s

window=Tk()
window.geometry("600x600")
window.title("Welcome")
window.configure(bg='#F9D200')
"""

imge =Image.open('rps.jpeg')
size=width, height = imge.size
imge.thumbnail((200,500))
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo)
lab.pack()
"""

label7=Label(window,fg='blue', text="LET'S PLAY ROCK-PAPER-SCISSOR", bg='#F9D200', font=("arial", 20, "bold", "underline"))
label7.place(x=50, y=150)
label1=Label(window,text="Score :" ,fg='black', bg='#F9D200', font=("arial", 25, "bold"))
label1.place(x=10, y=200)
label8=Label(window,fg='black',text="You: 0", bg='#F9D200', font=("arial", 25, "bold"))
label8.place(x=250, y=200)
label9=Label(window,fg='black',text="Robo: 0", bg='#F9D200', font=("arial", 25, "bold"))
label9.place(x=400, y=200)
label2=Label(window,text="You :" ,fg='black', bg='#F9D200', font=("arial", 20, "bold"))
label2.place(x=10, y=250)
label3=Label(window,text="Robo :" ,fg='black', bg='#F9D200', font=("arial", 20, "bold"))
label3.place(x=10, y=300)
label4=Label(window,fg='red', bg='#F9D200', font=("arial", 20, "bold"))
label4.place(x=300, y=250)
label5=Label(window,fg='red', bg='#F9D200', font=("arial", 20, "bold"))
label5.place(x=300, y=300)
label6=Label(window,fg='red', bg='#F9D200', font=("arial", 20, "bold"))
label6.place(x=250, y=350)

button_1=Button(window,fg='red', bg='pink', font=("arial", 25, "bold"), text='rock', command=lambda:printt('r'))
button_1.place(x=50, y=400)
button_2=Button(window,fg='red', bg='pink', font=("arial", 25, "bold"), text='paper', command=lambda:printt('p'))
button_2.place(x=200, y=400)
button_3=Button(window,fg='red', bg='pink', font=("arial", 25, "bold"), text='scissor', command=lambda:printt('s'))
button_3.place(x=350, y=400)

window.mainloop()
