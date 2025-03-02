import json
def transform_data(data, filename="output.json"):
    result = [
        {
            "mongoID": item["_id"]["$oid"],
            "id": "gocql.TimeUUID()",
            "orderID": item.get("orderID", ""),
            "title": item.get("subPhaseName", ""),
            "phase": item["phase"]["$oid"] if isinstance(item.get("phase"), dict) and "$oid" in item["phase"] else item.get("phase", ""),
            # "type": item["type"][0]["$oid"] if isinstance(item.get("type"), list) and len(item["type"]) == 1 and isinstance(item["type"][0], dict) and "$oid" in item["type"][0] else "",
            "role": item["role"][0]["$oid"] if isinstance(item.get("role"), list) and len(item["role"]) == 1 and isinstance(item["role"][0], dict) and "$oid" in item["role"][0] else "",
            "taskType": item["taskType"][0]["$oid"] if isinstance(item.get("taskType"), list) and len(item["taskType"]) == 1 and isinstance(item["taskType"][0], dict) and "$oid" in item["taskType"][0] else "",
            "workstream": item["workstream"][0]["$oid"] if isinstance(item.get("workstream"), list) and len(item["workstream"]) == 1 and isinstance(item["workstream"][0], dict) and "$oid" in item["workstream"][0] else "",
            "project": "66300cee23006656a617f366", 
            "ganttDuration": item.get("ganttDuration", 0), 
            "delayLog": item.get("delayLog", ""), 
            "constraintDate": item.get("constraintDate", ""),
            "constraintType": item.get("constraintType", ""),  
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
            file.write(f"        OrderID: {json.dumps(item['orderID'])},\n")
            file.write(f"        Phase: {json.dumps(item['phase'])},\n")
            file.write(f"        Role: {json.dumps(item['role'])},\n")
            file.write(f"        TaskType: {json.dumps(item['taskType'])},\n")
            file.write(f"        Workstream: {json.dumps(item['workstream'])},\n")
            file.write(f"        Project: {json.dumps(item['project'])},\n")
            file.write(f"        GanttDuration: {json.dumps(item['ganttDuration'])},\n")
            file.write(f"        Title: {json.dumps(item['title'])},\n")
            file.write(f"        DelayLog: {json.dumps(item['delayLog'])},\n")
            file.write(f"        ConstraintDate: {json.dumps(item['constraintDate'])},\n")
            file.write(f"        ConstraintType: {json.dumps(item['constraintType'])},\n")
            file.write("    }" + (",\n" if i < len(result) - 1 else "\n"))
        file.write("]\n")

    print(f"Transformed data saved to {filename}")




