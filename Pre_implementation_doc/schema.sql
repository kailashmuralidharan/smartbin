-- Create queries

CREATE TABLE `Designation` (
  `Designation_ID` varchar(8) NOT NULL,
  `Designation_Name` varchar(32) NOT NULL,
  `Monthly_Salary` double NOT NULL
) ;

CREATE TABLE `Development_Initiative_Details` (
  `Initiative_ID` varchar(8) NOT NULL,
  `Initiative_Name` varchar(32) DEFAULT NULL,
  `Initiative_Start_Date` date DEFAULT '2010-12-31',
  `Initiative_Status` varchar(32) DEFAULT NULL
) ;

CREATE TABLE `Employee` (
  `Employee_ID` varchar(10) NOT NULL,
  `Employee_FirstName` varchar(32) DEFAULT NULL,
  `Employee_LastName` varchar(32) DEFAULT NULL,
  `Employee_DOB` date DEFAULT NULL,
  `Email_ID` varchar(128) DEFAULT NULL,
  `Address` varchar(128) DEFAULT NULL,
  `Contact_Number` int(10) DEFAULT NULL,
  `Date_Of_Joining` date DEFAULT NULL,
  `Designation_ID` varchar(8) DEFAULT NULL,
  `Project_ID` varchar(10) DEFAULT NULL,
  `Time_Off_Tracker_ID` int(11) DEFAULT NULL,
  `Initiative_ID` varchar(8) DEFAULT NULL,
  `Laptop_ID` varchar(10) DEFAULT NULL,
  `Language_Level_ID` int(10) DEFAULT NULL
) ;


CREATE TABLE `Language_Assessment_Details` (
  `Language_Level_ID` int(10) NOT NULL,
  `Level_Description` varchar(16) DEFAULT NULL
) ;


CREATE TABLE `Laptop_Info` (
  `Laptop_ID` varchar(10) NOT NULL,
  `Model_ID` varchar(10) DEFAULT NULL,
  `Given_Date` date DEFAULT NULL
) ;


CREATE TABLE `Laptop_Model_Info` (
  `Model_ID` varchar(10) NOT NULL,
  `Model_Name` varchar(32) DEFAULT NULL,
  `Brand_Name` varchar(32) DEFAULT NULL
) ;

CREATE TABLE `Location` (
  `Location_ID` varchar(10) NOT NULL,
  `Location_Name` varchar(32) DEFAULT NULL
) ;

CREATE TABLE `Portfolio` (
  `Portfolio_ID` varchar(10) NOT NULL,
  `Portfolio_Name` varchar(32) DEFAULT NULL
) ;

CREATE TABLE `Project` (
  `Project_ID` varchar(10) NOT NULL,
  `Project_Name` varchar(32) DEFAULT NULL,
  `Portfolio_ID` varchar(10) DEFAULT NULL,
  `Location_ID` varchar(10) DEFAULT NULL
);


CREATE TABLE `Time_Off_Hours` (
  `Time_Off_Tracker_ID` int(11) NOT NULL,
  `Given_Hours` int(11) NOT NULL,
  `Availed_Hours` int(11) NOT NULL,
  `status` varchar(16) NOT NULL
) ;

-- Insert Queries

INSERT INTO `Designation` (`Designation_ID`, `Designation_Name`, `Monthly_Salary`) VALUES
('D01', 'Associate', 25000),
('D02', 'Business Analyst', 40000),
('D03', 'Consultant', 65000),
('D04', 'Senior Consultant', 75000),
('D05', 'Manager', 90000);

INSERT INTO `Development_Initiative_Details` (`Initiative_ID`, `Initiative_Name`, `Initiative_Start_Date`, `Initiative_Status`) VALUES
('I01', 'Database_Expert', '2012-12-31', 'Active'),
('I02', 'Java_Expert', '2011-12-31', 'Active'),
('I03', 'Professional_Skills', '2013-12-31', 'Active'),
('I04', 'Analytics', '2014-12-31', 'Active'),
('I05', 'IT_Expert', '2010-12-31', 'Active');

