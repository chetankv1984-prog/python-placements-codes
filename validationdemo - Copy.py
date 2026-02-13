# custom exception for length
class InValidNameLengthException(Exception):
    pass

# custom exception for characters
class InValidNameException(Exception):
    pass


def validate(fname, lname):

    # length check
    if len(fname) <= 3 or len(lname) <= 3:
        raise InValidNameLengthException("Length must be more than 3")

    # character check
    if not fname.isalpha() or not lname.isalpha():
        raise InValidNameException("Only characters allowed")

    # if valid
    print("\nValid Name")
    print("First Name:", fname)
    print("Last Name:", lname)


try:
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")

    validate(firstname, lastname)

except InValidNameLengthException as e:
    print("Error:", e)

except InValidNameException as e:
    print("Error:", e)
