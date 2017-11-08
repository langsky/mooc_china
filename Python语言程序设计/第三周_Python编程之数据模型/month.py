import random
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
month = input("Please input the month(1-12):")
pos = (int(month)-1)*3
print(months[pos:pos+3])
