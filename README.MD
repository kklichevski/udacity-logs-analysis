# Logs Analysis (Project)

Log analysis for articles on a newspaper site

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

1. A FSND-Virtual-Machine of Udacity running (See instruction on [Fullstack Nanodegree VM repository](https://github.com/udacity/fullstack-nanodegree-vm)).
2. Imported data for 'news' database ([newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)).
3. VIEW queries imported.
4. Python2 installed.

### Running

A step by step series of examples that tell you how to get this project running

Import the VIEW queries (Only for initialize the project)
_or see the VIEWs source code at the end of this file_

```
psql news
\i init-views.sql
```

Run the python file

```
python logs-analysis.py
```

An example of the program's output (see also 'output.txt')

```
Top 3 articles:
---------------
"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views

Top 3 authors:
--------------
Rudolf von Treppenwitz -- 338647 views
Ursula La Multa -- 253801 views
Anonymous Contributor -- 170098 views

Requests error per day (more than 1%):
--------------------------------------
2016-07-17 -- 2.26% errors
```

## Authors

* **Kfir Klichevski**

## VIEW queries

Top 3 articles (popularity)

```
CREATE VIEW top_3_articles AS
SELECT top3.slug, author, views
FROM (SELECT substring(path FROM 10) AS slug, count(*) AS views
      FROM log
      WHERE path LIKE '/article/%' AND status = '200 OK'
      GROUP BY slug
      ORDER BY views DESC
      LIMIT 3) AS top3
JOIN articles ON top3.slug = articles.slug;
```

Number of requests per day

```
CREATE VIEW requests_per_day AS
SELECT time::date AS day, count(*) AS requests
FROM log
GROUP BY day;
```

Number of request errors per day (with status code not success)

```
CREATE VIEW requests_per_day_errors AS
SELECT time::date AS day, count(*) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY day;
```