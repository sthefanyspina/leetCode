SELECT name, SUM(amount) AS balance FROM USERS
LEFT JOIN Transactions ON Users.account = Transactions.account
GROUP BY Users.account
HAVING SUM(amount) > 10000
