create TABLE public."dim_business" (
	business_id SERIAL PRIMARY KEY,
	business_name TEXT,
    phone_number TEXT,
    Address TEXT,
    Price_Range TEXT
	
);

CREATE TABLE public."dim_category" (
	category_id SERIAL PRIMARY KEY,
	Category_Name TEXT
);

CREATE TABLE public."dim_amenity" (
	amenity_id SERIAL PRIMARY KEY,
	Amenity_Name TEXT
	
);

CREATE TABLE public."dim_stars" (
	stars_id SERIAL PRIMARY KEY,
	Stars NUMERIC
);

