-- Compute average weighted score
-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users AS U, 
		(SELECT U.id, SUM(score * weight) / SUM(weight) AS wt_avg
		FROM users AS U
	       	JOIN corrections AS C ON U.id=C.user_id
		JOIN projects AS P ON C.project_id=P.id
		GROUP BY U.id) AS WT_AVG
	SET U.average_score = WT_AVG.wt_avg
	WHERE U.id = WT_AVG.id;
END //
DELIMITER ;
