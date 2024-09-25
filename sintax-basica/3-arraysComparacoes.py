a = [1,2,3,4]
b = a
print(a == b)
print(a is b)
b = [1,2,3,4]
print(a == b)
print(a is b) #falso, poid a e b não são referentes ao mesmo objeto

