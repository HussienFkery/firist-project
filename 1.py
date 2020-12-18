print("Welcome To My Store :)")
case = {
    "Master Cosmos C700P": 322,
    "Corsair Carbide 275R": 80,
    "Phanteks Evolv X": 226,
    "NZXT H200i": 100,
    "Cooler Master Silencio S600": 328,
    "Corsair Obsidian 1000D": 500,
    "be quiet! Dark Base Pro 900": 258,
    "Lian-Li PC-011 Dynamic": 150,
    "Zalman S3 ATX Mid Tower Computer PC Case": 40,
    "Zalman T6 ATX Mid Tower Compute": 40,
    "AeroCool Cylon RGB Mid Tower": 50,
    "Cooler Master MasterBox Q300L Micro-ATX Tower": 45,
    "Cooler Master N200 - Mini Tower": 45,
    "Fractal Design Core 1100 - Mini Tower": 30,
    "Thermaltake Versa H22 Black ATX Mid Tower": 50
}
ram = {
    "4 gb ram DDR3": 21,
    "8 gb ram DDR3": 54,
    "8 gb ram DDR4 RGB": 130,
    " gb ram DDR4 RGB16": 180
}
graphiccard = {
    "Nivedia 750 ti 2gb": 90,
    "Asus GTX 150 TI 4GB": 180,
    "NIVIDIA RTX 2060": 340,
    "NIVIDIA RTX 3060": 400
}
harddisk = {
    "Wd HDD 500GB": 18,
    "Wd HDD 1TB": 43,
    "Wd HDD 1 TB + SSD 256 GB": 85,
    "Wd HDD 2 TB + SSD 500 GB": 220
}
motherboard = {
    "Asus ROG Maximus XII HERO": 790,
    "MSI MPG Z390M Gaming Edge AC": 450,
    "HP Pro 3400 MT 657002-001 H-Coupertino2": 77,
    "Dell F3KHR OptiPlex 9010": 88
}
price = [0, 0, 0, 0, 0]
print("firist step chose yuure case by number :")
print("""--> Case High-end <--
1- Master Cosmos C700P
2- Corsair Carbide 275R
3- Phanteks Evolv X
4- NZXT H200i
5- Cooler Master Silencio S600
6- Corsair Obsidian 1000D
7- be quiet! Dark Base Pro 900
8- Lian-Li PC-011 Dynamic""")
print("""--> Case Low-end <--
9- Zalman S3 ATX Mid Tower Computer PC Case
10- Zalman T6 ATX Mid Tower Compute
11- AeroCool Cylon RGB Mid Tower
12- Cooler Master MasterBox Q300L Micro-ATX 
13- Cooler Master N200 - Mini Tower 
14- Fractal Design Core 1100 - Mini Tower
15- Thermaltake Versa H22 Black ATX Mid """)
casenum = (input("enter youre case ==>"))
if casenum == "1":
    print(case.get("Master Cosmos C700P"))
elif casenum == "2":
    print(case.get("Corsair Carbide 275R"))
elif casenum == "3":
    print(case.get("Phanteks Evolv X"))
elif casenum == "4":
    print(case.get("NZXT H200i"))
elif casenum == "5":
    print(case.get("Cooler Master Silencio S600"))
elif casenum == "6":
    print(case.get("Corsair Obsidian 1000D"))
elif casenum == "7":
    print(case.get("be quiet! Dark Base Pro 900"))
elif casenum == "8":
    print(case.get("Lian-Li PC-011 Dynamic"))
elif casenum == "9":
    print(case.get("Zalman S3 ATX Mid Tower Computer PC Case"))
elif casenum == "10":
    print(case.get("Zalman T6 ATX Mid Tower Compute"))
elif casenum == "11":
    print(case.get("AeroCool Cylon RGB Mid Tower"))
elif casenum == "12":
    print(case.get("Cooler Master MasterBox Q300L Micro-ATX Tower"))
elif casenum == "13":
    print(case.get("Cooler Master N200 - Mini Tower"))
elif casenum == "14":
    print(case.get("Fractal Design Core 1100 - Mini Tower"))
elif casenum == "15":
    print(case.get("Thermaltake Versa H22 Black ATX Mid Tower"))
else:
    print("how you wont get pc except case tell me howwwwwwwwwwwwww???",)

print("""--> chose youre mather bord <--
----> High-end <----
1- Asus ROG Maximus XII HERO
2- MSI MPG Z390M Gaming Edge AC
---->Low-end <----
3- HP Pro 3400 MT 657002-001 H-Coupertino2
4- Dell F3KHR OptiPlex 9010""")
matherboard = input("enter the num of motherboard :")
if matherboard == "1":
    print(motherboard.get("Asus ROG Maximus XII HERO"))
elif matherboard == "2":
    print(motherboard.get("MSI MPG Z390M Gaming Edge AC"))
elif matherboard == "3":
    print(motherboard.get("HP Pro 3400 MT 657002-001 H-Coupertino2"))
elif matherboard == "4":
    print(motherboard.get("Dell F3KHR OptiPlex 9010"))
else:
    print("how you wont PC except motherboard!! \nyou can live except youre mother??")
print("""chose youre ram 
---> High-end <---
1- 4 gb ram DDR3  
2- 8 gb ram DDR3
---> Low-end <---
3- 8 gb ram DDR4 RGB
4- 16 gb ram DDR4 RGB""")
rams = input("enter youre ram :")
if rams == "1":
    print(ram.get("4 gb ram DDR3"))
elif rams == "2":
    print(ram.get("8 gb ram DDR3"))
elif rams == "3":
    print("8 gb ram DDR4 RGB")
elif rams == "4":
    print(ram.get(" gb ram DDR4 RGB16"))
else:
    print("As you like :)")
hard = input("enter youre hard :")
if hard == "1":
    print(harddisk.get("Wd HDD 500GB"))
elif hard == "2":
    print(harddisk.get("Wd HDD 1TB"))
elif hard == "3":
    print(harddisk.get("Wd HDD 1 TB + SSD 256 GB"))
elif hard == "4":
    print(harddisk.get("Wd HDD 2 TB + SSD 500 GB"))
else:
    print("yasta 5od el hard mn 3andena ma3lesh ;)")
graphic = input("enter youre graohic card :")
if graphic == "1":
    print(graphiccard.get("Nivedia 750 ti 2gb"))
elif graphic == "2":
    print(graphiccard.get("Asus GTX 150 TI 4GB"))
elif graphic == "3":
    print(graphiccard.get("NIVIDIA RTX 2060"))
elif graphic == "4":
    print(graphiccard.get("NIVIDIA RTX 3060"))
