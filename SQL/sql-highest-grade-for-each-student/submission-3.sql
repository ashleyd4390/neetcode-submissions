-- Write your query below
WITH ranked_scores AS (
    SELECT 
        student_id, exam_id, score,
        ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY score DESC, exam_id ASC) AS row_num
    FROM exam_results
)
SELECT student_id, exam_id, score
FROM ranked_scores
WHERE row_num = 1
