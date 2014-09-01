import sys
import math
prog_name=sys.argv[0]
arg_num=sys.argv[1]

mystrx=[" zero "," one "," two "," three "," four "," five "," six "," seven "," eight "," nine "];
mystrx0=[" ten "," twenty "," thirty "," fourty "," fifty "," sixty "," seventy "," eighty "," ninty "];
mystr1x=[" ten "," eleven "," twelve "," thirteen "," fourteen "," fifteen "," sixteen "," seventeen "," eighteen "," nineteen "];

def print2(num):
	op=""
	if num<20 and num>=10:
		return (mystr1x[num-10])
	elif num<10:
		return (mystrx[num])
	elif num%10==0:
		b=int(math.floor(num/10));
		op=mystrx0[b-1] + op
		return (op)	
	else:
		a=num % 10;
		op = mystrx[a] + op;
		b=int(math.floor(num/10));
		op=mystrx0[b-1] + op
		return op
def isEven(num):
	if(num%2):
		return False
	else:
		return True

num=int(arg_num)
ndig=1;
numfordig=num;

while (int(numfordig/10))>0:
	ndig=ndig+1; 
	numfordig=int(numfordig/10);
output=""

mydict={3:"hundred",5:"thousand",4:"thousand",7:"lakhs",6:"lakhs",8:"crore",9:"crore"};


while(ndig>3):
	if(not isEven(ndig)):
		temp=int(math.floor(num/math.pow(10,(ndig-2))))
		if(temp!=0):		
			output=output+print2(temp)+mydict[ndig]
		num=(num%math.pow(10,ndig-2))	
		ndig=ndig-2
	elif(isEven(ndig)):
		temp=int(math.floor(num/math.pow(10,(ndig-1))))
		if(temp!=0):		
			output=output+print2(temp)+mydict[ndig]
		num=int(num%math.pow(10,ndig-1))
		ndig=ndig-1
if(ndig==3):
	temp=int(math.floor(num/100))
	if(temp!=0):
		output=output+mystrx[temp]+"hundred"
	ndig=ndig-1
	num=num-temp*100
if(ndig<3):
	output=output+print2(int(num))


print(output)
