-- View1_lang_level_3_internal_services_employee_count

CREATE VIEW LANG_LEVEL_3_INTERNAL_SERVICES_EMPLOYEE_COUNT AS

SELECT COUNT(Employee.Employee_ID) as No_of_Employees,Project.Project_Name,Location.Location_Name, Portfolio.Portfolio_Name
FROM Employee JOIN Project ON Employee.Project_ID=Project.Project_ID
JOIN Portfolio ON Project.Portfolio_ID=Portfolio.Portfolio_ID
JOIN Location ON Project.Location_ID=Location.Location_ID
WHERE (Employee.Language_Level_ID=3)
GROUP BY Project.Project_Name,Location.Location_Name,Portfolio.Portfolio_Name
HAVING Portfolio.Portfolio_Name IN("Internal_Services");

-- View2_LAPTOP_MODEL_INFO_INTERNAL_SERVICES

create view laptop_model_info_internal_services as

SELECT DISTINCT Laptop_Info.Model_ID, Laptop_Model_Info.Model_Name,Laptop_Model_Info.Brand_Name
FROM Laptop_Info JOIN Laptop_Model_Info ON Laptop_Info.Model_ID=Laptop_Model_Info.Model_ID
WHERE Laptop_Info.Laptop_ID IN (SELECT Employee.Laptop_ID
                               FROM Employee JOIN Project ON Employee.Project_ID=Project.Project_ID
                               JOIN Portfolio ON Project.Portfolio_ID=Portfolio.Portfolio_ID
                               WHERE Portfolio.Portfolio_ID="ABC005");

-- view3_database_initiative_employee_count

CREATE VIEW DATABASE_INITIATIVE_EMPLOYEE_COUNT AS

SELECT count(Employee.Employee_ID)as No_of_Employees,Location.Location_Name, Project.Project_Name, Development_Initiative_Details.Initiative_Name
FROM Employee JOIN Project ON Employee.Project_ID=Project.Project_ID
JOIN Development_Initiative_Details ON Employee.Initiative_ID = Development_Initiative_Details.Initiative_ID
JOIN Location on Project.Location_ID = Location.Location_ID
GROUP by Location.Location_Name,Project.Project_Name, Development_Initiative_Details.Initiative_Name
HAVING Development_Initiative_Details.Initiative_Name = "Database_Expert"
ORDER BY No_of_Employees DESC;
