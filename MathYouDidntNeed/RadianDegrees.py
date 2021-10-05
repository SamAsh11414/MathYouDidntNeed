if __name__ == "__main__":
    from math import pi

    def RadiansToDegrees(Radian):
        return Radian * 180 / pi
    def DegreesToRadians(Degree):
        return Degree * pi / 180


    print(DegreesToRadians(RadiansToDegrees(100)))