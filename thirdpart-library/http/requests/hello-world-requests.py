import requests

# region GET

# Send request to specific URL, then receive the response
# Note: jsonplaceholder.typicode.com provides many free restful apis
resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("<================= status =================>")

print(resp.status_code)

print("<================= status =================>")

print("<================= headers =================>")

for k, v in resp.headers.items():
    print(f"{k}: {v}")

print("<================= headers =================>")

print("<================= body =================>")

print(resp.json())

print("<================= body =================>")

# endregion
