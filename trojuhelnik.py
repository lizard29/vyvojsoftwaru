import math

def delkaStrany(x1, y1, x2, y2):
    str1 = x2-x1
    str2 = y2-y1
    str1 = math.pow(2, str1)
    str2 = math.pow(2, str2)
    st = math.sqrt(str1+str2)
    return st

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
print("Délka strany a: " + str(round(stra, 2)) + " cm")
strb = delkaStrany(ax, ay, cx, cy)
print("Délka strany b: " + str(round(strb, 2)) + " cm")
strc = delkaStrany(bx, by, ax, ay)
print("Délka strany c: " + str(round(strc, 2)) + " cm")
if stra + strb > strc and strb + strc > stra and strc + stra > strb:
    print("Trojúhelník je sestrojitelný")
else:
    print("Trojúhelník není sestrojitelný")
obvod = stra + strb + strc
print("Obvod trojúhelníku je " + str(round(obvod, 2)) + " cm")
s = (stra + strb + strc) / 2
m = s * (s - stra) * (s - strb) * (s - strc)
if m >= 0:
    obsah = math.sqrt(m)
    print("Obsah trojúhelníku je " + str(round(obsah, 2)) + " cm")
else:
    print("Obsah nelze vypočítat (záporné číslo pod odmocninou)")
if math.pow(2, stra) == math.pow(2, strb) + math.pow(2, strc) or math.pow(2, strb) == math.pow(2, strc) + math.pow(2, stra) or math.pow(2, strc) == math.pow(2, stra) + math.pow(2, strb):
    print("Trojúhelník je pravoúhlý")
else:
    print("Trojúhelník není pravoúhlý")
    
