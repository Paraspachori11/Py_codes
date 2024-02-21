#create a class C-2 d vector and use it to create another class representing a 3-d vector

class C2dVec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j

    def show2dVec(self):
        print(f" 2D Vector - : {self.icap}i+{self.jcap}j")

class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)   #observation -> mai C2dVec class k constructor ki properties inherit kara sakta hoon , naa ki values 
        self.kcap = k

    def show3dVec(self):
        print(f" 3D Vector - : {self.icap}i+{self.jcap}j+{self.kcap}k")

V2d = C2dVec(4,5)
V3d = C3dVec(1,2,11)
V2d.show2dVec()
V3d.show3dVec()