"""
.. module:: mongodb_interface
   :platform: Unix
   :synopsis: A simple mongodb interface to wrap pymongo calls

.. moduleauthor:: Boris Bauermeister <Boris.Bauermeister@gmail.com>


"""
import pymongo


class MongoDBapi():
    """MongoDBapi()
    
    """
    def __init__(self):
        """MongoDBapi:__init__()

        A simple constructor to set up your MongoDBapi() class.
        The hard coded information are only to define the variables.
        ToDo: You might need to check for the mongodb address in MongoDBapi:connect()
        """
        self.user = 'testDBuser'
        self.pw = 'testDBsecret'
        self.port = '27017'
        self.host = 'mongo'
        self.db_name = 'testDB'
        self.db_collection = 'testDB'
        self.myclient = None

    def set_db_info(self, user=None,
                    pw=None,
                    port='27017',
                    host=None,
                    db_name=None,
                    db_collection=None):
        """MongoDBapi:set_db_info()

        Set up the pymongo interface with your information to connect to the
        database.

        :param user: The MongoDB user name
        :param pw: The MongoDB password (Not encrypted during handling)
        :param port: Port of the MongoDB (Standard: '27017')
        :param host: MongoDB host address
        :param db_name: Name of the MongoDB database
        :param db_collection: Name of the MongoDB collection
        """

        self.user = user
        self.pw = pw
        self.port = port
        self.host = host
        self.db_name = db_name
        self.db_collection = db_collection

    def connect(self):
        """MongoDBapi:connect()

        Init the MongoClient to connect to your selected MongoDB
        """
        self.myclient = pymongo.MongoClient(
            "mongodb://{0}:{1}@{2}:{3}/{4}".format(self.user, self.pw, self.host, self.port, self.db_name))
        self.get_collection()

    def get_collection(self):
        """MongoDBapi:get_collection()

        This function returns the collection of a chosen MongoDB
        """
        self.mydb = self.myclient[self.db_name][self.db_collection]
        return self.mydb

    def insert(self, dc):
        """MongoDBapi:insert()

        :param dc: Insert/Add another piece of information to your mongoDB
                   Collection
        """
        self.get_collection()
        self.mydb.insert_one(dc)

    def read_all(self):
        """MongoDBapi:read_all()

        A simple read_all statement which loops and print over the full collection.
        Only for testing/verification - never in production
        """
        self.get_collection()
        for i in self.mydb.find():
            print(i)

    def find_one(self, query):
        """MongoDBapi:find_one()

        Find your data by a standard pymongo query

        :param query: Allows to query for a certain MongoDB dataset selection.
                      Needs to follow the standard MongoDB query convention as a
                      dictionary:
                      query = {"name": "your_name"} or
                      query = {"$and": [{"name": "your_name"}, {"location":"your_location"}]}

        :return q: Returns a json objection with the selected data.
        """
        self.get_collection()
        q = self.mydb.find(query)
        return q

    def delete_one(self, query):
        """MongoDBapi:delete_one()

        That member function offers a way to simply remove the first dataset in the
        MongoDB collection which follows the requested query.

        :param query: Delete (the first) dataset in the MongoDB collection which follows
                      a certain query.
        :return q: Return status of the deletion process from pymongo
        """

        self.get_collection()
        q = self.mydb.delete_one(query)

    def find_one_and_update(self, id_, query):
        """MongoDBapi:find_one_and_update()

        Update a certain piece of information in your collection according to the query

        :param id_: Specify the id_ field of the MongoDB collection to match the information
                    which you like to update.
        :param query: Update the row with a dictionary (query)
        :return q: Return the update status from pymongo
        """
        self.get_collection()
        q = self.mydb.find_one_and_update({"_id": id_}, {"$set": query})
