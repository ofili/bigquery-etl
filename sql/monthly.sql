SELECT
    REPLACE(title, 'Lewis BigQuery ETL', '') AS title,
    url,
    REPLACE(REPLACE(url, 'https://bigquery.googleapis.com/', ''), 'projects/', '') AS slug,
    COUNT(title) AS views
FROM
    `bigquery-public-data.samples.shakespeare`
WHERE
    timestamp >= TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL -1 MONTH)
GROUP BY
    title,
    url
ORDER BY
    COUNT(title) DESC
LIMIT
    2000;
`
