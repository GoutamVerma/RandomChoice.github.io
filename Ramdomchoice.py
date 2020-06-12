import random

def select():
    member=["mohit","praful","samarth"]
    members=["drakshi","avadhi","mansi"]
    first=random.choice(member)
    second=random.choice(members)
    return first,second


print(select())
