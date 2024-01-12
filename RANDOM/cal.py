calculating = True

def sum(fnum, snum):
    return fnum+snum
def dif(fnum, snum):
    return fnum-snum
def mul(fnum, snum):
    return fnum*snum
def div(fnum, snum):
    return fnum/snum

operations = {
    "+": sum,
    "-": dif,
    "*": mul,
    "/": div
}


fnum = int(input("First Number: "))
while calculating:
    for operate in operations:
        print(operate)
    operand = input("Pick Operation: ")
    snum = int(input("Second Number: "))
    function = operations[operand]
    calculating = function(fnum, snum)
    total = calculating
    print(f"{fnum} {operand} {snum} = {total}")
    decision = input("Do you want to Continue? [y]  [n]: ").lower()
    if decision == "y":
        fnum = total
    elif decision == "n":
        calculating = False

