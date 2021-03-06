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


def top_3_articles():
    return execute_query(
        "SELECT title, views "
        "FROM top_3_articles, articles "
        "WHERE top_3_articles.slug = articles.slug "
        "ORDER BY top_3_articles.views DESC;"
    )


def top_3_authors():
    return execute_query(
        "SELECT name, views "
        "FROM top_3_articles,authors "
        "WHERE top_3_articles.author = authors.id "
        "ORDER BY top_3_articles.views DESC;"
    )


def daily_request_errors(filter_percentages=1):
    return execute_query(
        "SELECT requests_per_day.day, trunc(errors::decimal/requests * 100, 2)"
        "  AS error_percentage "
        "FROM requests_per_day "
        "LEFT JOIN requests_per_day_errors "
        "  ON requests_per_day.day = requests_per_day_errors.day "
        "WHERE errors::decimal / requests > %f;" % (filter_percentages / 100.0)
    )


if __name__ == '__main__':
    dbConnection = psycopg2.connect("dbname=%s" % DB_NAME)

    print_tuple(top_3_articles(), "Top 3 articles", " views", True)
    print

    print_tuple(top_3_authors(), "Top 3 authors", " views")
    print

    print_tuple(daily_request_errors(1),
                "Requests error per day (more than 1%)", "% errors")
