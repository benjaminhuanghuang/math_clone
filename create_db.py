from pymongo import MongoClient


def main():
    try:
        # Connect to the DB
        db = MongoClient()["mathclone"]

        db.add_user('webuser', 'abc123', roles=[{'role':'readWrite','db':'mathclone'}])

        print "Database and user were created."

    except Exception as e:
        print "Create database failed with error {0}.".format(e.message)


if __name__ == '__main__':
    main()
