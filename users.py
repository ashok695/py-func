import json
def transform_data(data, filename="user.json"):
    result = [
        {
            "mongoID": item["_id"]["$oid"],
            "id": "gocql.TimeUUID()",
            "project": "66300cee23006656a617f366", 
            "fullname":item["fullName"],
            "email":item["email"],
            "team":item["team"]["$oid"],
            "role":item["role"]["$oid"]
        }
        for item in data
    ]
    # Writing manually formatted JSON without quotes for keys
    with open(filename, "w") as file:
        file.write("[\n")
        for i, item in enumerate(result):
            print(item)
            file.write("    {\n")
            file.write(f"        ID: {json.dumps(item['id'])},\n")
            file.write(f"        MongoID: {json.dumps(item['mongoID'])},\n")
            file.write(f"        Project: {json.dumps(item['project'])},\n")
            file.write(f"        FullName: {json.dumps(item['fullname'])},\n")
            file.write(f"        Email: {json.dumps(item['email'])},\n")
            file.write(f"        Team: {json.dumps(item['team'])},\n")
            file.write(f"        Role: {json.dumps(item['role'])},\n")
            file.write("    }" + (",\n" if i < len(result) - 1 else "\n"))
        file.write("]\n")

    print(f"Transformed data saved to {filename}")


