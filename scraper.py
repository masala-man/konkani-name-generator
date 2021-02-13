from SPARQLWrapper import SPARQLWrapper, JSON
from wikidata.client import Client
import pymongo

# setup wikidata queries
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
query = "SELECT ?item WHERE { ?item wdt:P31 wd:Q56436498. ?item wdt:P131* wd:Q1483337. }"
client = Client()
# access db
db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["kng"]
villages = db['villages']
names = db['names']
surnames = db['surnames']
# get the data
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
# process data
for n,x in enumerate(results["results"]["bindings"]):
    item = x["item"]["value"][31:]
    entity = client.get(item, load=True)
    name = dict(entity.label)
    # clean up data
    if "en" not in name:
        name["en"] = name[list(name.keys())[0]]
    if "," in name["en"]:
        name["en"] = name["en"].split(',')[0]
    # insert into db and print
    update = villages.insert_one({"_id": n, "name": name})
    print(name["en"])

names_list = ["Prashanth", "Ajit", "Sandeep", "Sudhakar", "Subbaraya", "Devaraya", "Damodar", "Dattanand", "Nitin", "Surendra", "Mohinichandra", "Vitthal", "Govindraya", "Vitthaldas", "Sharatchandra", "Sadashiv", "Ganapathi", "Gopalkrishna", "Manjunath", "Narasimha", "Lakshman", "Pandurang", "Ranganath", "Madhav", "Anant", "Anantraya", "Mohandas", "Santhosh", "Abhishek", "Abhijeeth", "Achyuta", "Amarnath", "Raghunandan", "Raghunath", "Venkatesh", "Narayan", "Narayandas", "Aravind", "Anand"]
for n,x in enumerate(names_list):
    update = names.insert_one({"_id": n, "name": x})
surnames_list = ["Shenoy", "Kini", "Kamath", "Shanbhag", "Padiyar", "Hegde", "Rao", "Acharya", "Mallya", "Mahale", "Nayak", "Bhatt", "Joshi", "Avarsekar", "Pai", "Koppikar", "Nadkarni", "Deshprabhu", "Prabhu"]
for n,x in enumerate(surnames_list):
    update = surnames.insert_one({"_id": n, "name": x})