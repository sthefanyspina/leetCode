SELECT SalesPerson.name FROM SalesPerson 
WHERE SalesPerson.name NOT IN(
    SELECT SalesPerson.name FROM SalesPerson 
    LEFT JOIN Orders ON SalesPerson.sales_id = Orders.sales_id 
    LEFT JOIN Company ON Company.com_id = Orders.com_id 
    WHERE Company.name = 'Red')
