
from supabase import create_client


SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_PUBLISHABLE_KEY"]

if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL is missing from .env")

if not SUPABASE_KEY:
    raise ValueError("SUPABASE_PUBLISHABLE_KEY is missing from .env")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def sign_up(email, password, name=None):

    return supabase.auth.sign_up({
        "email": email,
        "password": password,
        "options": {
            "data": {
                "name": name
            }
        }
    })


def login(email, password):

    return supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })


def logout():

    return supabase.auth.sign_out()


def get_current_user():

    try:

        response = supabase.auth.get_user()

        return response.user

    except Exception:

        return None

def get_property_count():

    response = supabase.table(
        "properties"
    ).select(
        "id",
        count="exact"
    ).execute()

    return response.count or 0



def save_search(
    user_id,
    location,
    bhk,
    property_type,
    furnishing,
    min_budget,
    max_budget,
    bathrooms,
    parking,
    lease_duration,
    availability
):

    response = supabase.table("searches").insert({
        "user_id": user_id,
        "location": location,
        "bhk": bhk,
        "property_type": property_type,
        "furnishing": furnishing,
        "min_budget": min_budget,
        "max_budget": max_budget,
        "bathrooms": bathrooms,
        "parking": parking,
        "lease_duration": lease_duration,
        "availability": availability
    }).execute()

    return response.data


def get_user_searches(user_id):

    session = supabase.auth.get_session()

    print("SESSION:", session)
    print("USER ID:", user_id)

    response = (
        supabase
        .table("searches")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    print("SUPABASE RESPONSE:", response.data)

    return response.data

def get_search_count(user_id):

    response = (
        supabase
        .table("searches")
        .select("id", count="exact")
        .eq("user_id", user_id)
        .execute()
    )

    return response.count or 0

def get_rental_trends():

    response = (
        supabase
        .table("rental_trends")
        .select("*")
        .order("snapshot_date", desc=True)
        .execute()
    )

    return response.data
