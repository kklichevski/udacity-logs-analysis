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


def print_tuple(tuples, header_title, trial_word, quotes_first_value=False):
    print header_title + ":"
    print "-" * (len(header_title) + 1)

    for row in tuples:
        value1 = row[0] if not quotes_first_value else "\"%s\"" % row[0]
        print "%s -- %s%s" % (value1, row[1], trial_word)


if __name__ == '__main__':
    dbConnection = psycopg2.connect("dbname=%s" % DB_NAME)

