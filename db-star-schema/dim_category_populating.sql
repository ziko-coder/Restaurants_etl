INSERT INTO public.dim_category (category_name)
SELECT DISTINCT "Category_1" FROM public.restaurants_data
UNION
SELECT DISTINCT "Category_2" FROM public.restaurants_data
UNION
SELECT DISTINCT "Category_3" FROM public.restaurants_data;

--select * from public.dim_category