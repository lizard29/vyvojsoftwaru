import math

def delkaStrany(x1, y1, x2, y2):
    """Calculate the length of a side of a triangle
    
    Return the length of the side
    >>> delkaStrany(10, 10, 5, 5) == 7.07
    True
    >>> delkaStrany(6, 4, 2, 3)
    4.12
    """
    str1 = x2-x1
    str2 = y2-y1
    str1 = math.pow(str1, 2)
    str2 = math.pow(str2, 2)
    st = round(math.sqrt(str1+str2), 2)
    return st

def getObvod(a, b, c):
    o = a + b + c
    return o

def getObsah(a, b, c):
    s = (a + b + c) / 2
    m = s * (s - a) * (s - b) * (s - c)
    if m >= 0:
        obs = round(math.sqrt(m), 2)
    else:
        obs = -1
    return obs

def jeSestrojitelny(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False
    
def jePravouhly(a, b, c):
    if math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2) or math.pow(b, 2) == math.pow(c, 2) + math.pow(a, 2) or math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2):
        return True
    else:
        return False

def trojuhelnik():
    print("Zadejte souřadnice pro bod A na ose X: ")
    ax = float(input())
    print("Zadejte souřadnice pro bod A na ose Y: ")
    ay = float(input())
    print("Zadejte souřadnice pro bod B na ose X: ")
    bx = float(input())
    print("Zadejte souřadnice pro bod B na ose Y: ")
    by = float(input())
    print("Zadejte souřadnice pro bod C na ose X: ")
    cx = float(input())
    print("Zadejte souřadnice pro bod C na ose Y: ")
    cy = float(input())
    stra = delkaStrany(cx, cy, bx, by)
    print("Délka strany a: " + str(stra) + " cm")
    strb = delkaStrany(ax, ay, cx, cy)
    print("Délka strany b: " + str(strb) + " cm")
    strc = delkaStrany(bx, by, ax, ay)
    print("Délka strany c: " + str(strc) + " cm")
    if jeSestrojitelny(stra, strb, strc):
        print("Trojúhelník je sestrojitelný")
    else:
        print("Trojúhelník není sestrojitelný")
    obvod = getObvod(stra, strb, strc)
    print("Obvod trojúhelníku je " + str(obvod) + " cm")
    obsah = getObsah(stra, strb, strc)
    if obsah >= 0:
        print("Obsah trojúhelníku je " + str(obsah) + " cm")
    else:
        print("Obsah nelze vypočítat (záporné číslo pod odmocninou)")
    if jePravouhly(stra, strb, strc):
        print("Trojúhelník je pravoúhlý")
    else:
        print("Trojúhelník není pravoúhlý")
    
