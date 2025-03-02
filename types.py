import json
def transform_data(data, filename="types.json"):
    result = [
        {
            "mongoID": item["_id"]["$oid"],
            "id": "gocql.TimeUUID()",
            "project": "66300cee23006656a617f366", 
            "name": item.get("name", ""),
            "type": item.get("__type", ""),
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
            file.write(f"        Name: {json.dumps(item['name'])},\n")
            file.write(f"        Project: {json.dumps(item['project'])},\n")
            file.write(f"        Type: {json.dumps(item['type'])},\n")
            file.write("    }" + (",\n" if i < len(result) - 1 else "\n"))
        file.write("]\n")

    print(f"Transformed data saved to {filename}")


