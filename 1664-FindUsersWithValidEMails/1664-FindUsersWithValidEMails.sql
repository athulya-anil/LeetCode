-- Last updated: 10/12/2025, 07:40:27
#Solution by siddarth
SELECT * FROM Users
WHERE mail REGEXP '^[a-z][a-zA-Z0-9_.-]*@leetcode[.]com' and mail like '%leetcode.com';

