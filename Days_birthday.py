print("Enter Today's Date ",end="")
c_day=int(input(":"))
c_month=int(input(":"))
print("Enter Next Birthday's Date ")
b_day=int(input(":"))
b_month=int(input(":"))
nod=0
nom=0
if b_month-c_month < 0:
    nom=b_month-c_month+12
else:
    nom=b_month-c_month
if b_day-c_day < 0:
    nod=b_day-c_day+30
else:
    nod=b_day-c_day
if nod>=30:
    nod=nod%30
    nom+=1
days=((nom-1)*30)+nod
print("Total Days : ",days)
    