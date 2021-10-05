class Convert():
    def RadiansToDegrees(Radian):
        from math import pi
        return Radian * 180 / pi
    def DegreesToRadians(Degree):
        from math import pi
        return Degree * pi / 180


if __name__ == "__main__":
    print(Convert.DegreesToRadians(Convert.RadiansToDegrees(100)))