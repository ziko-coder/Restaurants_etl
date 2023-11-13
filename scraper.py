import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
}

data_list = []

for i in range(0, 101, 1):
    print('\n' + 'sending request ...')
    page = requests.get(f'https://www.yellowpages.com/los-angeles-ca/restaurants?page={i}', headers=headers)
    page_content = page.content
    print('\n' + 'Parsing content ...')
    soup = BeautifulSoup(page_content, 'html.parser')
    print('\n' + f'page{i}' + '\n')

    primary_cards = soup.find_all('div', class_='info-primary')

    for card in primary_cards:
        # extract business name
        business_name_tag = card.find('a', class_='business-name')
        business_name = business_name_tag.get_text() if business_name_tag else 'NONE'

        #extract business categories
        categories_tags = card.find('div', class_='categories').find_all('a')
        categories = [category.get_text() for category in categories_tags] if categories_tags else ['NONE']

        # extract amenities
        amenities_section = card.find('div', class_='amenities-info')
        amenities = []
        if amenities_section:
           spans = amenities_section.findAll('span', class_=None)
           amenities = [span.get_text() for span in spans]

        else:
            amenities.append('None')

        ratings = []
        ratings_div = card.find('div', class_="ratings")
        if ratings_div:
            rating_tags = ratings_div.find_all('a')
            for rating_tag in rating_tags:
                rating = rating_tag.find('div', class_='result-rating')
                count = rating_tag.find('span', class_='count')
                if rating and count:
                    rating_text = rating.get('class')[1]
                    count_text = count.get_text()
                    ratings.append(f'{rating_text} ({count_text})')
                else:
                    ratings.append('NONE')
        else:
            ratings = ['NONE', 'NONE']

        # Extract snippet text (now handling it as a sibling)
        snippet_tag = card.find_next_sibling('div', class_ ='snippet').find('p', class_ ='body') if card.find_next_sibling('div', class_ ='snippet') else None
        snippet_text = snippet_tag.get_text() if snippet_tag else 'NONE'

        # extract number of years in business
        years_in_business_div = card.find('div', class_='years-in-business')
        years_in_business = years_in_business_div.get_text() if years_in_business_div else 'NONE'

        # extract full address and phone number
        info_sec = card.find_next_sibling('div', class_='info-secondary')
        phone_number = info_sec.find('div', class_='phones phone primary').get_text() if info_sec.find('div', class_='phones phone primary') else 'NONE'
        address_div = info_sec.find('div', class_='adr') if info_sec.find('div', class_='adr') else 'NONE'
        full_address = []
        street_address = info_sec.find('div', class_='street-address').get_text() if info_sec.find('div', class_='street-address') else 'NONE'
        full_address = [(address_div.find('div', class_='locality').get_text(), street_address)]

        # extract the price range
        info_sec = card.find_next_sibling('div', class_='info-secondary')
        price_range = info_sec.find('div', class_='price-range').get_text() if info_sec.find('div', class_='price-range') else 'NONE'

        # Append the data to the data_list as a dictionary
        data_list.append({
            'Business Name': business_name,
            'Categories': ', '.join(categories),
            'Ratings': ', '.join(ratings),
            'Snippet': snippet_text,
            'Amenities': ', '.join(amenities),
            'Years in Business': years_in_business,
            'Phone Number': phone_number,
            'Address': ', '.join([f"{locality} {street_address}" for locality, street_address in full_address]),
            'Price Range': price_range
        })

        # Define the CSV file name
        csv_file = 'yellowpages_data.csv'

        # Define the CSV column headers
        fieldnames = ['Business Name', 'Categories', 'Ratings', 'Snippet', 'Amenities', 'Years in Business',
                      'Phone Number', 'Address', 'Price Range']

        # Write the data to a CSV file
        with open(csv_file, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in data_list:
                writer.writerow(data)

        print(f'Data has been saved to {csv_file}')

        '''
        # Print the extracted data for each business
        print(f'Business Name: {business_name}')
        print(f'Categories: {categories}')
        print(f'Ratings: {ratings}')
        print(f'Snippet: {snippet_text}')
        print(f'Amenities: {amenities}')
        print(f'number of years in business: {years_in_business}')
        print(f'Phone Number: {phone_number}')
        print(f'Address: {full_address}')
        print(f'Price Range: {price_range}')
        print('*' * 40)
        '''



