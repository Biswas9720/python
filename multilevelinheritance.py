class A:
    def feature1(self):
        print("this is 1 feature")

    def feature2(self):
        print("this is 1 feature")

class B():
     def feature3(self):
        print("this is 3 feature")
    
     def feature4(self):
        print("this is 3 feature")
        

class C(A,B):
    def feature5(self):
        print("This is feature 5")

c1=C()

c1.feature5()
