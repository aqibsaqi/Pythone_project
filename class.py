class person:
    def __init__(self,nam,age,sal):
        self.name=nam
        self.age=age
        self.salary=sal
    def info(self):
        print(f"i am {self.name} ,i am {self.age}old and my income{self.salary}$")

p1=person("saqi",22,30)
p1.info()
