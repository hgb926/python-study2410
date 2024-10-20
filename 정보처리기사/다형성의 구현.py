class Tiger:
    def speak(self):
        print("I am Tiger")

class Lion:
    def speak(self):
        print("I am Lion")

def speak(animal):
    animal.speak()

def main():
    tiger=Tiger()
    lion=Lion()
    speak(tiger)
    speak(lion)

main()