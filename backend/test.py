from rental_data import process_rental_data

df, city_average, bhk_average = process_rental_data()

print("\n===== CITY AVERAGES =====")
print(city_average)

print("\n===== BHK AVERAGES =====")
print(bhk_average)

print("\n===== LISTINGS =====")
print(df[
    [
        "title",
        "city",
        "bedrooms",
        "price",
        "area_sqft",
        "furnishing",
        "url"
    ]
].head(10))