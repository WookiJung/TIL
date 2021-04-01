SELECT last_name, count(*) From users
group by last_name;  -- 전체 조회 후 ㄱㄴㄷ 순서
-- lastname이 같은사람들만 따로 select 구문 진행

SElect DISTINCT last_name from users;  -- 등장순서대로

