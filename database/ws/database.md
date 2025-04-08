- update문 에서 필드 하나의 모든 레코드에 대해 동일 변경 사항을 지정하고 싶은 경우
```sql
UPDATE hotels
SET grade = upper(grade);
```