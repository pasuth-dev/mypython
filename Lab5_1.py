def Fa(C):
    F= (9/5)*C+32
    return F

def K(C):
    K=  (C+273.75)
    return C


C = int(input("รับองศาเซลเซียส"))
print("องศาฟาเรนหาย %.2F" % Fa(C))
print("เควิน %.2F" % K(C))