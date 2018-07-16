from pymongo import MongoClient

uri = "mongodb://admin:admin123@ds137651.mlab.com:37651/c4e19"

# 1. Connect to database
client = MongoClient(uri)

# 2. Get database
db = client.get_default_database()

# 3. Create collection (dictionary)
games = db['games']
profies = db['profies']

# # 4. Create document
# new_game = {
#     "name": "Hứng bia",
#     "des": "Best game ever"
# }

# infor = {
#     "name": "Huyen",
#     "age": 21,
#     "address": "Phu Tho"
# }

# # 5. Insert doc into collection
# games.insert_one(new_game)
# profies.insert_one(infor)

# get all documents
all_games = games.find()

print(all_games[0]['name'])

