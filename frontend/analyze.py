import streamlit as st
import pandas as pd
from backend.OCR import extract_property_from_image


def analysis():

    

    uploaded_image = st.file_uploader(
        "Upload property screenshot",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image:

        st.image(
            uploaded_image,
            caption="Property Screenshot",
            width=300
        )

        if st.button(
            "🔍 Analyze Screenshot",
            use_container_width=True
        ):

            with st.spinner("Reading property details..."):

                try:
                    property_data = extract_property_from_image(
                        uploaded_image
                    )

                    st.success("Property information extracted!")

                    st.subheader("🏠 Property Details")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write(
                            f"**Location:** "
                            f"{property_data.location or 'Not found'}"
                        )

                        st.write(
                            f"**BHK:** "
                            f"{property_data.bhk or 'Not found'}"
                        )

                    with col2:
                        rent = property_data.monthly_rent

                        st.write(
                            f"**Monthly Rent:** "
                            f"₹{rent:,}" if rent else
                            "**Monthly Rent:** Not found"
                        )

                        st.write(
                            f"**Area:** "
                            f"{property_data.area_sqft:,} sq.ft"
                            if property_data.area_sqft
                            else
                            "**Area:** Not found"
                        )

                    with col3:
                        st.write(
                            f"**Furnishing:** "
                            f"{property_data.furnishing or 'Not found'}"
                        )

                        deposit = property_data.deposit

                        st.write(
                            f"**Deposit:** "
                            f"₹{deposit:,}" if deposit else
                            "**Deposit:** Not found"
                        )

                except Exception as e:

                    st.error(
                        f"Could not analyze the screenshot: {e}"
                    )