import pymongo


class MongoDBapi():
    def __init__(self):
        #hard coded quantities!
        #we can improve here...
        self.user='testDBuser'
        self.pw='testDBsecret'
        self.port='27017'
        self.host='mongo'

        self.myclient = None

    def connect(self):
        self.myclient = pymongo.MongoClient("mongodb://{0}:{1}@{2}:{3}/testDB".format(self.user, self.pw, self.host, self.port))
        self.get_collection()

    def get_collection(self):
        self.mydb = self.myclient["testDB"].testDB
        return self.mydb

    def insert(self, dc):
        self.get_collection()
        self.mydb.insert_one(dc)

    def read_all(self):
        self.get_collection()
        for i in self.mydb.find():
            print(i)

    def find_one(self, query):
        self.get_collection()
        q = self.mydb.find(query)
        return q

    def delete_one(self, query):
        self.get_collection()
        q = self.mydb.delete_one(query)

    def find_one_and_update(self, id_, query):
        self.get_collection()
        q = self.mydb.find_one_and_update( {"_id": id_}, {"$set": query} )

    def verify(self):
        self.get_collection()
        for i in self.mydb.find():
            print(i)
