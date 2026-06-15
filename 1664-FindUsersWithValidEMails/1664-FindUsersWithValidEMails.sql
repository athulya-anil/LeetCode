-- Last updated: 14/06/2026, 23:02:04
#Solution by siddarth
SELECT * FROM Users
WHERE mail REGEXP '^[a-z][a-zA-Z0-9_.-]*@leetcode[.]com' and mail like '%leetcode.com';

