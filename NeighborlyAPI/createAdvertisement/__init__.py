import azure.functions as func
import pymongo
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://cosmosud:uS3NRH8dQ9AMBhzpxaBma34cHj7XJlQAWtCDHBRehAhwDxclhCn22LoolzDyQpWECS71o9k55qIFbMOnY3sZDw==@cosmosud.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosud@" #TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['mongodbud']
            collection = database['ads']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )