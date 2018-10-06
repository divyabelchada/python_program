wc=float(input("enter weight charge:"))
dc=float(input("enter distance charge:"))
if wc>0 and wc<=10:
    wc=wc*0.75
    print("weight charge is:", (wc))
    charge=wc
elif wc>10 and wc<=15:
    wc=wc*0.85
    print("weight charge is:",(wc))
    charge=wc
elif wc>15 and wc<=20:
    wc=wc*0.95
    print("weight charge is:",(wc))
    charge=wc
else:
    print("not allowed")

    
if  dc>0 and dc<=50:
    dc=dc*0.07
    print("distance charge:",(dc))
    dis_charge= dc
elif dc>50 and dc<=100:
   dc= dc*0.06
   print("distance charge:",(dc))
   dis_charge=dc
elif dc>100 and dc<=200:
    dc=dc*0.05
    print("distance charge:",(dc))
    dis_charge=dc
elif     dc>200 and dc<=500:
    dc=dc*0.04
    print("distance charge:",(dc))
    dis_charge=dc
else:
    print("not allowed")

print( dis_charge+charge)

    



    
