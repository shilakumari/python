a=20
b=20
b=30
print(id(a),id(b))

f=3.14
c=5+4j
print("real of c: ",c.real," Imaginary of c: ",c.imag)

s1="Shila"
print(type(s1))

lst=[1,2,3,4,5]
byt=bytes(lst)
print(type(byt))
ba=bytearray(lst)
print(type(ba))

r1=range(10)
range(1,10)
range(1,10,3)

t=(1,2,3,4,5)
print(type(t))#tuple

st={1,3,4,55,7}
print(type(st))#set
print(st)
fs=frozenset(st)
print(type(fs))

d={1:100,2:90,3:89}
print(type(d))#dictionay