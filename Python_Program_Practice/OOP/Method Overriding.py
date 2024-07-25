class iPhone6:
    def home(self):
        print("Home is Pressed")

class iPhoneX(iPhone6):
    def home(self):
        print("Home is touched")
        super().home()


six = iPhone6()
six.home()

ten = iPhoneX()
ten.home()
