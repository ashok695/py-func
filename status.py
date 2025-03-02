import json
def transform_data(data, filename="output22.json"):
    result = [
        {
            "mongoID": item["_id"]["$oid"],
            "id": "gocql.TimeUUID()",
            "project": "66545494bdaea319df9ba43e", 
            "category": item.get("category", ""), 
            "color": item.get("color", ""),
            "status": item.get("status", ""),
            "workItem": item.get("workItem", ""),
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
            file.write(f"        Status: {json.dumps(item['status'])},\n")
            file.write(f"        Project: {json.dumps(item['project'])},\n")
            file.write(f"        Category: {json.dumps(item['category'])},\n")
            file.write(f"        Color: {json.dumps(item['color'])},\n")
            file.write(f"        WorkItem: {json.dumps(item['workItem'])},\n")
            file.write("    }" + (",\n" if i < len(result) - 1 else "\n"))
        file.write("]\n")

    print(f"Transformed data saved to {filename}")

