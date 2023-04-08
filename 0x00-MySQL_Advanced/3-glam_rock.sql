-- script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT id, band_name, ifnull(split,2023)-ifnull(formed, 0) AS lifespan FROM metal_bands WHERE style="Glam rock" ORDER BY lifespan DESC;
