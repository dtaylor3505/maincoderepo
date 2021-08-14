
#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
	return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
	hours = int(input("Enter the number of hours: "))
	minutes = int(input("Enter the number of mins: "))
	seconds = int(input("Enter the number of seconds: "))

	print("Thats {} seconds".format(to_seconds(hours, minutes, seconds)))
	print ()
	cont = input("DO you want to  do another conversation? [y to continue] ")
print("Goodbye!")


