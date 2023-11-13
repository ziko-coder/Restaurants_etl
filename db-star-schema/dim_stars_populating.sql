INSERT INTO public.dim_stars (stars)
SELECT DISTINCT "Stars" FROM public.restaurants_data;

--select * from public.dim_stars