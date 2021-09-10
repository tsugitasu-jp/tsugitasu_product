from datetime import datetime, timedelta
import random

from config.settings import tsugitasu_db
import pymongo
from pymongo.errors import DuplicateKeyError

co_user = tsugitasu_db['users_user']
co_following = tsugitasu_db['users_following']
co_follower = tsugitasu_db['users_follower']

cur = co_user.find(
    projection={'uid': 1}
)

uid_lst = [obj['uid'] for obj in cur]
length = len(uid_lst)

for i in range(800):
    ran_A = random.randrange(length)
    ran_B = random.randrange(length)
    if ran_A == ran_B:
        continue

    A = uid_lst[ran_A]
    B = uid_lst[ran_B]
    time = datetime.utcnow() + timedelta(hours=9),
    dic_following = {
        "created_at": time[0],
        "_f": A, 
        "_t": B
    }
    dic_follower={
        "created_at": time[0],
        "_f": B,
        "_t": A,
    }
    try:
        co_following.insert_one(dic_following)
        co_follower.insert_one(dic_follower)
    except DuplicateKeyError:
        pass
    if i % 50 == 0:
        print(f"{i}/800")
