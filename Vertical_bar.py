import random
def main():
    a = [2, 5, 4, 3, 0 ,2 ,3, 4,7,10]
    b =[ random.randint(0,15) for x  in range(15)]
    a.extend(b)
    print(b)
    highest = max(a)
    base = 0
    print()
    for x in range(highest, 0, -1):
        rivi = str(x).rjust(len(str(highest))+1)+" "
        base = len(rivi)
        for y in a:
            if y >= x:
                rivi += "#".ljust(len(str(highest))+1)
            else:
                rivi += " ".ljust(len(str(highest))+1)
        print(rivi)
    print(' '.ljust(len(str(highest))), end="  ")
    for v in a:
        print(str(v).ljust(len(str(highest))+1), end="")
main()