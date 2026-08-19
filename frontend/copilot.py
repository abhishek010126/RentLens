
import streamlit as st
import pandas as pd
from backend.chat_copilot import ask_property_copilot





def set_copilot_question(question):
    st.session_state.copilot_question = question


def property_copilot():

    st.caption("Ask RentLens anything about rental properties.")

    if "selected_details" not in st.session_state:
        st.session_state.selected_details = None

    if "copilot_messages" not in st.session_state:
        st.session_state.copilot_messages = []

    if "copilot_question" not in st.session_state:
        st.session_state.copilot_question = None

    details = st.session_state.selected_details

    if details:

        property_data = {
            "Location": details[9],
            "BHK": details[0],
            "Rent": f"₹{details[4][0]:,} - ₹{details[4][1]:,}",
            "Property_type": details[1],
            "Furnishing": details[3],
            "Tenant": details[2],
            "Availability": details[8],
            "Bathrooms": details[5],
            "Parking": details[6],
            "Lease": details[7]
        }

    else:

        property_data = {
            "Location": "Not filled",
            "BHK": "Not filled",
            "Rent": "Not filled",
            "Property_type": "Not filled",
            "Furnishing": "Not filled",
            "Tenant": "Not filled",
            "Availability": "Not filled",
            "Bathrooms": "Not filled",
            "Parking": "Not filled",
            "Lease": "Not filled"
        }

    with st.container(border=True):

        st.write("### 🏠 Property Details")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                f"📍 **Location**  \n"
                f"{property_data['Location']}"
            )

            st.write(
                f"🛏️ **BHK**  \n"
                f"{property_data['BHK']}"
            )

            st.write(
                f"🚿 **Bathrooms**  \n"
                f"{property_data['Bathrooms']}"
            )

        with col2:

            st.write(
                f"💰 **Rent**  \n"
                f"{property_data['Rent']}"
            )

            st.write(
                f"🏠 **Property Type**  \n"
                f"{property_data['Property_type']}"
            )

            st.write(
                f"🚗 **Parking**  \n"
                f"{property_data['Parking']}"
            )

        with col3:

            st.write(
                f"🛋️ **Furnishing**  \n"
                f"{property_data['Furnishing']}"
            )

            st.write(
                f"👨‍👩‍👦 **Tenant**  \n"
                f"{property_data['Tenant']}"
            )

            st.write(
                f"📅 **Availability**  \n"
                f"{property_data['Availability']}"
            )

    if details:

        st.write("### 💡 Suggested Questions")

        col1, col2 = st.columns(2)

        with col1:

            st.button(
                "💰 Is this rent negotiable?",
                use_container_width=True,
                on_click=set_copilot_question,
                args=(
                    "Is this rent negotiable? What should I negotiate?",
                )
            )

            st.button(
                "⚠️ What are the hidden costs?",
                use_container_width=True,
                on_click=set_copilot_question,
                args=(
                    "What hidden costs should I check before renting this property?",
                )
            )

            st.button(
                "📊 Is this a good deal?",
                use_container_width=True,
                on_click=set_copilot_question,
                args=(
                    "Based on the available information, is this a good rental deal?",
                )
            )

        with col2:

            st.button(
                "📋 What should I ask the landlord?",
                use_container_width=True,
                on_click=set_copilot_question,
                args=(
                    "What questions should I ask the landlord before renting this property?",
                )
            )

            st.button(
                "💸 Estimate my monthly cost",
                use_container_width=True,
                on_click=set_copilot_question,
                args=(
                    "What expenses should I consider in addition to the monthly rent?",
                )
            )

            st.button(
                "🔍 What should I verify?",
                use_container_width=True,
                on_click=set_copilot_question,
                args=(
                    "What information about this property should I verify before signing the lease?",
                )
            )

    for message in st.session_state.copilot_messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    chat_question = st.chat_input(
        "Ask RentLens anything..."
    )

    if chat_question:
        st.session_state.copilot_question = chat_question

    question = st.session_state.copilot_question

    if question:

        st.session_state.copilot_messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            with st.spinner("RentLens is thinking..."):

                try:

                    answer = ask_property_copilot(
                        question,
                        property_data
                    )

                except Exception as e:

                    answer = f"Could not get AI response: {e}"

            st.write(answer)

        st.session_state.copilot_messages.append({
            "role": "assistant",
            "content": answer
        })

        st.session_state.copilot_question = None