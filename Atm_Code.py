from tkinter import *
import tkinter.font as font         # imports font module and being imported as font. It helps to define a specific font style
import tkinter as tk
import pymysql as sql
import time
from datetime import date
from sklearn.linear_model import LinearRegression
import numpy as np

glob_count = 0
      # this is used to access balance_func() after press yes in question_func()
# displays message after selecting no in question_func()
class ATM:
    def __init__(self,win):
        self.win = win
        win.title('ATM')
        win.geometry('460x390')
        self.interface()
        
    def display_func(self):

        self.question_win.withdraw()
        self.display_win = Toplevel(self.win)
        self.display_win.geometry('460x390')
        message = Message(self.display_win, text='\n\nYour transaction has been successful\n\nThank you for using our', font=self.cour20, fg='blue')
        message.pack()
        text = Label(self.display_win, text='ATM', font=self.tim40, fg='red')
        text.pack()

        exit_button = Button(self.display_win, text='EXIT', font=self.cour15, fg='red', command=self.prediction_interface)
        exit_button.pack(side=BOTTOM, pady=10)


    # window asking whether to show balance or not
    def question_func(self):

        global glob_count
        glob_count+=1

        self.withdrawal_win.withdraw()
        self.question_win = Toplevel(self.win)
        self.question_win.geometry('460x390')

        self.money_entered = int(self.money_entry.get())
        self.bal_lst = self.bal_lst-self.money_entered
        if self.bal_lst<=0:
            self.ins_bal = Button(self.question_win,text="Sorry insufficient funds",font=self.cour15,fg='red',pady=20,command =self.option_func)
            self.ins_bal.pack()
        else:
            self.date = date.today()
            self.time =time.strftime("%H:%M:%S", time.localtime()) 
            update =self.my_cursor.execute("UPDATE customer SET Balance=%s WHERE Pin =%s",(self.bal_lst,self.user_id))
            insert_transaction = self.my_cursor.execute("INSERT INTO transactions (Transactions,Date,Time,Pin) VALUES(%s,%s,%s,%s)",(self.money_entered,self.date,self.time,self.user_id))
            self.mydb.commit()
            bf = Frame(self.question_win)
            bf.pack(side=BOTTOM)
            0
            msg_box = Message(self.question_win, text='\nYour transaction has been successful\n\nPlease collect your money\n\nYou can remove your card\n\nDo you want to check your balance?', font=self.cour20, fg='blue')
            msg_box.pack()

            yes_btn = Button(bf, text='YES', font=self.cour15, fg='green', command=self.balance_func)
            yes_btn.pack(side=LEFT, pady=10)

            no_btn = Button(bf, text=' NO ', font=self.cour15, fg='red', command=self.display_func)
            no_btn.pack(pady=10, padx=10)


    # withdrawing money window
    def withdrawal_func(self):

        self.option_win.withdraw()
        self.withdrawal_win = Toplevel(self.win)
        self.withdrawal_win.geometry('460x390')

        enter_lbl = Label(self.withdrawal_win, text='\nPlease enter amount\n', font=self.cour20, fg='red')
        enter_lbl.pack()
        self.money_entry = Entry(self.withdrawal_win, font=self.cour15, justify='center')
        self.money_entry.pack()

        bf = Frame(self.withdrawal_win)
        bf.pack(side=BOTTOM)

        bf4 = Frame(self.withdrawal_win)
        bf4.pack(side=BOTTOM)

        bf3 = Frame(self.withdrawal_win)
        bf3.pack(side=BOTTOM)

        bf3 = Frame(self.withdrawal_win)
        bf3.pack(side=BOTTOM)

        bf2 = Frame(self.withdrawal_win)
        bf2.pack(side=BOTTOM)

        bf1 = Frame(self.withdrawal_win)
        bf1.pack(side=BOTTOM)

        b1 = Button(bf1, text='1', font=self.cour15, command=lambda: self.money_entry.insert('end', '1'))
        b1.pack(side=LEFT, pady=10)

        b2 = Button(bf1, text='2', font=self.cour15, command=lambda: self.money_entry.insert('end', '2'))
        b2.pack(side=LEFT, padx=10)

        b3 = Button(bf1, text='3', font=self.cour15, command=lambda: self.money_entry.insert('end', '3'))
        b3.pack(side=LEFT)

        b4 = Button(bf2, text='4', font=self.cour15, command=lambda: self.money_entry.insert('end', '4'))
        b4.pack(side=LEFT)

        b5 = Button(bf2, text='5', font=self.cour15, command=lambda: self.money_entry.insert('end', '5'))
        b5.pack(side=LEFT, padx=10)

        b6 = Button(bf2, text='6', font=self.cour15, command=lambda: self.money_entry.insert('end', '6'))
        b6.pack(side=LEFT)

        b7 = Button(bf3, text='7', font=self.cour15, command=lambda: self.money_entry.insert('end', '7'))
        b7.pack(side=LEFT, pady=10)

        b8 = Button(bf3, text='8', font=self.cour15, command=lambda: self.money_entry.insert('end', '8'))
        b8.pack(side=LEFT, padx=10)

        b9 = Button(bf3, text='9', font=self.cour15, command=lambda: self.money_entry.insert('end', '9'))
        b9.pack(side=LEFT)

        btn = Button(bf4, text=' ', font=self.cour15)
        btn.pack(side=LEFT)

        b0 = Button(bf4, text='0', font=self.cour15, command=lambda: self.money_entry.insert('end', '0'))
        b0.pack(side=LEFT, padx=10)

        btn_ = Button(bf4, text=' ', font=self.cour15)
        btn_.pack(side=LEFT)

        enter_btn = Button(bf, text='ENTER', font=self.cour15, fg='green', command=self.question_func)
        enter_btn.pack(side=LEFT, pady=10)

        clear_btn = Button(bf, text='CLEAR', font=self.cour15, fg='orange', command=lambda: self.money_entry.delete(1))
        clear_btn.pack(side=LEFT, padx=10)


    # balance displaying window
    def balance_func(self):

        global glob_count

        if glob_count == 1:
            self.question_win.withdraw()

        self.option_win.withdraw()
        self.balance_win = Toplevel(self.win)
        self.balance_win.geometry('460x390')
        #balance_win.grab_set()
        balance = self.bal_lst
        message = Message(self.balance_win,text='\nYour transaction is successful\n\nAvailable Balance: '+str(balance)+'\n\nThank you for using our', font=self.cour20, fg='blue')
        message.pack()
        text = Label(self.balance_win, text='ATM', font=self.tim40, fg='red')
        text.pack()

        exit_button = Button(self.balance_win, text='EXIT', font=self.cour15, fg='red', command= self.prediction_interface)
        exit_button.pack(side=BOTTOM, pady=10)
        
    # displays message after change has been changed
    def prediction_interface(self):
         try:
            self.balance_win.destroy()
         except:
             self.display_win.destroy()
         self.ml_win = Toplevel(self.win)
         self.Machine_learning = Message(self.ml_win,text ='Do you want to predict the future transaction of the current user?',font = self.cour20,fg = 'red')
         self.Machine_learning.pack()
         predict_button = Button(self.ml_win,text = 'Predict',font=self.cour15,fg='red',command = self.pred_algo)
         predict_button.pack(side = BOTTOM,pady=10)
    def pred_algo(self):
         self.ml_win.destroy()
         self.algo_Win = Toplevel(self.win)
         self.mydb = sql.connect(
         host="localhost",
         user = "root",
         password="",
         database="ATM Data"
          )


         self.my_cursor = self.mydb.cursor()
         #self.user_id =  self.entry_box.get()
         self.my_cursor.execute("SELECT Transactions FROM transactions where Pin = %s",self.user_id)
         global t
         t = self.my_cursor.fetchall()
         self.y_train = np.concatenate(t)
         self.X_train = np.full((len(self.y_train), 1), 1111)

         self.model = LinearRegression().fit(self.X_train,self.y_train)
         self.predctions = self.model.predict([[1111]])
         self.msg = Message(self.algo_Win,text='The Next transaction may be:'+str(self.predctions), font=self.cour15,fg='red')
         self.msg.pack()
         exit_button = Button(self.algo_Win, text='EXIT', font=self.cour15, fg='red', command=lambda: self.win.destroy())
         exit_button.pack(side=BOTTOM, pady=10)

    def message_func(self):
        self.change_pin_win.withdraw()
        win2 = Toplevel(self.win)
        win2.geometry('460x390')
        message = Message(win2, text='\nYour transaction is successful\n\nYour PIN has been successfully changed\n\nThank you for using our', font=self.cour20, fg='blue')
        message.pack()
        text = Label(win2, text='ATM', font=self.tim40, fg='red')
        text.pack()
        self.ch_pin = self.pin_entry.get()
        updates =self.my_cursor.execute("UPDATE customer SET Pin=%s WHERE Pin =%s",(self.ch_pin,self.user_id))
        self.mydb.commit()
        
        update_trans = self.my_cursor.execute("UPDATE transactions SET Pin=%s WHERE Pin =%s",(self.ch_pin,self.user_id))
        self.mydb.commit()
        exit_button = Button(win2, text='EXIT', font=self.cour15, fg='red', command=lambda: self.win.destroy())
        exit_button.pack(side=BOTTOM, pady=10)


    # changing pin function
    def change_pin_func(self):
        self.option_win.withdraw()
        self.change_pin_win = Toplevel(self.win)
        self.change_pin_win.geometry('460x420')

        pin_lbl = Label(self.change_pin_win, text='\nEnter new-PIN', font=self.cour15, fg='red')
        pin_lbl.pack()
        self.pin_entry = Entry(self.change_pin_win, font=self.cour15,justify='center', show='*')
        self.pin_entry.pack()
        

        re_entry_lbl = Label(self.change_pin_win, text='\nRe-enter new-PIN', font=self.cour15, fg='red')
        re_entry_lbl.pack()
        re_entry = tk.Entry(self.change_pin_win, font=self.cour15, justify='center', show='*')
        re_entry.pack()
        
        

        bf = Frame(self.change_pin_win)
        bf.pack(side=BOTTOM)

        bf4 = Frame(self.change_pin_win)
        bf4.pack(side=BOTTOM)

        bf3 = Frame(self.change_pin_win)
        bf3.pack(side=BOTTOM)

        bf3 = Frame(self.change_pin_win)
        bf3.pack(side=BOTTOM)

        bf2 = Frame(self.change_pin_win)
        bf2.pack(side=BOTTOM)

        bf1 = Frame(self.change_pin_win)
        bf1.pack(side=BOTTOM)

        b1 = Button(bf1, text='1', font=self.cour15, command=lambda: [self.pin_entry.insert('end','1'), re_entry.insert('end','1')])
        b1.pack(side=LEFT,pady=10)

        b2 = Button(bf1, text='2', font=self.cour15, command=lambda: [self.pin_entry.insert('end','2'), re_entry.insert('end','2')])
        b2.pack(side=LEFT, padx=10)

        b3 = Button(bf1, text='3', font=self.cour15, command=lambda: [self.pin_entry.insert('end','3'), re_entry.insert('end','3')])
        b3.pack(side=LEFT)

        b4 = Button(bf2, text='4', font=self.cour15, command=lambda: [self.pin_entry.insert('end','4'), re_entry.insert('end','4')])
        b4.pack(side=LEFT)

        b5 = Button(bf2, text='5', font=self.cour15, command=lambda: [self.pin_entry.insert('end','5'), re_entry.insert('end','5')])
        b5.pack(side=LEFT, padx=10)

        b6 = Button(bf2, text='6', font=self.cour15, command=lambda: [self.pin_entry.insert('end','6'), re_entry.insert('end','6')])
        b6.pack(side=LEFT)

        b7 = Button(bf3, text='7', font=self.cour15, command=lambda: [self.pin_entry.insert('end','7'), re_entry.insert('end','7')])
        b7.pack(side=LEFT,pady=10)

        b8 = Button(bf3, text='8', font=self.cour15, command=lambda: [self.pin_entry.insert('end','8'), re_entry.insert('end','8')])
        b8.pack(side=LEFT, padx=10)

        b9 = Button(bf3, text='9', font=self.cour15, command=lambda: [self.pin_entry.insert('end','9'), re_entry.insert('end','9')])
        b9.pack(side=LEFT)

        btn = Button(bf4, text=' ', font=self.cour15)
        btn.pack(side=LEFT)

        b0 = Button(bf4, text='0', font=self.cour15, command=lambda: [self.pin_entry.insert('end','0'), re_entry.insert('end','0')])
        b0.pack(side=LEFT, padx=10)                         # with help of list we can assign multiple functions for buttons

        btn_ = Button(bf4, text=' ', font=self.cour15)
        btn_.pack(side=LEFT)

        enter_btn = Button(bf, text='ENTER', font=self.cour15, fg='green', command=self.message_func )
        enter_btn.pack(side=LEFT, pady=10)

        clear_btn = Button(bf, text='CLEAR', font=self.cour15, fg='orange', command=lambda: [self.pin_entry.delete(0), re_entry.delete(0)])
        clear_btn.pack(side=LEFT, padx=10)


    # options window
    def option_func(self):
        global num
        num = 0
        self.new_win.withdraw()     # check enter_pin() function for the functionality of .withdraw()
        self.option_win = Toplevel(self.win)
        #self.check_win = Toplevel(self.win)
        self.option_win.geometry('460x390')
    # option_win.grab_set()                       ## check enter_pin() function for the functionality of .grab_set()

        self.mydb = sql.connect(
        host="localhost",
        user = "root",
        password="",
        database="ATM Data"
        )


        self.my_cursor = self.mydb.cursor()
        self.user_id =  self.entry_box.get()
        self.my_cursor.execute("SELECT * FROM customer where Pin = %s",self.user_id)
        global p
        p = self.my_cursor.fetchall()
        print(p)
        self.my_cursor.execute("SELECT Balance from customer where Pin = %s",self.user_id)
        
        if p==():
            
            self.np = Button(self.option_win,text="Sorry please enter Valid pin",font=self.cour15,fg='red',pady=20,command =self.enter_pin)
            self.np.pack()
            
            
        else:
            global bal 
            bal = self.my_cursor.fetchall()
            self.bal_lst = []
            for x in bal:
                for z in x:
                    self.bal_lst.append(z)
            self.bal_lst = int(''.join(map(str, self.bal_lst)))
           
            text_title = Label(self.option_win, text='\nATM', font=self.tim40)
            text_title.pack(padx=40,pady=10)

            rf = Frame(self.option_win)          #right frame
            rf.pack(side=RIGHT)

            lf = Frame(self.option_win)          #left frame
            lf.pack(side=LEFT)

            withdrawal_btn = Button(rf, text=' WITHDRAWAL ', font=self.cour15, fg='blue', command=self.withdrawal_func)
            withdrawal_btn.pack(padx=40, pady=10)

            balance_btn = Button(rf, text='BALANCE INQ', font=self.cour15, command=self.balance_func)
            balance_btn.pack(padx=40, pady=10)

            change_pin_btn = Button(lf, text='CHANGE PIN', font=self.cour15, command=self.change_pin_func)
            change_pin_btn.pack(padx=40, pady=10)

            exit_btn = Button(lf, text='   EXIT   ', font=self.cour15, fg='red', command=lambda: [self.option_win.destroy(), self.new_win.deiconify()])
            exit_btn.pack(padx=40, pady=10)                                                                         # check enter_pin() function for the functionality of .deiconify()
        num =+1

    # enter_pin window
    def enter_pin(self):
        
        self.win.withdraw()  
                           # .withdraw() hides or make the associated window invisible until (.deiconify()) appears

        self.new_win = Toplevel(self.win)           # enter_pin.new_win makes the variable new_win as the member of the function object
        self.new_win.geometry('460x390')       # this helps us to use the variable even outside the function

        #enter_pin.new_win.grab_set()               ## .grab.set() makes the associated window inactive temporarily until the active window is working


        def setInputText(text):
            self.entry_box.insert('end',text)            # insert allows to enter(display on entry box) the text at the end(if we replace end with 0 the text is placed at front)

        def text_delete():
            self.entry_box.delete(0)                     # we have another function called delete which deletes text for the given range(.delete(0,'end') deletes the entire text

        lbl = Label(self.new_win, text='Enter your PIN',font=self.cour20,fg='red')
        lbl.pack(pady=20)

        self.entry_box = tk.Entry(self.new_win, font=self.cour15, show='*', justify='center')
        #piins = self.entry_box.get()

            
                

          # show parameter display the input text as *(we can use any other element also)
        self.entry_box.pack()

        bf = Frame(self.new_win)
        bf.pack(side=BOTTOM)

        bf0 = Frame(self.new_win)
        bf0.pack(side=BOTTOM)

        bf1 = Frame(self.new_win)
        bf1.pack(side=BOTTOM)

        bf2 = Frame(self.new_win)
        bf2.pack(side=BOTTOM)

        bf3 = Frame(self.new_win)
        bf3.pack(side=BOTTOM)

        bf4 = Frame(self.new_win)
        bf4.pack(side=BOTTOM)

        rf = Frame(self.new_win)
        rf.pack(side=RIGHT)

        btn1 = Button(bf4,text='1',font=self.cour15, command=lambda:setInputText('1'))
        btn1.pack(side=LEFT, pady=10)

        btn2 = Button(bf4, text='2', font=self.cour15, command=lambda:setInputText('2'))
        btn2.pack(side=LEFT,padx=10)

        btn3 = Button(bf4, text='3', font=self.cour15, command=lambda:setInputText('3'))
        btn3.pack(side=LEFT)

        btn4 = Button(bf3, text='4', font=self.cour15, command=lambda:setInputText('4'))
        btn4.pack(side=LEFT)

        btn5 = Button(bf3, text='5', font=self.cour15, command=lambda:setInputText('5'))
        btn5.pack(side=LEFT,padx=10)

        btn6 = Button(bf3, text='6', font=self.cour15, command=lambda:setInputText('6'))
        btn6.pack(side=LEFT)

        btn7 = Button(bf2, text='7', font=self.cour15, command=lambda:setInputText('7'))
        btn7.pack(side=LEFT,pady=10)

        btn8 = Button(bf2, text='8', font=self.cour15, command=lambda:setInputText('8'))
        btn8.pack(side=LEFT, padx=10)

        btn9 = Button(bf2, text='9', font=self.cour15, command=lambda:setInputText('9'))
        btn9.pack(side=LEFT)

        btn = Button(bf1, text=' ', font=self.cour15)
        btn.pack(side=LEFT)

        btn0 = Button(bf1, text='0', font=self.cour15, command=lambda:setInputText('0'))
        btn0.pack(side=LEFT, padx=10)

        btn_ = Button(bf1, text=' ', font=self.cour15)
        btn_.pack(side=LEFT)

        enter_btn = Button(bf0, text='ENTER', font=self.cour15,fg='green', command=self.option_func)
        enter_btn.pack(side= LEFT, pady=10,padx=10)

        exit_btn = Button(bf0, text='EXIT', font=self.cour15, fg='red', command=lambda:[self.new_win.destroy(), self.win.deiconify()])   # .deiconify() makes the associated window visible
        exit_btn.pack(side=RIGHT, padx=10)

        clear_btn = Button(bf0,text='CLEAR', font=self.cour15, fg='orange', command=text_delete)
        clear_btn.pack(side=LEFT)

        note = Label(bf, text='Note:Enter pin either from keyboard or keypad', fg='red')
        
        note.pack()

        
            

    

    def interface(self):
        self.tim40 = font.Font(family='Times', size=40, weight='bold', slant='italic', underline=1)
        self.cour20 = font.Font(family='Courier', size=20, weight='bold')
        self.cour15 = font.Font(family='Courier', size=15, weight='bold')
        intro = Label(self.win, text='\nWelcome User Customer', font=self.cour20, fg='green')
        intro.pack()
        option_label = Label(self.win, text='\nSelect your account type', font=self.cour15, fg='grey')
        option_label.pack()

        bottom_frame = Frame(self.win)
        bottom_frame.pack(side=BOTTOM)
        right_frame = Frame(self.win)
        right_frame.pack(side=RIGHT)

        note = Label(bottom_frame, text='NOTE:Use only EXIT button to exit', font=self.cour15, fg='red')
        note.pack(pady=10)
        saving = Button(right_frame, text='Savings', font=self.cour15, bg='sky blue', fg='red', command=self.enter_pin)
        saving.pack(padx=30, pady=10)
        current = Button(right_frame, text="Current", font=self.cour15, bg='sky blue', fg='red', command=self.enter_pin)
        current.pack(padx=30, pady=10)


                # main opening window
        title_label = Label(self.win, text='ATM', font=self.tim40, fg='red')              # Label is something similar to a label which displays text on the window
        title_label.pack(pady=10)                                               # pad y gives vertical distance both above and below where as pad x gives

              # Font is an instance which contains parameter as
         # family(the font style), size, weight(bold,normal)
         # slant(italic,roman(non-italic)), underline(1-yes,0-no),
        # overstrike(1-yes,0-no) and many more


        
    

    def database(self):

        self.mydb = sql.connect(
        host="localhost",
        user = "root",
        password="",
        database="ATM Data"
        )
        #ob = ATM()
        self.my_cursor = self.mydb.cursor()
        self.user_id =  self.entry_box.get( )
        self.my_cursor.execute("SELECT * FROM customer where Pin = %s",self.user_id)
        global p
        p = self.my_cursor.fetchall()
        self.my_cursor.execute("SELECT Balance from customer where Pin = %s",self.user_id)
        global bal 
        bal = self.my_cursor.fetchall()

def main():
        win = Tk()                          # creates the window
        app = ATM(win)             # sets the dimension of the window
        win.mainloop()
if __name__ == "__main__":
    main()

#displaying some introduction

