package db

import (
	"fmt"

	"github.com/gocql/gocql"
)

func DBConnection() (*gocql.Session, error) {
	cluster := gocql.NewCluster("<i/p>")
	cluster.Keyspace = "dharun"
	cluster.Consistency = gocql.One
	cluster.NumConns = 20 // Open multiple connections per
	// cluster.PoolConfig.HostSelectionPolicy = gocql.TokenAwareHostPolicy(gocql.DCAwareRoundRobinPolicy())
	session, err := cluster.CreateSession()
	if err != nil {
		fmt.Println("Error in creating session")
		return nil, err
	}
	return session, nil
}
