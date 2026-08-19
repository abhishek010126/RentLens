import streamlit as st
import pandas as pd

from backend.supabase_config import (
    supabase,
    get_search_count,
    get_user_searches,
    get_rental_trends
)


def dash():

    st.header("Rental market overview at a glance.")


    user = st.session_state.get("user")

    if user is None:

        try:
            user = supabase.auth.get_user().user
        except Exception:
            user = None

    if user:
        search_count = get_search_count(user.id)
    else:
        search_count = 0


    trends = get_rental_trends()


    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.metric(
                "Searches Made",
                search_count
            )

    with col2:

        with st.container(border=True):

            if trends:

                df = pd.DataFrame(trends)

                median = df[
                    "median_rent"
                ].median()

                st.metric(
                    "Median Rent",
                    f"₹{median:,.0f}"
                )

            else:

                st.metric(
                    "Median Rent",
                    "No data"
                )

    with col3:

        with st.container(border=True):

            if trends:

                listings = sum(
                    x["listings"] or 0
                    for x in trends
                )

                st.metric(
                    "Listings Analyzed",
                    listings
                )

            else:

                st.metric(
                    "Listings Analyzed",
                    0
                )

    st.divider()


    with st.container(border=True):

        st.subheader("🕘 Search History")

        if user:

            searches = get_user_searches(user.id)

            if searches:

                for search in searches[:5]:

                    location = search.get(
                        "location",
                        "Unknown"
                    )

                    bhk = search.get(
                        "bhk",
                        "BHK"
                    )

                    property_type = search.get(
                        "property_type",
                        "Property"
                    )

                    minimum = search.get(
                        "min_budget"
                    )

                    maximum = search.get(
                        "max_budget"
                    )

                    if (
                        minimum is not None
                        and maximum is not None
                    ):

                        budget = (
                            f"₹{minimum:,} – ₹{maximum:,}"
                        )

                    else:

                        budget = "Budget not specified"

                    st.write(
                        f"📍 **{location}**"
                    )

                    st.caption(
                        f"{bhk} • "
                        f"{property_type} • "
                        f"{budget}"
                    )

                    st.divider()

            else:

                st.info(
                    "No previous searches yet."
                )

        else:

            st.info(
                "Login to see your search history."
            )

    st.divider()



    with st.container(border=True):

        st.subheader("📊 Average Rent by City")

        if trends:

            df = pd.DataFrame(trends)

            chart = df[
                [
                    "city",
                    "average_rent"
                ]
            ].set_index("city")

            st.bar_chart(
                chart,
                color="#35C98A"
            )

        else:

            st.info(
                "Rental data is not available yet."
            )

    st.divider()

    
    with st.container(border=True):

        st.subheader("🇮🇳 India Rental Trends")

        if trends:

            df = pd.DataFrame(trends)

            table = df[
                [
                    "city",
                    "average_rent",
                    "median_rent",
                    "listings"
                ]
            ].copy()

            table.columns = [
                "City",
                "Average Rent",
                "Median Rent",
                "Listings"
            ]

            table["Average Rent"] = (
                table["Average Rent"]
                .apply(
                    lambda x:
                    f"₹{x:,.0f}"
                    if pd.notna(x)
                    else "—"
                )
            )

            table["Median Rent"] = (
                table["Median Rent"]
                .apply(
                    lambda x:
                    f"₹{x:,.0f}"
                    if pd.notna(x)
                    else "—"
                )
            )

            st.dataframe(
                table,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "Rental data is not available yet."
            )

    st.divider()


    with st.container(border=True):

        st.subheader("🏠 Rent by BHK")

        if trends:

            df = pd.DataFrame(trends)

            bhk = df[
                [
                    "city",
                    "one_bhk_average",
                    "two_bhk_average",
                    "three_bhk_average"
                ]
            ].copy()

            bhk.columns = [
                "City",
                "1 BHK",
                "2 BHK",
                "3 BHK"
            ]

            bhk["1 BHK"] = (
                bhk["1 BHK"]
                .apply(
                    lambda x:
                    f"₹{x:,.0f}"
                    if pd.notna(x)
                    else "—"
                )
            )

            bhk["2 BHK"] = (
                bhk["2 BHK"]
                .apply(
                    lambda x:
                    f"₹{x:,.0f}"
                    if pd.notna(x)
                    else "—"
                )
            )

            bhk["3 BHK"] = (
                bhk["3 BHK"]
                .apply(
                    lambda x:
                    f"₹{x:,.0f}"
                    if pd.notna(x)
                    else "—"
                )
            )

            st.dataframe(
                bhk,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "BHK data is not available yet."
            )
    