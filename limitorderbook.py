#code for basic limit order book by suraj gurav suraj2office@gmail.com
#not using database and any UI here 
#I am dealing with only integers here but we can edit as per need...

#initalizing varables to use globally
pricenow=1  
shareowned=0
Balance =0
LimitSellPrice=1
LimitPriceBuy=1

def sell(pricenow):
	global Balance,shareowned #to make scope global
	Balance=Balance+shareowned*pricenow
	shareowned=0   #we assume that we are selling all shares
	print("your all shares got sold ! your account balance is "+str(Balance))
		


def buy(pricenow):
		global Balance,shareowned
		shareowned=shareowned+int(Balance/pricenow) #we assume that we will buy largest possible number of shares
		Balance=Balance%pricenow
		print("you got "+str(shareowned)+" Shares in your account ! your account balance is "+str(Balance))

if __name__ == '__main__':
	
	#take inputs
	trans="True"   #trans means transaction here 
	while trans=="True":
		LimitPriceBuy=int(input("Enter limiting buy price per share "))
		LimitSellPrice=int(input("Enter limiting sell price per share "))
		Balance=int(input("How much money do you have please enter "))
		pricenow=int(input("Enter price per share at this momment "))
	
		if  (pricenow==LimitSellPrice==LimitPriceBuy) :
	 		sell(pricenow)
#please note if pricenow=LimitSellPrice=LimitPriceBuy then as we are on 50% probablity on both side
#hence I have put to sell as we should not get any loss at least...
		elif (pricenow >= LimitSellPrice) :
			sell(pricenow)

		elif (pricenow <= LimitPriceBuy) :
			buy(pricenow)

		else:
			print("we will neither sell nor buy but will wait for fluctuations")
			# conditions where pricenow is in between LimitSellPrice and LimitPriceBuy
		trans=input("if you don't want to continue type False else type anything ")
		if trans=="False":
			break;
