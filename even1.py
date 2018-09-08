lower_limit=int(input("enter lower limit:"))
upper_limit=int(input("enter upper limit:"))

for i in range(lower_limit,upper_limit-1):
   if(i%2 == 0):
       print i,
