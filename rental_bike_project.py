import datetime
class Bike:
    def __init__(self,s):
        self.s=s
        print('''                 

           Welcome to bike rental
            ''')

    def booking(self,q):
        rec=open("booking.txt",'a')
        name=input("Name->  ")
        if 0<=q<=self.s:
            i = self.s
            if q <= i:
                p = q * 100
                print("total rents is ", p, "rs.")
                com =   input('''Confirm booking
                    1. yes
                    2. no
                        -''')
                if com == "1" or com == "y" or com == "Y":
                    rb = i - q
                    opr=open("totalbike.txt",'r')
                    read=opr.read()
                    readl=read.split('\n')
                    sr=int(readl[2])+1
                    ssr=str(sr)
                    opr.close()
                    op=open("totalbike.txt",'w')
                    rs=str(rb)
                    op.write(rs+'\n'+'\n')
                    op.write(ssr+'\n')
                    op.close()
                    ps=str(p)
                    qs=str(q)
                    time=str(datetime.datetime.now())
                    rec.write("time- ("+time+")"'\n')
                    rec.write(ssr+'\n')
                    rec.write("Name="+ name +'\n')
                    rec.write("bike="+ qs +'\n')
                    rec.write("pay="+ ps +'\n')
                    rec.write("___________________________________" +'\n')
                    rec.write("-------------" +'\n')
                    rec.close()
                    print(time)
                    print("your sr. no. is ",sr)
                    print('''
                        Thanks for booking.
                        pay rs.''', p)
                    print('\n',"Now Avilebale bike is ", rs)

                        

                elif com == "2" or com == "n" or com == "N":
                    print("cencal booking")
                else:
                    print("pleas enter only 1 and 2")
            else:
                print("only Avilebale ", i, "bikes")

        elif q>self.s:
            print("you request quantity not avilebale '\n' only ",self.s , "bike avilebale")

        else:
            print("error")

    def avi(self,q=0):
        self.s=self.s-q
        print("Avilebale bike is ", self.s)


while True:
    op=open("totalbike.txt",'r')
    r=op.readline()
    ri=int(r)


    obj = Bike(ri)
    ui = input('''
        1. Show Avilebale bikes
        2. booking start
        3. exit
           -''')
    if ui == '1':
        obj.avi()
    elif ui == '2':
        q = input("no. of bike for booking (note- 100rs.@bike)- ")
        q.lower()
        if 'a' in q or 'b' in q or 'c' in q or 'd' in q or 'e' in q or 'f' in q or 'g' in q or 'h' in q or 'i' in q or 'j' in q or 'k' in q or 'l' in q or 'm' in q or 'n' in q or 'o' in q or 'p' in q or 'q' in q or 'r' in q or 's' in q or 't' in q or 'u' in q or 'v' in q or 'w' in q or 'x' in q or 'y' in q or 'z' in q:
            print("Enter only number")
        else:
            obj.booking(int(q))
    elif ui == '3':
        ec = input('''
            EXIT
                1. yes
                2. no
                    -''')
        if ec == "1" or ec=='Y' or ec=="y":
            print("exit")
            break
        elif ec == '2' or ec == "n" or ec == "N":
            pass
        else:
            print("enter only 1 or 2 ")
    else:
        print("enter only 1,2 or 3")

