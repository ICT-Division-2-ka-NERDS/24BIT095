class String:
    def __init__(self, text):
        self.text = text
    def __iadd__(self, other):
        self.text += other.text
        return self
    def toLower(self):
        self.text = self.text.lower()
    def toUpper(self):
        self.text = self.text.upper()
    def display(self):
        print(self.text)


s1 = String("Hello,")
s2 = String(" You got to start with hello - James May")

s1 += s2
s1.display()       

s1.toLower()
s1.display()       

s1.toUpper()
s1.display()      