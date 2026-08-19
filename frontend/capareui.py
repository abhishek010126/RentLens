import streamlit as st

from backend.compare import compare_properties


def compare():

    st.title("⚖️ Compare Properties")

    properties = st.session_state.get(
        "compare_list",
        []
    )

    if len(properties) < 2:

        st.warning(
            "Select at least 2 properties to compare."
        )

        return

    st.subheader("Selected Properties")

    for property in properties:

        with st.container(border=True):

            st.subheader(
                property.get(
                    "title",
                    "Property"
                )
            )

            st.write(
                f"📍 {property.get('location', 'Not available')}"
            )

            st.write(
                f"💰 {property.get('rent', 'Not available')}"
            )

            st.write(
                f"🏠 {property.get('bhk', 'Not available')}"
            )

            st.write(
                f"📐 {property.get('area', 'Not available')}"
            )

    st.divider()

    if st.button(
        "🤖 Analyze Comparison",
        use_container_width=True
    ):

        with st.spinner(
            "Analyzing properties..."
        ):

            try:

                result = compare_properties(
                    properties
                )

                st.subheader(
                    "🧠 AI Comparison"
                )

                st.markdown(result)

            except Exception as e:

                st.error(
                    f"Could not compare properties: {e}"
                )