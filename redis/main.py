import redis

r= redis.Redis(host='localhost', port=6379)

# r.set("France", "Paris")
# r.set("Germany", "Berlin")

# france_capital= r.get("France")
# # print(france_capital)

# print(france_capital.decode('utf-8'))  # Output: Paris

r.mset({"Germany": "Berlin", "France": "Paris"})

print(r.get("Germany"))
print(r.get("France"))


