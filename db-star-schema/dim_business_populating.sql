INSERT INTO public.dim_business (business_name, phone_number, address, price_range)
SELECT "Business_Name", "Phone_Number", "Address", "Price_Range" FROM public.restaurants_data;

--select * from public.dim_business