-- Select all bands with Glam rock as their main style, calculating their lifespan
-- Column names must be: band_name and lifespan (in years)
SELECT
    name AS band_name,
    CASE
        WHEN split IS NULL THEN YEAR(CURDATE()) - formed  -- if the band hasn't split, calculate lifespan until current year
        ELSE split - formed  -- if the band has split, calculate lifespan until split year
    END AS lifespan
FROM
    bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
