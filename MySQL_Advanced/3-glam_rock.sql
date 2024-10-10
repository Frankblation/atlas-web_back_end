-- Script to list all bands with Glam rock as their main style, ranked by their longevity
-- Column names are band_name and lifespan (in years)

SELECT
    band_name,
    IFNULL(
        IF(split IS NULL, YEAR(CURDATE()), YEAR(split)) - YEAR(formed),
        0
    ) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;