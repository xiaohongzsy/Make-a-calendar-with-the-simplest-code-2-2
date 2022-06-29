
def a(n1,n2):
 a=[]
 for i in range(n1,n2):
  a.append(i)
 print(a)

def main():
 for j in range(1,13):
  if j in [1,3,5,7,8,10,12]:
   print(j,'月份')
   print(a(1,32))
  if j in [2]:
   print(j,'月份')
   print(a(1,29))
  if j in [4,6,9,11]:
   print(j,'月份️')
   print(a(1,31))
main()