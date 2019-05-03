#!/usr/bin/env python

import psycopg2

# Database name
DB_NAME = "news"

# Global database connection
dbConnection = None


def execute_query(query):
    cursor = dbConnection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


if __name__ == '__main__':
    dbConnection = psycopg2.connect("dbname=%s" % DB_NAME)

