import json
def transform_data(data, filename="output.json"):
    result = [
        {
            "mongoID": item["_id"]["$oid"],
            "id": "gocql.TimeUUID()",  # Generating UUID for ScyllaDB
            "orderID": item.get("orderID", ""),
            "title": item.get("title", ""),
            "status": item.get("status", {}).get("$oid", "") if isinstance(item.get("status"), dict) else item.get("status", ""),  # Handle empty string case
            "phase": item["phase"]["$oid"] if isinstance(item.get("phase"), dict) and "$oid" in item["phase"] else item.get("phase", ""),
            "subPhaseID": item["subPhaseID"]["$oid"] if isinstance(item.get("subPhaseID"), dict) and "$oid" in item["subPhaseID"] else item.get("subPhaseID", ""),
            "assignedTo": item.get("assignedTo", {}).get("$oid", "") if isinstance(item.get("assignedTo"), dict) else "", 
            "priority": item.get("priority", {}).get("$oid", "") if isinstance(item.get("priority"), dict) else "", 
            "refTaskID": item.get("refTaskID", {}).get("$oid", "") if isinstance(item.get("refTaskID"), dict) else item.get("refTaskID", ""),  # Handle empty string case
           "type": item["type"][0]["$oid"] if isinstance(item.get("type"), list) and len(item["type"]) == 1 and isinstance(item["type"][0], dict) and "$oid" in item["type"][0] else "",
            "plannedFrom": item["plannedFrom"]["$date"] if isinstance(item.get("plannedFrom"), dict) and "$date" in item["plannedFrom"] else item.get("plannedFrom", ""),
            "plannedTo": item["plannedTo"]["$date"] if isinstance(item.get("plannedTo"), dict) and "$date" in item["plannedTo"] else item.get("plannedTo", ""),
            "startedOn": item["startedOn"]["$date"] if isinstance(item.get("startedOn"), dict) and "$date" in item["startedOn"] else item.get("startedOn", ""),
            "completedOn": item["completedOn"]["$date"] if isinstance(item.get("completedOn"), dict) and "$date" in item["completedOn"] else item.get("completedOn", ""),
            "activePercentage": round(float(item["activePercentage"]), 2) if item.get("activePercentage") not in [None, ""] else 0.0,
            "role": item["role"][0]["$oid"] if isinstance(item.get("role"), list) and len(item["role"]) == 1 and isinstance(item["role"][0], dict) and "$oid" in item["role"][0] else "",
            "taskType": item["taskType"][0]["$oid"] if isinstance(item.get("taskType"), list) and len(item["taskType"]) == 1 and isinstance(item["taskType"][0], dict) and "$oid" in item["taskType"][0] else "",
            "workstream": item["workstream"][0]["$oid"] if isinstance(item.get("workstream"), list) and len(item["workstream"]) == 1 and isinstance(item["workstream"][0], dict) and "$oid" in item["workstream"][0] else "",
            "project": "66300cee23006656a617f366", 
            "ganttDuration": item.get("ganttDuration", 0),  # Extracting ganttDuration, default ""
            "delayLog": item.get("delayLog", ""),  # Extracting delayLog, default ""
            "constraintDate": item["constraintDate"]["$date"] if isinstance(item.get("constraintDate"), dict) and "$date" in item["constraintDate"] else item.get("constraintDate", ""),
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
            file.write(f"        Status: {json.dumps(item['status'])},\n")
            file.write(f"        Phase: {json.dumps(item['phase'])},\n")
            file.write(f"        SubPhaseID: {json.dumps(item['subPhaseID'])},\n")
            file.write(f"        AssignedTo: {json.dumps(item['assignedTo'])},\n")
            file.write(f"        RefTaskID: {json.dumps(item['refTaskID'])},\n")
            file.write(f"        Type: {json.dumps(item['type'])},\n")
            file.write(f"        PlannedFrom: {json.dumps(item['plannedFrom'])},\n")
            file.write(f"        PlannedTo: {json.dumps(item['plannedTo'])},\n")
            file.write(f"        StartedOn: {json.dumps(item['startedOn'])},\n")
            file.write(f"        CompletedOn: {json.dumps(item['completedOn'])},\n")
            file.write(f"        ActivePercentage: {json.dumps(item['activePercentage'])},\n")
            file.write(f"        Role: {json.dumps(item['role'])},\n")
            file.write(f"        TaskType: {json.dumps(item['taskType'])},\n")
            file.write(f"        Workstream: {json.dumps(item['workstream'])},\n")
            file.write(f"        Project: {json.dumps(item['project'])},\n")
            file.write(f"        GanttDuration: {json.dumps(item['ganttDuration'])},\n")
            file.write(f"        Title: {json.dumps(item['title'])},\n")
            file.write(f"        DelayLog: {json.dumps(item['delayLog'])},\n")
            file.write(f"        ConstraintDate: {json.dumps(item['constraintDate'])},\n")
            file.write(f"        ConstraintType: {json.dumps(item['constraintType'])},\n")
            file.write(f"        Priority: {json.dumps(item['priority'])},\n")
            file.write("    }" + (",\n" if i < len(result) - 1 else "\n"))
        file.write("]\n")

    print(f"Transformed data saved to {filename}")

