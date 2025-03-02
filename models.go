package models

import "github.com/gocql/gocql"

type UserDetailsStruct struct {
	ID       gocql.UUID `json:"id"`
	MongoID  string     `json:"mongoID"`
	Team     string     `json:"team"`
	FullName string     `json:"fullName"`
	Project  string
	Email    string
	Role     string
}

type Statustruct struct {
	ID       gocql.UUID `json:"id"`
	MongoID  string     `json:"mongoID"`
	Category string     `json:"category"`
	Color    string     `json:"color"`
	WorkItem string     `json:"workItem"`
	Status   string     `json:"status"`
	Project  string     `json:"project"`
}

type TypesStruct struct {
	ID      gocql.UUID `json:"id"`
	MongoID string     `json:"mongoID"`
	Name    string     `json:"name"`
	Type    string
	Project string
}

type SubPhaseStruct struct {
	ID             gocql.UUID `json:"id"`
	MongoID        string     `json:"mongoid"`
	OrderID        string     `json:"orderID"`
	Phase          string     `json:"phase"`
	Type           string     `json:"category"`
	Role           string     `json:"role"`
	TaskType       string     `json:"type"`
	Workstream     string     `json:"workStream"`
	Project        string     `json:"project"`
	GanttDuration  float64
	Title          string `json:"title"`
	DelayLog       string
	ConstraintDate string
	ConstraintType string
}

type TaskDataStruct struct {
	ID               gocql.UUID `json:"id"`
	ActivePercentage float64    `json:"activePercentage"`
	AssignedTo       string     `json:"assignedTo"`
	ConstraintDate   string
	ConstraintType   string
	DelayLog         string
	GanttDuration    float64
	MongoID          string `json:"mongoID"`
	OrderID          string `json:"orderID"`
	Phase            string `json:"phaseID"`
	PlannedFrom      string `json:"plannedFrom"`
	PlannedTo        string `json:"plannedTo"`
	StartedOn        string `json:"startedOn"`
	CompletedOn      string `json:"completedOn"`
	Project          string `json:"project"`
	RefTaskID        string `json:"refTaskID"`
	Role             string `json:"role"`
	Status           string `json:"status"`
	SubPhaseID       string `json:"subphaseID"`
	TaskType         string `json:"taskType"`
	Title            string `json:"title"`
	Type             string `json:"type"`
	Workstream       string `json:"workStream"`
	Priority         string `json:"priority"`
}
type PSRRisks struct {
	ID              gocql.UUID `json:"id"`
	MongoID         string     `json:"mongoID"`
	Status          string     `json:"-"`
	PlannedTo       string     `json:"plannedTo"`
	AssignedTo      string
	Description     string  `json:"description"`
	AssessmentScore float64 `json:"assessmentScore"`
	RefTaskID       string
	Title           string
	Category        string
	Project         string
}

type Team struct {
	ID      gocql.UUID `json:"id"`
	MongoID string     `json:"mongoid"`
	Project string     `json:"project"`
	Title   string     `json:"title"`
	Type    string     `json:"type"`
}

type Dependencies struct {
	Project   string
	DBID      gocql.UUID
	ID        string
	Lag       int16
	LagUnit   string
	MongoID   string
	Source    string
	Target    string
	Type      int
	GanttType string
}
