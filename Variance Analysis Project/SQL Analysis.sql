----------------------------------------------------------
-- Budget Table []
----------------------------------------------------------
SELECT * FROM budget;

--create a function to store it in unpivot formating
DROP FUNCTION unpivot_budget();
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

-- show the table after the unpivoting
SELECT * FROM unpivot_budget();

-- Return the total value for each product
SELECT SUM(value) AS Total_Budget_Aspen FROM unpivot_budget()
Where product = 'Aspen';

SELECT SUM(value) AS Total_Budget_Carlota FROM unpivot_budget()
Where product = 'Carlota';

SELECT SUM(value) AS Total_Budget_Quad FROM unpivot_budget()
Where product = 'Quad';

-- Return the total value for the all product
SELECT SUM(value)  AS Total_Budget FROM unpivot_budget();


----------------------------------------------------------
-- Actual Table []
----------------------------------------------------------

-- Return the total sales for each product
SELECT Round(SUM(sales), 2) AS Total_Actual_Aspen FROM actual
Where product = 'Aspen';

SELECT Round(SUM(sales), 2) AS Total_Actual_Carlota FROM actual
Where product = 'Carlota';

SELECT Round(SUM(sales), 2) AS Total_Actual_Quad FROM actual
Where product = 'Quad';

-- Return the total sales for the all product
SELECT Round(SUM(sales), 2) AS Total_Actual_Sales FROM actual;

----------------------------------------------------------
-- Budget_Variance & Budget_Variance %
----------------------------------------------------------
SELECT (SELECT SUM(sales) FROM actual) - SUM(value) AS Budget_Variance
FROM unpivot_budget();


SELECT Concat(ROUND(((SELECT SUM(sales) FROM actual) - SUM(value)) / SUM(value) *100, 2), '%')  
AS "Budget_Variance%"
FROM unpivot_budget();
----------------------------------------------------------
-- Let's Drill Down <3
----------------------------------------------------------

SELECT COALESCE(b.eomonth, a.Date) AS EOMonth,
		ROUND(SUM(b.TotalValue), 2) AS TotalValue,
		ROUND(SUM(a.TotalSales), 2) AS TotalSales
FROM 
	(SELECT EOMONTH(date) AS Date, SUM(sales) AS TotalSales FROM actual
	GROUP BY EOMONTH(date)) a
FULL OUTER JOIN 
    (SELECT eomonth, SUM(value) AS TotalValue FROM unpivot_budget()
     GROUP BY eomonth) b
ON a.Date = b.eomonth
GROUP BY COALESCE(b.eomonth, a.Date)
ORDER BY EOMonth;


SELECT COALESCE(b.eomonth, a.Date) AS EOMonth,
		ROUND((SUM(b.TotalValue) - SUM(a.TotalSales)),2) AS TotalSales
FROM 
	(SELECT EOMONTH(date) AS Date, SUM(sales) AS TotalSales FROM actual
	GROUP BY EOMONTH(date)) a
FULL OUTER JOIN 
    (SELECT eomonth, SUM(value) AS TotalValue FROM unpivot_budget()
     GROUP BY eomonth) b
ON a.Date = b.eomonth
GROUP BY COALESCE(b.eomonth, a.Date)
ORDER BY EOMonth;


SELECT COALESCE(b.eomonth, a.Date) AS EOMonth,
		ROUND((SUM(b.TotalValue)- SUM(a.TotalSales))/SUM(b.TotalValue) *100, 2) AS TotalSales
FROM 
	(SELECT EOMONTH(date) AS Date, SUM(sales) AS TotalSales FROM actual
	GROUP BY EOMONTH(date)) a
FULL OUTER JOIN 
    (SELECT eomonth, SUM(value) AS TotalValue FROM unpivot_budget()
     GROUP BY eomonth) b
ON a.Date = b.eomonth
GROUP BY COALESCE(b.eomonth, a.Date)
ORDER BY EOMonth;