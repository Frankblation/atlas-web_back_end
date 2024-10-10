--a stored procedure ComputeAverageScoreForUser
--computes and stores the average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(input_id INT)
BEGIN
    DECLARE average FLOAT;

    -- Calculate the average score, handling nulls
    SELECT AVG(score) INTO average
    FROM corrections
    WHERE user_id = input_id;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = average
    WHERE id = input_id;
END$$

DELIMITER ;