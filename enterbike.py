import time

while True:
	pass
	c=input('''
		1 for add bike
		2 for show booking
		3 for show total bike
		4 for clear booking record
		5 for payment paid
		6 for exit
		>''')
	if c=='1':
		op= open("totalbike.txt",'r')
		o=op.read()
		tl=o.split('\n')
		total=tl[0]
		t=int(total)
		print(t)
		sno=tl[2]
		op.close()

		wop=open("totalbike.txt",'w')
		i=int(input("no. of bike add ="))
		r=t+i 
		s=str(r)
		print(s)
		wop.write(s+'\n'+'\n'+sno)
		wop.close()
		print("Add seccessfully")

	elif c=='2':
		op=open("booking.txt",'r')
		sb=op.read()
		ssb=sb.split("-------------")
		for ssm in range(0,len(ssb)):
			print(ssb[ssm])
			time.sleep(0.5)
		op.close()

	elif c=='3':
		op= open("totalbike.txt",'r')
		print("Total bike is ",op.readline())

	elif c=='4':
		pasw=input("Enter Password - ")
		if pasw=="2108":
			print("clear all booking record")
			co=input('''
			1 for yes clear
			2 for no
				=''')
			if co=='1':
				op=open("booking.txt",'w')
				op.close()

			else:
				pass
		else:
			print("Incorrect Password")

	elif c=='5':
		op=open("booking.txt",'r')
		re=op.read()
		op.close()
		l=re.split("\n")
		n=input('sr no.=')
		na=""
		f=n
		p="n"
		for i in range(len(l)):
			if l[i]==f:
				na=l[i+1]
				print(na)
				print('')
				p=i
		if p=="n":
			print("name not found")
		else:
			conf=input('''
					Confirm Name
					Y/N
					   -''')
			if conf=="y" or conf=="Y":
				l[p]=n+'                      '+'paid'
				str1=""
				for ij in l:
				    str1=str1+ij+'\n'
				pr=str1.split("-------------")
				for ij in range(0,len(pr)):
					print(pr[ij])
					time.sleep(0.5)
				opw=open("booking.txt",'w')
				opw.write(str1)
				opw.close()
			elif conf=="n" or conf=="N":
				pass
			else:
				print("enter only y/Y or n/N and no paid enter try again")



	elif c=='6':
		print("Exit")
		break;

	else:
		print("enter valid code")
