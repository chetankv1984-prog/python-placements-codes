# Custom Exception for invalid length
class InValidNameLengthException(Exception):
    def __init__(self, message="Length must be more than 3"):
        self.message = message
        super().__init__(self.message)

# Custom Exception for invalid characters
class InValidNameException(Exception):
    def __init__(self, message="Only characters are allowed"):
        self.message = message
        super().__init__(self.message)

# Validation function
def validate(firstname, lastname):

    # Check length
    if len(firstname) <= 3 or len(lastname) <= 3:
        raise InValidNameLengthException()

    # Check only alphabets
    if not firstname.isalpha() or not lastname.isalpha():
        raise InValidNameException()

    # If all valid
    print("\nValidation Successful")
    print("First Name:", firstname)
    print("Last Name:", lastname)


# Main program
try:
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")

    validate(fname, lname)

except InValidNameLengthException as e:
    print("Error:", e)

except InValidNameException as e:
    print("Error:", e)

except Exception as e:
    print("Something went wrong:", e)
