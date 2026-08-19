import os

from dotenv import load_dotenv
from apify_client import ApifyClient


load_dotenv()

APIFY_TOKEN = st.secrets["APIFY_API_TOKEN"]

if not APIFY_TOKEN:
    raise ValueError("APIFY_API_TOKEN is missing from .env")


client = ApifyClient(APIFY_TOKEN)


def run_apify_actor(actor_id, run_input):

    try:

        run = client.actor(actor_id).call(
            run_input=run_input
        )

        if not run:
            return []

        dataset = client.dataset(
            run.default_dataset_id
        )

        items = dataset.list_items().items

        return items

    except Exception as e:

        print("Apify error:", e)

        return []
