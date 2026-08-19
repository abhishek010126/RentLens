
import pandas as pd


from apify_client import ApifyClient

from supabase_config import supabase




APIFY_API_TOKEN = st.secrets["APIFY_API_TOKEN"]

client = ApifyClient(APIFY_API_TOKEN)


def get_latest_apify_data():

    runs = client.actor(
        "benthepythondev/magicbricks-scraper"
    ).runs().list(
        limit=1
    )

    if not runs.items:
        print("No Apify runs found.")
        return []

    latest_run = runs.items[0]

    dataset_id = latest_run.default_dataset_id

    items = list(
        client.dataset(dataset_id).iterate_items()
    )

    print(f"Loaded {len(items)} listings.")

    return items


def process_and_save():

    properties = get_latest_apify_data()

    if not properties:
        return

    df = pd.DataFrame(properties)

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df["bedrooms"] = pd.to_numeric(
        df["bedrooms"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["city", "price"]
    )

    df = df[
        (df["price"] >= 5000) &
        (df["price"] <= 100000)
    ]

    today = pd.Timestamp.now().date()

    for city, city_df in df.groupby("city"):

        average_rent = city_df["price"].mean()
        median_rent = city_df["price"].median()

        one_bhk = city_df[
            city_df["bedrooms"] == 1
        ]["price"].mean()

        two_bhk = city_df[
            city_df["bedrooms"] == 2
        ]["price"].mean()

        three_bhk = city_df[
            city_df["bedrooms"] == 3
        ]["price"].mean()

        row = {
            "city": city,
            "average_rent": round(average_rent),
            "median_rent": round(median_rent),
            "listings": len(city_df),
            "one_bhk_average": (
                round(one_bhk)
                if pd.notna(one_bhk)
                else None
            ),
            "two_bhk_average": (
                round(two_bhk)
                if pd.notna(two_bhk)
                else None
            ),
            "three_bhk_average": (
                round(three_bhk)
                if pd.notna(three_bhk)
                else None
            ),
            "snapshot_date": str(today)
        }

        supabase.table(
            "rental_trends"
        ).insert(row).execute()

        print(f"Saved {city}")


if __name__ == "__main__":

    print("Updating rental market data...")

    process_and_save()

    print("Done.")
