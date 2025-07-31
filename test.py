class vehicle():
    def __init__(self,name,color,model):
        self.name = name
        self.color = color
        self.model =model

    def display(self):
        print(f"name : {self.name}, color : {self.color} , model : {self.model}")

class car(vehicle):
    def __init__(self,name,color,model,Speed):
        super().__init__(name,color,model)
        self.speed = Speed

    def details(self):
        super().display()
        print(f"speed : {self.speed}")

car1 = car('XUV','Black','2015',80)
car1.details()



