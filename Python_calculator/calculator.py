a=int(input("enter no1::"))
b=int(input("enter no2:"))

print("1 for addition +")
print("2 for substraction -")
print("3 for multiplication *")
print("4 for divide /")
print("5 for power **")
print("6 for modulus %")
print("7 for floor division //")
print("8 for maximum")
print("9 for minimum")
print("10 for swap")

choose=input("enter choose 1 to 4? ::")

if choose== "1":
	print("answer is ",a+b)
	
elif choose=="2":
	print("answer is", a-b)
	
elif choose=="3":
	print("answer is", a*b)
	
elif choose=="4":
	print("answer is ", a/b)
	
elif choose=="5":
	print("answer is ", a**b)
	
elif choose=="6":
    print("answer is", a % b)
   
elif choose=="7":
    print("answer is", a // b)
    
elif choose=="8":
    print("largest number is", max(a, b))
    
elif choose=="9":
    print("smallest number is", min(a, b))
    
elif choose=="10":
    a, b = b, a
    print("a =", a)
    print("b =", b)	
else:
	print("invalid input")
