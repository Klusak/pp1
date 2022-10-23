x=int(input("podaj x: "))
y=int(input("podaj y: "))
if x>0 and y>0:
    print(f"punkt p{x,y} znajduje sie w 1 cwiartce")
if x<0 and y>0:
    print(f"punknt p{x,y} znajduje sie w 2 cwiartce")
if x<0 and y<0:
    print(f"punkt p{x,y} znajduje sie w 3 cwiartce")
if x>0 and y<0:
    print(f"punkt p{x,y} znajduje sie w 4 cwiartce")
if x==0 and y!=0:
    print(f"punkt p{x,y} znajduje sie na osi y")
if y==0 and x!=0:
    print(f"punkt p{x,y} znajduje sie na osi x")
if x==0 and y==0:
    print(f"punkt p{x,y} znajduje sie w pozycji (0,0)")
