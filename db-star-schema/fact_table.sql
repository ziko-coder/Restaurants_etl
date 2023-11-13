CREATE TABLE public.fact_restaurant (
    fact_id SERIAL PRIMARY KEY,
    business_id INTEGER REFERENCES public.dim_business(business_id),
    category_id INTEGER REFERENCES public.dim_category(category_id),
    amenity_id INTEGER REFERENCES public.dim_amenity(amenity_id),
    stars_id INTEGER REFERENCES public.dim_stars(stars_id),
    Ratings NUMERIC,
    Years_in_Business NUMERIC
);