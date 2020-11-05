#Input 3 buah bilangan, menggunakan statement if
print ( "Menentukan bilangan terbesar dari 3 bilangan")
a = int ( input ( "Masukkan bilangan A: " ))
b = int ( input ( "Masukkan bilangan B: " ))
c = int ( input ( "Masukkan bilangan C: " ))
if a > b and a > c :
  print ( "Jadi bilangan terbesarnya adalah =" , a )
elif b > a and b > c :
    print ( "Jadi bilangan terbesarnya adalah =", b )
else :
    print ( "Jadi bilangan terbesarnya adalah =", c )