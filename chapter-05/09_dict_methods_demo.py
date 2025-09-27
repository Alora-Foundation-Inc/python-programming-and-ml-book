person = {"name": "Bob", "age": 15, "city": "Denver"}
print("keys:", list(person.keys()))
print("values:", list(person.values()))
print("'name' in person:", "name" in person)
print("'phone' in person:", "phone" in person)
print("get('phone','No phone'):", person.get("phone", "No phone"))
age = person.pop("age")
print("popped age:", age)
print("now person:", person)
