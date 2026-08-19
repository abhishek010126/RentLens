
import pandas as pd

import streamlit as st 
from apify_client import ApifyClient




APIFY_API_TOKEN = st.secrets["APIFY_API_TOKEN"]

if not APIFY_API_TOKEN:
    raise ValueError("APIFY_API_TOKEN is missing from .env")

client = ApifyClient(APIFY_API_TOKEN)


CITIES = [
    "Mumbai",
    "Bangalore",
    "New Delhi",
    "Noida",
    "Hyderabad",
    "Pune",
    "Chennai",
    "Kolkata",
    "Ahmedabad"
]


def get_rental_data():

    actor_id = "benthepythondev/magicbricks-scraper"

    run_input = {
        "cities": CITIES,

        "transaction": "rent",

        "minPrice": 5000,

        "maxPrice": 100000,

        "maxResultsPerSearch": 50,

        "maxPagesPerSearch": 1
    }

    print("Starting Apify...")

    run = client.actor(actor_id).call(
        run_input=run_input
    )

    dataset_id = run.default_dataset_id

    items = list(
        client.dataset(dataset_id).iterate_items()
    )

    print(f"Listings received: {len(items)}")

    return items


def process_rental_data():

    properties = get_rental_data()

    if not properties:
        print("No properties found.")
        return None, None, None, None

    df = pd.DataFrame(properties)

    # --------------------------------
    # Make sure required columns exist
    # --------------------------------

    required_columns = [
        "city",
        "price",
        "bedrooms",
        "area_sqft",
        "price_per_sqft",
        "furnishing",
        "property_type",
        "url",
        "title"
    ]

    for column in required_columns:

        if column not in df.columns:
            df[column] = None

    # --------------------------------
    # Convert numeric columns
    # --------------------------------

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df["bedrooms"] = pd.to_numeric(
        df["bedrooms"],
        errors="coerce"
    )

    df["area_sqft"] = pd.to_numeric(
        df["area_sqft"],
        errors="coerce"
    )

    df["price_per_sqft"] = pd.to_numeric(
        df["price_per_sqft"],
        errors="coerce"
    )

    # --------------------------------
    # Remove invalid listings
    # --------------------------------

    df = df.dropna(
        subset=[
            "city",
            "price"
        ]
    )

    # --------------------------------
    # Keep reasonable rental prices
    # --------------------------------

    df = df[
        (df["price"] >= 5000) &
        (df["price"] <= 100000)
    ]

    # =================================
    # CITY STATISTICS
    # =================================

    city_stats = (
        df.groupby("city")["price"]
        .agg(
            Average_Rent="mean",
            Median_Rent="median",
            Listings="count"
        )
        .round()
        .reset_index()
    )

    city_stats.columns = [
        "City",
        "Average Rent",
        "Median Rent",
        "Listings"
    ]

    # =================================
    # BHK STATISTICS
    # =================================

    # Only use 1, 2 and 3 BHK
    bhk_df = df[
        df["bedrooms"].isin([1, 2, 3])
    ]

    bhk_stats = (
        bhk_df
        .groupby(
            ["city", "bedrooms"]
        )["price"]
        .agg(
            Average_Rent="mean",
            Median_Rent="median",
            Listings="count"
        )
        .round()
        .reset_index()
    )

    bhk_stats.columns = [
        "City",
        "BHK",
        "Average Rent",
        "Median Rent",
        "Listings"
    ]

    # =================================
    # CITY + BHK COMBINED DATA
    # =================================

    city_bhk_stats = (
        bhk_df
        .groupby(
            ["city", "bedrooms"]
        )["price"]
        .mean()
        .round()
        .reset_index()
    )

    city_bhk_stats.columns = [
        "City",
        "BHK",
        "Average Rent"
    ]

    # =================================
    # RENT PER SQFT
    # =================================

    sqft_stats = (
        df.dropna(
            subset=["price_per_sqft"]
        )
        .groupby("city")["price_per_sqft"]
        .mean()
        .round(2)
        .reset_index()
    )

    sqft_stats.columns = [
        "City",
        "Average Rent Per Sqft"
    ]

    # =================================
    # FURNISHING DISTRIBUTION
    # =================================

    furnishing_stats = (
        df["furnishing"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
    )

    furnishing_stats.columns = [
        "Furnishing",
        "Listings"
    ]

    # =================================
    # PROPERTY TYPE DISTRIBUTION
    # =================================

    property_type_stats = (
        df["property_type"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
    )

    property_type_stats.columns = [
        "Property Type",
        "Listings"
    ]

    return (
        df,
        city_stats,
        bhk_stats,
        city_bhk_stats
    )


if __name__ == "__main__":

    (
        df,
        city_stats,
        bhk_stats,
        city_bhk_stats
    ) = process_rental_data()

    print("\n==============================")
    print("CITY STATISTICS")
    print("==============================")

    print(city_stats.to_string(index=False))

    print("\n==============================")
    print("BHK STATISTICS")
    print("==============================")

    print(bhk_stats.to_string(index=False))

    print("\n==============================")
    print("CITY + BHK")
    print("==============================")

    print(city_bhk_stats.to_string(index=False))

    print("\n==============================")
    print("TOTAL LISTINGS")
    print("==============================")

    print(len(df))
