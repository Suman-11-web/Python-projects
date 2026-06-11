def num_finder():
	while True:
		num=input("enter no::")
		if num.lower() =="exit":
			print("goodbye")
			break
			
		try:
			num=int(num)
			if num%2 ==0:
				print(f"{num} is an even number.")
				
			else:
				print(f"{num} is an odd number.")
				
		except ValueError:
			print("Please enter a valid integer or type 'exit'.")
			
num_finder()