# #input
# goal = 500
# shopamount = int(input("เก็บมาแล้วกี่ร้าน"))
# income = int(input("เก็บมาเท่าไหร่ละ"))
# wallet = 0
# shopnote = 0
# #output
# while wallet <=goal:
#     sum = int(input(f"เก็บเงินมาทั้งหมด{shopamount}ร้าน"))
#     wallet+=sum
#     shopnote +=1
# print("จำนวนร้านที่เก็บ =",shopamount)
# print("จำนวนเงินที่เก็บ =",sum)

bank = 0
shopcount = 0
goal = 50000

while bank <= goal:
    recieve = int(input("ยอดที่เก็บได้จากร้านนี้ :"))
    bank += recieve
    shopcount += 1
    
print("จำนวนร้านค้า",shopcount)
print("ยอดเงินรวม",bank)

    
