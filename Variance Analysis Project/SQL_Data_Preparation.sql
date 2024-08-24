-- #1 Data Discovering
SELECT * FROM Budget;
SELECT * FROM Actual;

-- #2 Data Preparation

-- #2.1 Create a function to store the data in unpivot formating
DROP FUNCTION IF EXISTS unpivot_budget();

CREATE FUNCTION unpivot_budget()
RETURNS TABLE (
  product TEXT,
  EOMonth DATE,
  value NUMERIC
)
AS $$
  WITH data AS (
    SELECT 'Aspen' AS product, EOMonth, Aspen AS value
    FROM budget
    UNION ALL
    SELECT 'Carlota' AS product, EOMonth, Carlota AS value
    FROM budget
    UNION ALL
    SELECT 'Quad' AS product, EOMonth, Quad AS value
    FROM budget
  )
  SELECT * FROM data;
$$
LANGUAGE sql;

SELECT * FROM unpivot_budget();

-- #2.2 Store the Function data in a new table (Tabular_table)
DROP TABLE IF EXISTS Tabular_budget;

CREATE TABLE Tabular_budget(
    Date DATE,
    Value NUMERIC(18, 2),
    Product NVARCHAR(50)
);

INSERT INTO Tabular_budget (Date, Value, Product)
SELECT eomonth, ROUND(SUM(value), 2) AS Total_budget, product FROM unpivot_budget()
GROUP BY eomonth, product
ORDER BY eomonth, product;

SELECT * FROM Tabular_budget

-----------------------------------------------------------------------------------------
-- #2.3 Handling the Actual Table
DROP TABLE IF EXISTS Tabular_Actual;

CREATE TABLE Tabular_Actual (
    Date DATE,
    Total_Sales NUMERIC(18, 2),
    Product NVARCHAR(50)
);

INSERT INTO Tabular_Actual (Date, Total_Sales, Product)
SELECT EOMONTH(date) AS Date, ROUND(SUM(sales), 2) AS Total_Sales, Product
FROM actual 
GROUP BY EOMONTH(date), Product
ORDER BY EOMONTH(date), Product;

SELECT * FROM Tabular_Actual

-----------------------------------------------------------------------------------------
-- #2.4 Create a Calendar Table
DROP TABLE IF EXISTS Calendar;

CREATE TABLE Calendar (
    Date DATE
);

INSERT INTO Calendar (Date)
SELECT EOMONTH(date) AS Date FROM actual 
GROUP BY EOMONTH(date)
ORDER BY EOMONTH(date);

SELECT * FROM Calendar





















