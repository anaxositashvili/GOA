#4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.
password= "python123"
user_password = input("enter your password")

while user_password !=password:
    user_password = input("enter your password again: ")