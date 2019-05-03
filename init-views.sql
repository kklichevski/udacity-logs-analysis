--
-- Creates new view. Top 3 articles
--

CREATE VIEW top_3_articles AS
SELECT top3.slug, author, views
FROM (SELECT substring(path FROM 10) AS slug, count(*) AS views
      FROM log
      WHERE path LIKE '/article/%' AND status = '200 OK'
      GROUP BY slug
      ORDER BY views DESC
      LIMIT 3) AS top3
JOIN articles ON top3.slug = articles.slug;


--
-- Creates new view. Number of requests per day
--

CREATE VIEW requests_per_day AS
SELECT time::date AS day, count(*) AS requests
FROM log
GROUP BY day;


--
-- Creates new view. Number of request errors per day (with status code not success)
--

CREATE VIEW requests_per_day_errors AS
SELECT time::date AS day, count(*) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY day;
