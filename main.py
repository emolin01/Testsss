i = 0 
while i <= 10:
 print(i)
 i = i + 1



for i in range(11):
 print(i)

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print (n, 'equals', x, '*', n/x )
    break
  else: 
    print (n, 'is a prime number')


stocks_dict = {
  "AAL": "34.56",
  "IBM": "44.56",
  "AAPL": "78.56",
  "ACI": "12.45",
  "AGI": "45.11",
  "BKR": "11.99"
}
x = input("Please enter you stock symbol:")
#z = stocks_dict[x]
#print (z)
z = stocks_dict.get(x, 'Please try again inputting the correct symbol')
print (z)


print ("hello github? test test")