INSERT INTO `Employee` (`Employee_ID`, `Employee_FirstName`, `Employee_LastName`, `Employee_DOB`, `Email_ID`, `Address`, `Contact_Number`, `Date_Of_Joining`, `Designation_ID`, `Project_ID`, `Time_Off_Tracker_ID`, `Initiative_ID`, `Laptop_ID`, `Language_Level_ID`) VALUES
('100200003', 'Meghna ', 'Raj', '1982-12-04', 'meghnaraj@gmail.com', '17 , Chandra Bhuvan, Goras Wadi, Malad - 400064', 23410, '2015-09-10', 'D03', 'PROJ33333', 1234567893, 'I02', 'LAP1002', 3),
('10020001', 'Abhinav', 'Krishna', '1985-08-05', 'abhinav@gmail.com', '603  Vipin Villa, Jame Jamshed Road, Matunga - 560031', 95973456, '2017-06-10', 'D03', 'PROJ10001', 1234567891, 'I01', 'LAP1001', 3),
('10020002', 'Umed ', 'Shasthri', '1985-08-12', 'umed@gmail.com', '14 /, Mehrauli Road, Nr Dev Cinema, Karnataka - 122001', 65027334, '2016-05-05', 'D02', 'PROJ10001', 1234567892, 'I01', 'LAP1006', 3),
('10020004', 'Kirti', 'Kirti  Mander', '1988-04-18', 'kirti@gmail.com', 'Krishna Bhavan, P D Mello Rd, Near Sagar Vihar Hotel, Chinch Bunder, Mumbai - 400009', 23433756, '2017-06-20', 'D04', 'PROJ33333', 1234567894, 'I03', 'LAP1003', 3),
('10020005', 'Nara ', 'Shere', '1987-02-09', 'nara@gmail.com', 'C/48, Sanman Chs, Kharegaon, Pakhadi, Kalwa, Mumbai - 400605', 78652345, '2015-05-13', 'D03', 'PROJ99999', 1234567895, 'I01', 'LAP1002', 3);

INSERT INTO `Language_Assessment_Details` (`Language_Level_ID`, `Level_Description`) VALUES
(1, 'Beginner'),
(2, 'Intermediate'),
(3, 'Good'),
(4, 'Mastery'),
(5, 'Excellence');

INSERT INTO `Laptop_Info` (`Laptop_ID`, `Model_ID`, `Given_Date`) VALUES
('LAP1001', 'MODEL01', '2015-03-11'),
('LAP1002', 'MODEL01', '2017-02-04'),
('LAP1003', 'MODEL02', '2018-10-09'),
('LAP1004', 'MODEL02', '2015-07-10'),
('LAP1005', 'MODEL03', '2018-04-10'),
('LAP1006', 'MODEL03', '2016-11-02'),
('LAP1007', 'MODEL04', '2017-07-11'),
('LAP1008', 'MODEL04', '2017-07-03'),
('LAP1009', 'MODEL05', '2016-09-07'),
('LAP1010', 'MODEL05', '2015-09-08');

INSERT INTO `Laptop_Model_Info` (`Model_ID`, `Model_Name`, `Brand_Name`) VALUES
('MODEL01', 'HP Chromebook 14', 'HP'),
('MODEL02', 'HP Spectre x360', 'HP'),
('MODEL03', 'Dell G5 15 5590', 'Dell'),
('MODEL04', 'Dell XPS 13', 'Dell'),
('MODEL05', 'MacBook Pro 16', 'Apple');

INSERT INTO `Location` (`Location_ID`, `Location_Name`) VALUES
('LOC01', 'Bangalore'),
('LOC02', 'Hyderabad'),
('LOC03', 'Mumbai'),
('LOC04', 'New Delhi'),
('LOC05', 'Chennai');


INSERT INTO `Portfolio` (`Portfolio_ID`, `Portfolio_Name`) VALUES
('ABC001', 'Audit'),
('ABC002', 'Tax'),
('ABC003', 'Consulting '),
('ABC004', 'Management_Services'),
('ABC005', 'Internal_Services');

INSERT INTO `Project` (`Project_ID`, `Project_Name`, `Portfolio_ID`, `Location_ID`) VALUES
('PROJ10001', 'MNP', 'ABC005', 'LOC04'),
('PROJ11111', 'GRD', 'ABC001', 'LOC01'),
('PROJ22222', 'SGG', 'ABC001', 'LOC02'),
('PROJ33333', 'YUY', 'ABC005', 'LOC01'),
('PROJ44444', 'KKH', 'ABC002', 'LOC03'),
('PROJ55555', 'HNH', 'ABC003', 'LOC01'),
('PROJ66666', 'TRR', 'ABC003', 'LOC04'),
('PROJ77777', 'RDD', 'ABC003', 'LOC03'),
('PROJ88888', 'WWT', 'ABC004', 'LOC01'),
('PROJ99999', 'CVV', 'ABC005', 'LOC05');

INSERT INTO `Time_Off_Hours` (`Time_Off_Tracker_ID`, `Given_Hours`, `Availed_Hours`, `status`) VALUES
(1234567891, 450, 350, 'AVAILABLE'),
(1234567892, 450, 250, 'AVAILABLE'),
(1234567893, 450, 375, 'AVAILABLE'),
(1234567894, 450, 300, 'AVAILABLE'),
(1234567895, 450, 400, 'AVAILABLE');
