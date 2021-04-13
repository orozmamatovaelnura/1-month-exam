start_deposit=int(input('Enter your starting investment : '))
final_deposit=int(input('Enter your final budget : '))
percent=int(input('Enter annual interest : '))
i=0
while start_deposit<final_deposit:
  start_deposit+=start_deposit*(percent/12)
  i+=1
  print(start_deposit)
print(i)
