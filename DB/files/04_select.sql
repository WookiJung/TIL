--create와 다르게 DB에 변화가 없음--
--전체조회

SELECT * FROM classmates;

-- 컬럼지정조회

SELECT name, address FROM classmates;

-- 개수지정

SELECT id, name FROM classmates LIMIT 1;