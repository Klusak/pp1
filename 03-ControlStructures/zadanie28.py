pierwsza=0
druga=1
print(pierwsza,druga,end=" ")
for i in range(50):
    trzecia=pierwsza+druga
    print(trzecia,end=" ")
    pierwsza=druga
    druga=trzecia
