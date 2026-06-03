import numpy as np
a = np.array([1,2,3,4,5])
print(a)
#[1 2 3 4 5]


print(a.dtype,a.shape)
#int32 (5,)



b = np.array([1.0,2.0,3.0,4.0,5.0])
print(b.dtype,b.shape)
#float64 (5,)



d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d,d.shape,d.ndim)
print(d[1][1])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]] (3, 3) 2
# 5



a = np.array([1,2,3,4,5])
print(a[-1])
print(a[1:3])
print(a[::2])          #start:end:gap
print(a[a>2])
# 5
# [2 3]
# [1 3 5]
# [3 4 5]



print(d[1:,:2])
# [[4 5]
#  [7 8]]


print(d[1:2,1:])
#[[5 6]]


print(d[:,2:])
# [[3]
#  [6]
#  [9]]




a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
print(a+b)
print(a*b)
print(a**b)
print(np.sqrt(a))
print(np.exp(a))
print(np.log(a))
print(np.log2(a))
print(np.pow(a,2))
# [ 7  9 11 13 15]
# [ 6 14 24 36 50]
# [      1     128    6561  262144 9765625]
# [1.         1.41421356 1.73205081 2.         2.23606798]
# [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
# [0.         0.69314718 1.09861229 1.38629436 1.60943791]
# [0.         1.         1.5849625  2.         2.32192809]
# [ 1  4  9 16 25]




score = np.array([45,60,75,95,76,59])
print(np.where(score>60,"Pass","Fail"))
# ['Fail' 'Fail' 'Pass' 'Pass' 'Pass' 'Fail']





temps = np.array([38,22,15,41,30])
#['fever','normal','cold','fever','normal']
x = np.array([-3,-1,0,2,5])
print(np.where(temps>37,'Fever',np.where(temps<=20,'cold','normal')))
print(np.where(x>0,-x,np.where(x<0,x**2,0)))
# ['Fever' 'normal' 'cold' 'Fever' 'normal']
# [ 9  1  0 -2 -5]