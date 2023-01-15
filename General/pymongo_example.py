
import os
from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import pprint
load_dotenv()
URI_MONGO = os.getenv('URI_MONGO')
# connect to MongoDB, change the to reflect your own connection string
client = MongoClient(URI_MONGO)
db = client[os.getenv('DB_CLIENT')]


def search(doc, doc_filter=None):
    """
    Find document by filter
    :param doc: document of a collection
    :param doc_filter: filter

    :return:
    """
    if doc_filter is None:
        doc_filter = {}
    try:
        return db[doc].find(doc_filter)
    except Exception as ex:
        return []


def create(doc, payload: dict):
    return db[doc].insert_one(payload)


# Find
documents_res = search(doc="parcela", doc_filter={'id_odoo': 6543})
for document in documents_res:
    print(f"{pprint.pformat(document)}")

# Create
# data_parcela = {
#     "id_feature_collection": ObjectId("603fb0be9a1cfe1158e076f4"),
#     "type": "Feature",
#     "id_odoo": 15000,
#     "properties": {
#     },
#     "geometry": {
#         "type": "MultiPolygon",
#         "coordinates": []
#     }
# }
# doc_res = create(doc="parcela", payload=data_parcela)
# print(f"{pprint.pformat(str(doc_res.inserted_id))}")
