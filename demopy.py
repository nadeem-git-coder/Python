class Computer :
    def __init__(self, price1, ver1):
        print("-----",id(self))
        self.price = price1
        self.ver = ver1

c1= Computer(90000,8.9)
c2 = Computer(80000,7.9)
c3 = Computer(60000,5.9)
c4 =Computer(40000,1.9)
c5 = Computer(30000,1.9)



list_comp = [c1,c2,c3,c3,c4,c5]

dic_comp ={ "a1":c1,"a2":c2,"a3":c3,"a4":c4,"a5":c5,"a6": Computer(85000,9.2)

}

for k,v in dic_comp.items():
    print(v.price," ",v.ver)    