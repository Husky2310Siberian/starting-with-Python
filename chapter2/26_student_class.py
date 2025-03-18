class Student:
    def __init__(self , firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname

def main():
    st = Student("John", "Smith")
    # Shows existing attributes
    print(st.__dict__)
    print("Firstname:", st.firstname + "  " + "Lastname:",st.lastname)

    # Python allows adding attributes to objects at runtime.
    # Allows adding attributes dynamically because it stores them in a dictionary inside the object
    st.hello_Python = "Learn Python"
    # Now includes 'hello_Python : "Learn Python"'
    print(st.__dict__)
    print(st.hello_Python)

if __name__ == "__main__":
    main()
