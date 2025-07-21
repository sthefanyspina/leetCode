SELECT employee_id FROM Employees WHERE salary > 3000
AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id
