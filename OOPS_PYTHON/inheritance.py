'''class Gf:    # grandfather
    def name(self,name):
        self.n=name
class P(Gf):
    def __init__(self, p_name):
        self.x=p_name
    def p_properties(self,home,bank):
        self.h=home
        self.b=bank
        print(self.h)
        print(self.b)
class c(P):
    def c_properties(self,qualities):
        self.q=qualities
        self.p_properties("farrukhabad","PNB")
#        print(self.h)
#        print(self.b)
        print(self.q)
        print(self.x)
        self.name("Pragati Gupta")
        print(self.n)
obj=c("PRAGATI")
#obj.p_properties("fbd","pnb")
obj.c_properties("B.Tech")
'''

class Gf:
    def name(self,name):
        self.n=name
        print(self.n)
class F(Gf):
    def f_name(self, f_name):
        self.m=f_name
        print(self.m)
class C(F):
    def c_name(self, c_name):
        self.o=c_name
        print(self.o)
obj =C()
obj.name("RAM PRAKASH GUPTA")
obj.f_name("AJAY GUPTA")
obj.c_name("PRAGATI GUPTA")