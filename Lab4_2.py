def abc(num):
    sum = 0
    for i in range(num):
        price = int(input("รับสินค้า %d " % (i+1)))
        sum += price
    return sum
def Tax(sum):
    vat 