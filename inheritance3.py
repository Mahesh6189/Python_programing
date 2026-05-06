class A:
    def Afunc(self):
        print("this is class A")
class B(A):
    def Bfunc(self):
        print("this is class B")
class C(B):
    def Cfunc(self):
        print("this is class c")
a=A()
b=B()
c=C()
c.Bfunc()
c.Afunc()