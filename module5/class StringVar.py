class StringVar(str):
    def __init__(self, string='Привет!!!'):
        self.string = string

    def get(self):
        return self.string

    def set(self, value):
        self.string = value


str1 = StringVar()
print(str1.string)
print(str1.get())
str1.set('Hello')
print(str1.get())
