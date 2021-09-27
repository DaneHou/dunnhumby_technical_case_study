-- Section 2: pandas/SQL data frames
-- Suppose you have access to two data frames, dept and employee.  The first three rows of these are represented below. 

--  employee.head(3) 
 
-- dept.head(3) 
 
-- Notes: 
-- •	MGR is the EMPNO of the Employee whom the observed Employee reports to.   
-- •	DEPTNO is a foreign key.   
 
-- QUESTIONS
-- 1.	Find the nth largest salary. 
-- 2.	List the highest salary paid for each job.
-- 3.	In which year did most people join the company?  Display the year and the number of Employees. 
-- 4.	Create a new column with the length of service of the Employees (in the form n years and m months). 
-- 5.	List all the Employees who have at least one person reporting to them. 


-- 1.	Find the nth largest salary.
SELECT sal 
FROM employee 
ORDER BY sal DESC 
LIMIT N-1, 1



-- 2.	List the highest salary paid for each job.
with job_sal_rank as (
    select *, 
        ROW_Number() over(
            partition by job
            order by sal desc
        ) as ranking
    from employee
    )
    
select job, sal
from job_sal_rank
where ranking = 1



-- 3.	In which year did most people join the company?  Display the year and the number of Employees. 
select EXTRACT(YEAR FROM hiredate), count(distinct empno) as emp_num
from employee
group by EXTRACT(YEAR FROM hiredate)
order by 2 desc
limit 1


-- 4.	Create a new column with the length of service of the Employees (in the form n years and m months). 
with emp_length as (
                    select empno, datediff(month, hiredate, NOW()) diff_months
                    from employee
                    )
                    
select empno, CONCAT((diff_months/12::int)::text, ' years ', (diff_months%12::int)::text, ' months') as employment_length
from emp_length


-- --Another solution
-- with emp_length as (
--                     SELECT 
--                         empno
--                         DATE_PART('year', AGE(NOW(), hiredate)) AS years,
--                         DATE_PART('month', AGE(NOW(), hiredate)) AS months
--                     FROM employee
--                     ) 

-- select empno, CONCAT(years::text, ' years ', months::text, ' months') as employment_length
-- from emp_length




-- 5.	List all the Employees who have at least one person reporting to them. 
select mgr, count(distinct empno) as subordinate
from employee
group by mgr
having count(distinct empno) >= 1