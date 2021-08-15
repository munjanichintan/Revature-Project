from pymongo import MongoClient
import pprint
from dateutil import parser

client = MongoClient()

db = client.restaurants
collection = db.data

print(db.list_collection_names())

# 1. Write a MongoDB query to display all the documents in the collection restaurants.
# for i in collection.find().limit(5):
#     pprint.pprint(i)

# 2. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
# for i in collection.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1}):
#     pprint.pprint(i)

# 3. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.
# for i in collection.find({}, {'_id': 0, 'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1}):
#     pprint.pprint(i)

# 4. Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.
# for i in collection.find({}, {'_id': 0, 'restaurant_id': 1, 'name': 1, 'borough': 1, 'address.zipcode': 1}):
#     pprint.pprint(i)

# 5. Write a MongoDB query to display all the restaurant which is in the borough Bronx.
# for i in collection.find({'borough': 'Bronx'}):
#     pprint.pprint(i)

# 6. Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.
# for i in collection.find({'borough': 'Bronx'}).limit(5):
#     pprint.pprint(i)

# 7. Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.
# for i in collection.find({'borough': 'Bronx'}).skip(5).limit(5):
#     pprint.pprint(i)

# 8. Write a MongoDB query to find the restaurants who achieved a score more than 90.
# for i in collection.find({'grades.score': {'$gt': 90}}):
#     pprint.pprint(i)

# 9. Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.
# for i in collection.find({'grades': {'$elemMatch': {'score': {'$gt': 80 , '$lt': 100}}}}):
#     pprint.pprint(i)

# 10. Write a MongoDB query to find the restaurants which locate in longitude value less than -95.754168.Go to the editor
# for i in collection.find({'address.coord.0': {'$lt': -95.754168}}):
#     pprint.pprint(i)

# 11. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168.
# for i in collection.find({'$and': [{'cuisine': {'$ne': 'American '}}, {'grades.score': {'$gt': 70}}, {'address.coord.1': {'$gt': -65.754168}}]}):
#     pprint.pprint(i)

# 12. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
# for i in collection.find({'cuisine': {'$ne': 'American '}, 'grades.score': {'$gt': 70}, 'address.coord.0': {'$lt': -65.754168}}):
#     pprint.pprint(i)

# 13. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.
# for i in collection.find({'cuisine': {'$ne': 'American '}, 'grades.grade': {'$eq': 'A'}, 'borough': {'$ne': 'Brooklyn'}}).sort('cuisine', -1):
#     pprint.pprint(i)

# 14. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name.
# for i in collection.find({'name': {'$regex': '^Wil.*'}}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, '_id': 0}):
#     pprint.pprint(i)

# 15. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'ces' as last three letters for its name.
# for i in collection.find({'name': {'$regex': '.*ces$'}}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, '_id': 0}):
#     pprint.pprint(i)

# 16. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Reg' as three letters somewhere in its name.
# for i in collection.find({'name': {'$regex': 'Reg'}}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, '_id': 0}):
#     pprint.pprint(i)

# 17. Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish.
# for i in collection.find({'borough': {'$eq': 'Bronx'}, 'cuisine': {'$in': ['American ', 'Chinese']}}):
#     pprint.pprint(i)

# 18. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn.
# for i in collection.find({'borough': {'$in': ['Staten Island', 'Queens', 'Bronxor Brooklyn']}}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, '_id': 0}):
#     pprint.pprint(i)

# 19. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.
# for i in collection.find({'borough': {'$nin': ['Staten Island', 'Queens', 'Bronxor Brooklyn']}}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, '_id': 0}):
#     pprint.pprint(i)

# 20. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which achieved a score which is not more than 10.
# for i in collection.find({'grades': {'$elemMatch': {'score': {'$lte': 10}}}}, {'grades.score': 1}):
#     pprint.pprint(i)

# 21. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinese' or restaurant's name begins with letter 'Wil'.
# for i in collection.find({'$or': [{'cuisine': {'$nin': ['American ', 'Chinese']}}, {'name': {'$regex': '$Wil.*'}}]}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, '_id': 0}):
#     pprint.pprint(i)

# 22. Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates..
# for i in collection.find({'grades': {'$elemMatch': {'date': parser.isoparse("2014-08-11T00:00:00Z"), 'score': 11, 'grade': 'A'}}}, {'restaurant_id': 1, 'name': 1, 'grades': 1, '_id': 0}):
#     pprint.pprint(i)

# 23. Write a MongoDB query to find the restaurant Id, name and grades for those restaurants where the 2nd element of grades array contains a grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z".
# for i in collection.find({'grades.1.date': parser.isoparse("2014-08-11T00:00:00Z"), 'grades.1.score': 9, 'grades.1.grade': 'A'}, {'restaurant_id': 1, 'name': 1, 'grades': 1, '_id': 0}):
#     pprint.pprint(i)

# 24. Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52..
# for i in collection.find({'address.coord.1': {'$gt': 42, '$lte': 52}}, {'_id': 0, 'restaurant_id': 1, 'name': 1, 'address': 1}):
#     pprint.pprint(i)

# 25. Write a MongoDB query to arrange the name of the restaurants in ascending order along with all the columns.
# for i in collection.find().sort('name', 1):
#     pprint.pprint(i)

# 26. Write a MongoDB query to arrange the name of the restaurants in descending along with all the columns.
# for i in collection.find().sort('name', -1):
#     pprint.pprint(i)

# 27. Write a MongoDB query to arranged the name of the cuisine in ascending order and for that same cuisine borough should be in descending order.
# for i in collection.find().sort([('cuisine', 1), ('borough', -1)]):
#     pprint.pprint(i)

# 28. Write a MongoDB query to know whether all the addresses contains the street or not.
# print(collection.count_documents({'address.street': {'$exists': True}}))

# 29. Write a MongoDB query which will select all documents in the restaurants collection where the coord field value is Double.
# for i in collection.find({'address.coord': {'$type': 1}}):
#     pprint.pprint(i)

# 30. Write a MongoDB query which will select the restaurant Id, name and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.
# for i in collection.find({'grades': {'$elemMatch': {'score': {'$mod': [7, 0]}}}}, {'_id': 0, 'name': 1, 'restaurant_id': 1, 'grades': 1}):
#     pprint.pprint(i)

# print(collection.count_documents({'grades': {'$elemMatch': {'score': {'$mod': [7, 0]}}}}))

# 31. Write a MongoDB query to find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which contains 'mon' as three letters somewhere in its name.
# for i in collection.find({'name': {'$regex': 'mon'}}, {'name': 1, '_id': 0, 'borough': 1, 'address.coord': 1, 'cuisine': 1}):
#     pprint.pprint(i)

# 32. Write a MongoDB query to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants which contain 'Mad' as first three letters of its name.
# for i in collection.find({'name': {'$regex': '^Mad.*'}}, {'name': 1, '_id': 0, 'borough': 1, 'address.coord': 1, 'cuisine': 1}):
#     pprint.pprint(i)