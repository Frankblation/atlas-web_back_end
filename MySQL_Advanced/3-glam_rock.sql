-- Script to list all bands with Glam rock as their main style, ranked by their longevity
-- Column names are band_name and lifespan (in years)
SELECT band_name, TIMESTAMPDIFF(year, MAKEDATE(formed, 1), IF(split IS NULL, CURDATE(), MAKEDATE(split, 1))) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;