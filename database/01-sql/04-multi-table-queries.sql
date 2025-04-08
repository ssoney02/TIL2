-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN
-- 1단계. 두 테이블 결합 후 조건에 만족하는 모든 필드 조회
-- 작성자가 존재하는 모든 게시글을 출력
-- 2단계. 최종 출력 필드에 맞게 title과 name만 조회
-- SELECT title, name해도 필드이름이 겹치지 않아서 잘 조회되긴 함 but.. 권장x 명시적으로!!
SELECT articles.title, users.name
FROM articles
INNER JOIN users
  ON users.id = articles."userId"
-- 3단계. 1번 작성자가 작성한 게시글만 조회
WHERE "userId" = 1;



-- LEFT JOIN
-- 1단계. 모든 유저 정보 출력 + 이 유저들이 작성한 게시글 정보까지
SELECT articles.name
FROM users
LEFT JOIN articles
  ON articles."userId" = users.id
-- 2단계. 1단계 결과에서 결국 article 정보가 NUll 사용자가 게시글을 작성한 적이 없는 사용자다!
WHERE articles."userId" IS NULL;
--  3단계. 2단계 출력에서 문제 요구사항에 맞게 사용자 이름만 출력
