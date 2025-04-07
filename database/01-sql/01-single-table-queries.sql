-- 01. Querying data
SELECT 
  LastName
FROM
  employees;

SELECT LastName, FirstName
FROM employees;

SELECT * FROM employees;

SELECT Name , Milliseconds / 60000 AS '재생 시간(분)'
FROM tracks;


-- 02. Sorting data
SELECT 
  FirstName AS '이름'
FROM
  employees
ORDER BY 
  FirstName DESC;

SELECT Country, City
FROM customers
ORDER BY Country DESC, City;

-- NULL 정렬 예시
SELECT 
  postalCode
FROM
  customers
ORDER BY
  postalCode;

SELECT Name, Milliseconds / 60000 AS '재생 시간 (분)'
FROM tracks
ORDER BY Milliseconds DESC;

-- 03. Filtering data
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT LastName, FirstName, City
FROM customers
WHERE City = 'Prague';

SELECT LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

SELECT Name, Bytes
From tracks
WHERE Bytes BETWEEN 10000 AND 500000;

SELECT Name, Bytes
From tracks
WHERE Bytes BETWEEN 10000 AND 500000
ORDER BY Bytes;

SELECT LastName, "FirstName", "Country"
FROM customers
WHERE Country IN ('Canada', 'Germany', 'France');

-- WHERE
--   Country = 'Canada'
--   OR Country = 'Germany'
--   OR Country = 'France';

SELECT LastName, "FirstName", "Country"
FROM customers
WHERE Country NOT IN ('Canada', 'Germany', 'France');


SELECT "LastName", "FirstName"
FROM customers
WHERE
  "LastName" LIKE '%son';

SELECT "LastName", "FirstName"
FROM customers
WHERE "FirstName" LIKE '___a';

SELECT TrackId, Name, Bytes
FROM
  tracks
ORDER BY Bytes DESC
LIMIT 7;

SELECT TrackId, Name, Bytes
FROM
  tracks
ORDER BY Bytes DESC
-- LIMIT 3, 4;
LIMIT 4 OFFSET 3;

-- 04. Grouping data
SELECT
  Country, COUNT(*) AS '고객 수'
  -- COUNT(Country) 로 적어도 동일, 앞에 필드를 기준으로 COUNT하는거라면 일반적으로 COUNT(*) 사용
FROM
  customers
GROUP BY
  Country;


SELECT 
  Composer,
  AVG(Bytes)
FROM
  tracks
GROUP BY
  "Composer"
ORDER BY
  AVG(Bytes) DESC;