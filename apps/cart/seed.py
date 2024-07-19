import csv
from datetime import datetime
from django.utils import timezone
from apps.cart.models import *
from apps.main.models import Reviews
from django.db.models import Q

# def add_data_from_csv():
#     with open(r"C:\Users\USER\PycharmProjects\Final Year\flipcart _dataset.csv", 'r', encoding='utf-8-sig') as file:
#         reader = csv.DictReader(file, delimiter=',')
#         count = 0  # Initialize a counter
#         for index, row in enumerate(reader):
#             if count >= 10000:  # Check if 1000 rows have been processed
#                 break  # Exit the loop if 1000 rows have been processed
#
#             # Extract categories from the category tree
#             categories = row['product_category_tree'].split(' >> ')
#             gender_cat = categories[1] if len(categories) > 1 else categories[0]
#             sub_cat = categories[0] if len(categories) > 0 else None
#             article_type = categories[2] if len(categories) > 2 else None
#
#             market_price = int(row['Flipkart_retail_price']) if row['Flipkart_retail_price'].strip() else 0
#             discount_price = int(row['discounted_price']) if row['discounted_price'].strip() else 0
#             Amarket_price = int(row['amazon_retail_price']) if row['amazon_retail_price'].strip() else 0
#             Adiscount_price = int(row['amazon_discounted_price']) if row['amazon_discounted_price'].strip() else 0
#
#             product = Product.objects.create(
#                 timestamp = int(row['crawl_timestamp']),
#                 title=row['product_name'],
#                 gender_cat=gender_cat,
#                 sub_cat=sub_cat,
#                 articel_type=article_type,
#                 market_price=market_price,
#                 discount_price=discount_price,
#                 description=row['description'],
#                 new_product_url = row['product_url'],
#                 brand=row['brand'],
#                 size="S",
#                 ama_market_price=Amarket_price,
#                 ama_discount_price=Adiscount_price,
#                 ama_rating = int(row['amazon_discounted_price'])
#             )
#
#             image_urls = row['image'].strip("[]").split(", ")  # Convert string to list of URLs
#             for url in image_urls[:5]:  # Take only the first 5 URLs
#                 ProductImagesURL.objects.create(
#                     product=product,
#                     image_url=url.strip("'\""),  # Remove extra quotes
#                 )
#
#             Reviews.objects.create(
#                 product=product,
#                 user=None,  # You can set the user field if you have user information
#                 name=None,  # Set name and email if available
#                 email=None,
#                 rating=int(row['FlipKart_overall_rating']),
#                 review="",
#                 pros='',
#                 cons='',
#                 created_at=timezone.now(),  # Set the timestamp to current time
#             )
#
#             product.save()
#             count += 1  # Increment the counter after processing each row





def add_data():
    with open(r"C:\Users\USER\OneDrive\Pictures\Product\New folder\amazon_zebronics.csv", 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        count = 0  # Initialize a counter

        for index, row in enumerate(reader):
            market_price_str = row['Orginal_price'].replace(',', '')
            market_price = int(market_price_str) if market_price_str.strip() else 0
            discount_price_str = row['Discount_price'].replace(',', '')
            discount_price = int(discount_price_str) if discount_price_str.strip() else 0
            fmarket_price_str = row['Flipkart_Orginal_price'].replace(',', '')
            fmarket_price = int(fmarket_price_str) if market_price_str.strip() else 0
            fdiscount_price_str = row['Filpkart_Discount_price'].replace(',', '')
            fdiscount_price = int(fdiscount_price_str) if discount_price_str.strip() else 0

            product_url = row['Flipkart_Product URL']
            if not product_url:
                product_url = f"https://www.flipkart.com/search?q={row['Product_name']}"

            product = Product.objects.create(
                timestamp=int(row['Timestamp']) if row['Timestamp'].strip() else 0,
                title=row['Product_name'],
                gender_cat='Electronics',
                sub_cat='Accessories',
                articel_type="Hearphones",
                market_price=market_price,
                discount_price=discount_price,
                description=row['Product_name'],
                new_product_url=row['Product_url'],
                brand='Zebronics',
                size="S",
                ama_market_price=fmarket_price,
                ama_discount_price=fdiscount_price,
                ama_rating=float(row['Filpkart_Rating']),
                ama_url = product_url
            )

            ProductImagesURL.objects.create(
                product=product,
                image_url=row['Image_url'],  # Remove extra quotes
            )

            Reviews.objects.create(
                product=product,
                user=None,  # You can set the user field if you have user information
                name=None,  # Set name and email if available
                email=None,
                rating=float(row['Rating']),
                review="",
                pros='',
                cons='',
                created_at=timezone.now(),  # Set the timestamp to current time
            )

            product.save()
            # count += 1

def change():
    products = Product.objects.all()
    for product in products:
        new_description = product.description.lower()
        new_description = new_description.replace("(refurbished)", "")
        new_description = new_description.replace("(renewed)", "")
        product.description = new_description
        product.save()





def add_data_from_csv():
    with open(r"C:\Users\USER\PycharmProjects\Final Year\flipcart _dataset.csv", 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        count = 0  # Initialize a counter
        for index, row in enumerate(reader):
            # if count >= 10000:  # Check if 1000 rows have been processed
            #     break  # Exit the loop if 1000 rows have been processed

            # Extract categories from the category tree
            categories = row['product_category_tree'].split(' >> ')
            gender_cat = categories[1] if len(categories) > 1 else categories[0]
            sub_cat = categories[0] if len(categories) > 0 else None
            article_type = categories[2] if len(categories) > 2 else None

            # Check if gender_cat contains "Men's" (case-insensitive)
            if "Men's".lower() in gender_cat.lower():
                market_price = int(row['Flipkart_retail_price']) if row['Flipkart_retail_price'].strip() else 0
                discount_price = int(row['discounted_price']) if row['discounted_price'].strip() else 0
                Amarket_price = int(row['amazon_retail_price']) if row['amazon_retail_price'].strip() else 0
                Adiscount_price = int(row['amazon_discounted_price']) if row['amazon_discounted_price'].strip() else 0

                product = Product.objects.create(
                    timestamp = int(row['crawl_timestamp']),
                    title=row['product_name'],
                    gender_cat=gender_cat,
                    sub_cat=sub_cat,
                    articel_type=article_type,
                    market_price=market_price,
                    discount_price=discount_price,
                    description=row['description'],
                    new_product_url = row['product_url'],
                    brand=row['brand'],
                    size="S",
                    ama_market_price=Amarket_price,
                    ama_discount_price=Adiscount_price,
                    ama_rating = int(row['amazon_discounted_price'])
                )

                image_urls = row['image'].strip("[]").split(", ")  # Convert string to list of URLs
                for url in image_urls[:5]:  # Take only the first 5 URLs
                    ProductImagesURL.objects.create(
                        product=product,
                        image_url=url.strip("'\""),  # Remove extra quotes
                    )

                Reviews.objects.create(
                    product=product,
                    user=None,  # You can set the user field if you have user information
                    name=None,  # Set name and email if available
                    email=None,
                    rating=int(row['FlipKart_overall_rating']),
                    review="",
                    pros='',
                    cons='',
                    created_at=timezone.now(),  # Set the timestamp to current time
                )

                product.save()
                # count += 1  # Increment the counter after processing each row