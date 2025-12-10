-- Last updated: 10/12/2025, 07:42:25
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from employee order by salary desc limit 1 offset N
  );
END
