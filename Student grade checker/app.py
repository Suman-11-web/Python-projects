name=input("enter name of student::")

print("\n enter this all subjects marks below")

sub1=int(input("  enter kannada marks::"))
sub2=int(input("  enter english marks::"))
print("\n   (PCMC)")
sub3=int(input("  enter physics marks::"))
sub4=int(input("  enter chemistry marks::"))
sub5=int(input("  enter mathematics marks::"))
sub6=int(input("  enter computer science marks::"))

total=sub1+sub2+sub3+sub4+sub5+sub6
percentage=total/6

print("\n =====RESULT=====")
print("name:", name)
print("total marks:", total)
print("total percentage", percentage,"%")

if percentage>=90:
	print("Grade: A+")
	
elif percentage>=80:
	print("Grade: A")

elif percentage>=70:
	print("Grade: B")
	
elif percentage>=60:
	print("Grade: C")
	
elif percentage>=35:
	print("Grade: D")
	
else:
	print("Grade: FAIL ")


