from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


def main():
    # Ask for data to store
    name = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    # Insert the user in the DB
    try:
        # Connect to the DB
        collection = MongoClient()["mathclone"]["users"]
        collection.insert({"name": name, "password": pass_hash, "email": "", "role": 2})
        print "User created."
    except DuplicateKeyError:
        print "User already present in DB."
    except Exception as e:
        print "Insert data failed with error: \n    {}.".format(e.message)

if __name__ == '__main__':
    main()
