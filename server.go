package main

import (
	"fmt"
	"scylladb/db"
	"scylladb/models"
	"time"

	"github.com/gocql/gocql"
	"github.com/gofiber/fiber/v2"
	// "github.com/gofiber/storage/scylladb"
)

var client *gocql.Session

func main() {
	var err error
	app := fiber.New()
	client, err = db.DBConnection()
	if err != nil {
		fmt.Println("Error")
	}
	app.Get("/", greetings)
	app.Get("/ji", insertStatusData)
	app.Listen(":8000")
	fmt.Println("APP is listening in PORT 8000")
}

func greetings(c *fiber.Ctx) error {
	var tasksData []models.TaskDataStruct
	// var id gocql.UUID
	// var activePercentage, ganttduration float64
	// var actualend, actualstart, assignedto, mongoid, orderid, phase, plannedfrom, plannedto, project, reftaskid, role, status, subphaseid, tasktype, title, types, workstream string
	start := time.Now()
	iter := client.Query(`SELECT * from tasks`).Iter()
	fmt.Println("time taken for query", time.Since(start))
	startw := time.Now()
	itere := client.Query(`SELECT * from taskslists WHERE project_id = '66300cee23006656a617f366'`).Iter()
	fmt.Println("time taken for query using partition", time.Since(startw))
	fmt.Println("time taken for query", itere)
	timetakenForScan := time.Now()
	// for iter.Scan(&id, &activePercentage, &actualend, &actualstart, &assignedto, &ganttduration, &mongoid, &orderid, &phase, &plannedfrom,
	// 	&plannedto, &project, &reftaskid, &role, &status, &subphaseid, &tasktype, &title, &types, &workstream) {
	// 	task := models.TaskDataStruct{
	// 		ID:               id,
	// 		ActivePercentage: activePercentage,
	// 		StartedOn:        actualstart,
	// 		CompletedOn:      actualend,
	// 		AssignedTo:       assignedto,
	// 		GanttDuration:    ganttduration,
	// 		MongoID:          mongoid,
	// 		OrderID:          orderid,
	// 		Phase:            phase,
	// 		PlannedFrom:      plannedfrom,
	// 		PlannedTo:        plannedto,
	// 		Project:          project,
	// 		RefTaskID:        reftaskid,
	// 		Role:             role,
	// 		Status:           status,
	// 		SubPhaseID:       subphaseid,
	// 		TaskType:         tasktype,
	// 		Title:            title,
	// 		Type:             types,
	// 		Workstream:       workstream,
	// 	}
	// 	tasksData = append(tasksData, task)
	// }
	row := make(map[string]interface{})
	for iter.MapScan(row) {
		tasksData = append(tasksData, models.TaskDataStruct{
			ID:               row["id"].(gocql.UUID),
			ActivePercentage: row["activepercentage"].(float64),
			StartedOn:        row["actualstart"].(string),
			CompletedOn:      row["actualend"].(string),
			AssignedTo:       row["assignedto"].(string),
			GanttDuration:    row["ganttduration"].(float64),
			MongoID:          row["mongoid"].(string),
			OrderID:          row["orderid"].(string),
			Phase:            row["phase"].(string),
			PlannedFrom:      row["plannedfrom"].(string),
			PlannedTo:        row["plannedto"].(string),
			Project:          row["project"].(string),
			RefTaskID:        row["reftaskid"].(string),
			Role:             row["role"].(string),
			Status:           row["status"].(string),
			SubPhaseID:       row["subphaseid"].(string),
			TaskType:         row["tasktype"].(string),
			Title:            row["title"].(string),
			Type:             row["type"].(string),
			Workstream:       row["workstream"].(string),
		})
		row = make(map[string]interface{}) // Reset for next row
	}

	fmt.Println("time taken for scan", time.Since(timetakenForScan))
	err := iter.Close()
	if err != nil {
		fmt.Println("ERROR IN DATA", err.Error())
		return c.JSON("ERROR Da macha ")
	}
	fmt.Println(len(tasksData), "length")
	return c.JSON(tasksData)
}

func insertStatusData(c *fiber.Ctx) error {
	ddata := []models.Dependencies{}
	for _, dep := range ddata {
		err := client.Query(`INSERT into dependencies(project,dbid,gantttype,id,
		lag,lagunit,mongoid,source,target,type
		) 
		VALUES(?,?,?,?,?,?,?,?,?,?)`, dep.Project, dep.DBID, dep.GanttType, dep.ID,
			dep.Lag, dep.LagUnit, dep.MongoID, dep.Source, dep.Target, dep.Type).Exec()

		if err != nil {
			fmt.Println("error in data", err.Error())
			return c.JSON("error")
		}
	}
	return c.JSON("success")
}
