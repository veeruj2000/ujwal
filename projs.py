code=input("Enter the item you would like to order: (eg:Hyderabadi Biryani)")
file=open("fooddescription.txt","r")
for line in file:
	data=line.split(";")
	restaurant=data[0]
	item_Description=data[1]
	item_Price=float(data[2])
if restaurant== code:
	print(restaurant+"_"+item_Description+"_$"+str(item_Price))
	code=input("Enter another code or X to exit")