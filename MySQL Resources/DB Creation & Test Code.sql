-- generates database
CREATE DATABASE IF NOT EXISTS project0;

-- generates necessary tables for database
-- row_index was set as a primary key to ensure ease of access and reading

CREATE TABLE `project0`.`sql_admin` (
`row_index` INT NOT NULL AUTO_INCREMENT,
`cl_user` VARCHAR(255) NULL DEFAULT '(Undefined)',
`cl_pass` VARCHAR(255) NULL DEFAULT '(Undefined)',
PRIMARY KEY (`row_index`),
UNIQUE INDEX `cl_user_UNIQUE` (`cl_user` ASC) VISIBLE
);

CREATE TABLE `project0`.`sql_user` (
  `row_index` INT NOT NULL AUTO_INCREMENT,
  `website` VARCHAR(255) NOT NULL,
  `username` VARCHAR(255) NULL DEFAULT '(Undefined)',
  `password` VARCHAR(255) NULL DEFAULT '(Undefined)',
  `email` VARCHAR(255) NULL DEFAULT '(Undefined)',
  `cl_user` VARCHAR(255),
  PRIMARY KEY (`row_index`),
  FOREIGN KEY (`cl_user`) REFERENCES `project0`.`sql_admin`(`cl_user`),
  UNIQUE INDEX `website_UNIQUE` (`website` ASC) VISIBLE
 );
 
 -- Inserts the important data into the Admin table
 -- no need to add to row_index as it is set to auto_increment
 INSERT INTO sql_admin(cl_user, cl_pass) VALUES('TerrAsauR','YEET!');
 
  -- Command to insert test data into database
  INSERT INTO sql_user(`website`, `username`, `password`, `email`, `cl_user`) VALUES('Test Website', 'Test User', 'p455w0rd', 'email@address.com', 'HamingnottT');
  INSERT INTO sql_user(`website`, `username`, `password`, `email`, `cl_user`) VALUES('Website Test', 'User Test', 'p455w0rd', 'email@address.com', 'TerrAsauR');