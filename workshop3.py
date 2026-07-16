#input
shopamount = int(input("วันนี้เก็บกี่ร้าน"))
wallet = 0
#start,stop,step
for i in range(1,shopamount):
    sum = int(input(f"เก็บเงินจากร้านที่{i}เท่าไหร่"))
    wallet+=sum
print(wallet)


