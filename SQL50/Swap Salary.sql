UPDATE Salary SET sex = 
CASE SEX
WHEN 'm' THEN 'f'
ELSE 'm'
END
