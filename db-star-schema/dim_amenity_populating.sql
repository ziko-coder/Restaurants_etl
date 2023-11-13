
INSERT INTO public.dim_amenity (amenity_name)
SELECT DISTINCT "Amenity_1" FROM public.restaurants_data
UNION
SELECT DISTINCT "Amenity_2" FROM public.restaurants_data
UNION
SELECT DISTINCT "Amenity_3" FROM public.restaurants_data
UNION
SELECT DISTINCT "Amenity_4" FROM public.restaurants_data
UNION
SELECT DISTINCT "Amenity_5" FROM public.restaurants_data
UNION
SELECT DISTINCT "Amenity_6" FROM public.restaurants_data
UNION
SELECT DISTINCT "Amenity_7" FROM public.restaurants_data;


--select * from public.dim_amenity
