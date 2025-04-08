-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(100) NOT NULL,
    createdAt DATE NOT NULL
);

-- 1. Insert data into table
-- id는 AUTOINCREMENT라서 자동으로 입력될 것
INSERT INTO articles(title, content, "createdAt")
VALUES ('hello', 'world', '2000-01-01');


INSERT INTO articles(title, content, "createdAt")
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');

INSERT INTO articles(title, content, "createdAt")
VALUES
    ('mytitle', 'mycontent', DATE());
-- 2. Update data in table
UPDATE
    articles
SET 
    title = 'update Title'
WHERE
    id = 1;

UPDATE
    articles
SET
    title = 'update Title',
    content = 'update Content'
WHERE
    id = 2;
-- 3. Delete data from table
DELETE FROM
    articles
WHERE
    id = 1;


DELETE FROM
    articles
-- 작성한 지 오래된 게시글 2개
WHERE id IN(
    SELECT id FROM articles
    ORDER BY "createdAt"
    LIMIT 2
);