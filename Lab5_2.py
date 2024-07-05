def L(A,B,C):
    F= A+B+C
    return F

    

C = int(input("ค่าคะแนนเก็บ"))
B = int(input("ค่าคะแนนสอบ"))
V = int(input("ค่าคะแนนจิตพิสัย"))
print("ค่าคะแนน %.2F" % L(C,B,V))
