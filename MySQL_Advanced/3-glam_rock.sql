-- Script to list all bands with Glam rock as their main style, ranked by their longevity
-- Column names are band_name and lifespan (in years)

SELECT band_name, 
    CASE
        WHEN split IS NULL THEN ((YEAR(NOW()) - formed) - 4)
        ELSE (split - formed)
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;