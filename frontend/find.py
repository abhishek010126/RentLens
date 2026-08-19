import streamlit as st

from backend.finding import (
    search_properties,
    parse_properties
)



from backend.supabase_config import (
    supabase
)


def find():


    if "selected_details" not in st.session_state:
        st.session_state.selected_details = None

    if "properties" not in st.session_state:
        st.session_state.properties = []

    if "compare_list" not in st.session_state:
        st.session_state.compare_list = []
    if "data" not in st.session_state:
        st.session_state.data = []


    st.write(
        "Find rental properties based on your requirements."
    )


    place = st.text_input(
        "Where do you want the Property?",
        placeholder="e.g. Sector 62, Noida"
    )


    col1, col2 = st.columns(2)

    with col1:

        bhk_type = st.selectbox(
            "BHK Type",
            [
                "1BHK",
                "2BHK",
                "3BHK",
                "4BHK",
                "4+BHK"
            ]
        )

        property_type = st.radio(
            "Property Type",
            [
                "Gated Societies",
                "Apartment",
                "Independent House/Villa",
                "Gated Community Villa"
            ],
            horizontal=True
        )


    with col2:

        tenant_type = st.selectbox(
            "Preferred Tenants",
            [
                "Family",
                "Company",
                "Bachelor Male",
                "Bachelor Female"
            ]
        )

        furnishing = st.selectbox(
            "Furnishing",
            [
                "Full",
                "Semi",
                "None"
            ]
        )


    budget = st.slider(
        "Monthly Rent Budget",
        min_value=5000,
        max_value=100000,
        value=(15000, 30000),
        step=1000
    )


    col1, col2 = st.columns(2)

    with col1:

        bathrooms = st.selectbox(
            "Bathrooms",
            [
                "Any",
                "1",
                "2",
                "3",
                "4+"
            ]
        )

        parking = st.selectbox(
            "Parking",
            [
                "Any",
                "1 Car",
                "2 Cars",
                "Bike Only"
            ]
        )


    with col2:

        lease = st.selectbox(
            "Lease Duration",
            [
                "Any",
                "6 Months",
                "11 Months",
                "1 Year+"
            ]
        )

        availability = st.selectbox(
            "Availability",
            [
                "Any",
                "Immediately",
                "Within 15 Days",
                "Within 30 Days"
            ]
        )


    st.write("")


    if st.button(
        "🔍 Find Properties",
        use_container_width=True
    ):

        if not place:

            st.warning(
                "Please enter a location."
            )

            return


    
        st.session_state.compare_list = []


        with st.spinner(
            "Searching rental properties..."
        ):

            try:


                result_text, metadata = search_properties(

                    place,
                    bhk_type,
                    property_type,
                    tenant_type,
                    furnishing,
                    budget,
                    bathrooms,
                    parking,
                    lease,
                    availability
                )


                properties = parse_properties(
                    result_text,
                    metadata
                )


                st.session_state.properties = properties
                st.session_state.data = properties



                try:

                    user = (
                        supabase
                        .auth
                        .get_user()
                        .user
                    )

                except Exception:

                    user = None



                if user:

                    supabase.table(
                        "searches"
                    ).insert({

                        "user_id": user.id,

                        "location": place,

                        "bhk": bhk_type,

                        "property_type": property_type,

                        "furnishing": furnishing,

                        "min_budget": budget[0],

                        "max_budget": budget[1],

                        "bathrooms": bathrooms,

                        "parking": parking,

                        "lease_duration": lease,

                        "availability": availability

                    }).execute()



                st.session_state.selected_details = (

                    bhk_type,
                    property_type,
                    tenant_type,
                    furnishing,
                    budget,
                    bathrooms,
                    parking,
                    lease,
                    availability,
                    place

                )


            except Exception as e:

                st.error(
                    f"Could not search properties: {e}"
                )

                return




    properties = st.session_state.properties


    if properties:

        st.divider()

        st.subheader(
            "🏠 Properties Found"
        )


        for index, property in enumerate(properties):

            
            if (
                property.get("title", "")
                .lower()
                == "not available"
            ):
                continue


            with st.container(
                border=True
            ):


                st.subheader(
                    f"🏠 {property.get('title', 'Property')}"
                )



                col1, col2, col3 = st.columns(3)


                with col1:

                    st.write(
                        f"📍 **Location:** "
                        f"{property.get('location', 'Not available')}"
                    )

                    st.write(
                        f"🛏️ **BHK:** "
                        f"{property.get('bhk', 'Not available')}"
                    )


                with col2:

                    st.write(
                        f"💰 **Rent:** "
                        f"{property.get('rent', 'Not available')}"
                    )

                    st.write(
                        f"📐 **Area:** "
                        f"{property.get('area', 'Not available')}"
                    )


                with col3:

                    st.write(
                        f"🛋️ **Furnishing:** "
                        f"{property.get('furnishing', 'Not available')}"
                    )

                    st.write(
                        f"🏠 **Type:** "
                        f"{property.get('property_type', 'Not available')}"
                    )


            

                description = property.get(
                    "description"
                )

                if description:

                    st.write(
                        description
                    )

                source_name = property.get(
                    "source_name"
                )

                if source_name:

                    st.caption(
                        f"Source: {source_name}"
                    )


                url = property.get(
                    "url"
                )

                if url:

                    st.link_button(
                        "🔗 View Original Listing",
                        url,
                        use_container_width=True
                    )

                else:

                    st.caption(
                        "Listing URL unavailable"
                    )



                if st.checkbox(
                    "Compare",
                    key=f"compare_{index}"
                ):

                    if (
                        property
                        not in
                        st.session_state.compare_list
                    ):

                        st.session_state.compare_list.append(
                            property
                        )

                else:

                    if (
                        property
                        in
                        st.session_state.compare_list
                    ):

                        st.session_state.compare_list.remove(
                            property
                        )



        if st.session_state.compare_list:

            st.divider()

            count = len(
                st.session_state.compare_list
            )

            st.info(
                f"⚖️ {count} "
                f"property{'ies' if count != 1 else ''} "
                f"selected for comparison."
            )



            if st.button(
                "Clear Comparison"
            ):

                st.session_state.compare_list = []

                st.rerun()


            if len(
                st.session_state.compare_list
            ) >= 2:

                if st.button(
                    "⚖️ Compare Properties",
                    use_container_width=True
                ):

                    st.session_state.page = "Compare"

                    

                    st.rerun()
                   
                                   

                



