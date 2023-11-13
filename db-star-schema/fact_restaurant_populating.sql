INSERT INTO public.fact_restaurant (business_id, category_id, amenity_id, stars_id, ratings, years_in_business)
SELECT
    b.business_id,
    c.category_id,
    a.amenity_id,
    s.stars_id,
    rd."Ratings",
    rd."Years_in_Business"
FROM
    public.restaurants_data rd
LEFT JOIN
    public.dim_business b ON rd."Business_Name" = b.business_name
LEFT JOIN
    public.dim_category c ON rd."Category_1" = c.category_name
LEFT JOIN
    public.dim_amenity a ON rd."Amenity_1" = a.amenity_name
LEFT JOIN
    public.dim_stars s ON rd."Stars" = s.stars;
