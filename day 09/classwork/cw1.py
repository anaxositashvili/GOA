#მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილაs
start=int(input("enter the 'start' number: "))
end=int(input("enter the 'end' number: "))
step=int(input("enter the 'step' number: "))

for i in range(start,end,step):
    print(i)