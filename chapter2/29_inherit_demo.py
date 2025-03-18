class Base:
    def __init__(self, name):
        """
        Base is a parent class (or superclass).
        :param name:
        """
        self.name = name

class Derived(Base):
    def __init__(self, name, y):
        """
        Derived inherits from Base.
        :param name:
        :param y:
        """
        super().__init__(name)  # calls the parent class constructor, so Derived gets the name attribute from Base
        self.y = y

def main():
    base = Base('BASE')
    derived = Derived('derived','DERIVED')

    print(base.name)
    print(derived.y , derived.name)

if __name__ == '__main__':
    main()