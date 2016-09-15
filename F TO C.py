def Convert2F(tempa):
	
tempa=tempa*9/5+32
	
return tempa 



def Convert2K(tempb):
	
tempb=tempb+273

return tempb

	

choice=""

while choice!="h":
	
	temp=float(input("enter a temp "))
	
	choice=input("enter f to convert to F k to convert to K of h to halt")
	
	if choice=="f":
		
		b=Convert2F (temp)
		
		u=F
	
	if choice=="k":
		
		b=Convert2K (temp)
		
		u=K

print (b,u)