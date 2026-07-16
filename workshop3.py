#input
shopamount = int(input("วันนี้เก็บกี่ร้าน"))

wallet = 0

for i in range(1,shopamount+1):
    sum = int(input(f"เก็บเงินจากร้านที่{i}"))
    wallet+=sum
print(wallet)


#output
