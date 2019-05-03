#!/usr/bin/env python

import psycopg2

# Database name
DB_NAME = "news"

# Global database connection
dbConnection = None

if __name__ == '__main__':
    dbConnection = psycopg2.connect("dbname=%s" % DB_NAME)

