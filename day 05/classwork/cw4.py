#4) შემოატანინეთ მომხმარებელს ასო თუ ეს ასო არის 'A' მაშინ გამოიტანეთ რიცხვი 100, თუ ის არის 'B' - 80, თუ 'C' - 60, თუ 'D' - 40, ხოლო თუ 'F' მაშინ სიტყვა 'Failed!'
mark = input("Enter random letter: ")
if mark == "A":
    print(100)
elif mark == "B":
    print(80)
elif mark == "C":
    print(60)
elif mark == "D":
    print(40)
elif mark == 'F':
    print("failed")
else:
    print("Enter correct letter")
