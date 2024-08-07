-- Stored Procedure
-- Script creates a stored procedure AddBonus that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus(
	IN user_id INT,
       	IN project_name VARCHAR(255),
        IN score FLOAT)
BEGIN

END
//
