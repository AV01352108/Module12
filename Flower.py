class Flower: #Define the flower class
    def __init__(self, name): #Define initialization function
        self.name = name #Set the name of the flower

    def grow(self): #Define grow function
        print("The " +self.name + " is growing.") #Sets for if the flower is growing

    def bloom(self): #Define bloom function
        print("The " + self.name + " is blooming.") #Sets for if the flower is blooming

def main():
    flower1 = Flower("Rose") #Set flower1 to be of class Flower with name Rose
    flower1.grow() #Set flower1 to grow
    flower1.bloom() #Set flower1 to bloom
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("Sunflower")
    flower3.grow()
    flower3.bloom()

if __name__ == "__main__":
  main()