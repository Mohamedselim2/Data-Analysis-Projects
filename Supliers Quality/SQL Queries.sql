CREATE TABLE NewPlants (
    City VARCHAR(255),
    State CHAR(2),
    Plant_ID INT PRIMARY KEY
);
INSERT INTO newplants (City, State, Plant_ID)
SELECT
    SUBSTRING_INDEX(Plant_Name, ',', 1) AS City,
    CASE
    WHEN Plant_Name REGEXP '.*, [A-Z]' 
    THEN SUBSTRING_INDEX(Plant_Name, ', ', -1)
    WHEN Plant_Name REGEXP '.* [A-Z]' 
    THEN SUBSTRING_INDEX(Plant_Name, ' ', -1)
    ELSE RIGHT(Plant_Name, NULL)
    END AS State,
Plant_ID
FROM Plants;


ALTER TABLE Categories
DROP COLUMN Sub_Category, 
RENAME COLUMN Sub_Category_ID TO Category_ID;


CREATE TABLE IF NOT EXISTS States(
 State_ID VARCHAR(2) PRIMARY KEY,
 State_Name VARCHAR(125)
);
INSERT INTO States (State_ID,State_Name) 
VALUES 
 ('MI','Michigan'),
 ('WI','Wisconsin'),
 ('IL','Illinois'),
 ('IN','Indiana'),
 ('OH','Ohio'),
 ('IA','Iowa');
