import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(x=%d, y=%d)" % (self.x, self.y)

    def distance_to(self , other):
        return math.sqrt(math.pow(self.x - other.x , 2) + math.pow(self.y - other.y , 2))

def main():
    """
    :return: The Euclidean distance between two points
    """

    p1 = Point(10, 20)
    p2 = Point(20, 30)

    print("Distance between (x,y) is" , p1.distance_to(p2))

    p1.x = 20
    p1.y = 40

    print("Distance between (x,y) is" , p1.distance_to(p2))

    print("p1:" ,p1.__str__())
    print("p2:" ,p2.__str__())

if __name__ == "__main__":
    main()