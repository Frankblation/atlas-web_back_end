-- Script to list all bands with Glam rock as their main style, ranked by their longevity
-- Column names are band_name and lifespan (in years)

SELECT
    band_name,
    IFNULL(YEAR(split), YEAR(CURDATE())) - YEAR(formed) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;