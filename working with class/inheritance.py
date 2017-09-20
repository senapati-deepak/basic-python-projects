class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: "+self.last_name)
        print("Eye Color: "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, no_of_toys):
        print("Child class Constructor")
        Parent.__init__(self, last_name, eye_color)
        self.no_of_toys = no_of_toys    

    def show_info(self):
        print("Last Name: "+self.last_name)
        print("Eye Color: "+self.eye_color)
        print("No. of Toys: "+str(self.no_of_toys))    


#billy_Cyrus.Parent("Cyrus", "black")
billy_Cyrus = Parent("Cyrus","blue" )
#print(billy_Cyrus.last_name)
billy_Cyrus.show_info()
miley_cyrus = Child("Cyrus", "black", 8)
miley_cyrus.show_info()
