import azure.functions as func
import pymongo
import os
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://cosmosud:uS3NRH8dQ9AMBhzpxaBma34cHj7XJlQAWtCDHBRehAhwDxclhCn22LoolzDyQpWECS71o9k55qIFbMOnY3sZDw==@cosmosud.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosud@" #TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['mongodbud']
            collection = database['ads']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
