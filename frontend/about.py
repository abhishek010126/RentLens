import streamlit as st


def about():

    st.title("🏠 About RentLens")

    st.markdown(
        """
        ### Smarter rental decisions, not just rental searches.

        **RentLens** is an AI-powered rental intelligence platform designed
        to help users discover, evaluate, and compare rental properties
        before making a decision.

        Instead of simply showing listings, RentLens combines property
        discovery, market data, AI-powered visual analysis, and property
        comparison into one platform.
        """
    )

    st.divider()

    # ==========================================
    # WHAT RENTLENS DOES
    # ==========================================

    st.subheader("🚀 What is RentLens?")

    st.write(
        """
        Finding a rental property can involve comparing dozens of listings,
        understanding whether the asking price is reasonable, checking the
        condition of a property, and deciding which option actually provides
        the best value.

        RentLens brings these steps together into a single workflow.
        """
    )

    # ==========================================
    # CORE FEATURES
    # ==========================================

    st.subheader("✨ Core Features")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown("### 🔍 Find Properties")

            st.write(
                """
                Search for rental properties using requirements such as
                location, BHK, budget, furnishing, tenant type, parking,
                bathrooms, lease duration, and availability.
                """
            )


        with st.container(border=True):

            st.markdown("### 📷 AI Property Analysis")

            st.write(
                """
                Upload a screenshot or image of a property along with its
                details. Gemini Vision analyzes the available information
                and provides an AI-generated property score, insights,
                advantages, and potential concerns.
                """
            )


        with st.container(border=True):

            st.markdown("### 🧠 Property Copilot")

            st.write(
                """
                Ask questions about rental properties and get contextual
                AI assistance for evaluating listings and understanding
                property information.
                """
            )


    with col2:

        with st.container(border=True):

            st.markdown("### ⚖️ Property Comparison")

            st.write(
                """
                Select multiple properties and compare them together.
                RentLens brings the selected property information into one
                place so users can quickly understand differences in rent,
                area, BHK, furnishing, property type, and other available
                details.
                """
            )


        with st.container(border=True):

            st.markdown("### 📊 Rental Market Dashboard")

            st.write(
                """
                View rental-market information through KPI cards,
                statistics, charts, and market insights to understand
                rental prices and activity at a glance.
                """
            )


        with st.container(border=True):

            st.markdown("### 🕘 Search History")

            st.write(
                """
                Authenticated users can save their rental searches and
                access their previous search activity through Supabase.
                """
            )

    st.divider()

    # ==========================================
    # HOW IT WORKS
    # ==========================================

    st.subheader("⚙️ How RentLens Works")

    steps = [
        (
            "01",
            "Define your requirements",
            "Enter your preferred location, budget, BHK, furnishing and other rental requirements."
        ),
        (
            "02",
            "Discover properties",
            "RentLens searches for relevant rental listings and presents the available property information."
        ),
        (
            "03",
            "Analyze",
            "Use AI-powered property analysis to evaluate a listing and, when available, analyze its property image."
        ),
        (
            "04",
            "Compare",
            "Select properties that interest you and compare them side by side."
        ),
        (
            "05",
            "Make a decision",
            "Use the property data, market information, comparison results and AI insights to make a more informed rental decision."
        )
    ]

    for number, title, description in steps:

        col1, col2 = st.columns([1, 5])

        with col1:

            st.markdown(
                f"## {number}"
            )

        with col2:

            st.markdown(
                f"### {title}"
            )

            st.write(
                description
            )

    st.divider()

    # ==========================================
    # TECHNOLOGY
    # ==========================================

    st.subheader("🛠️ Technology Behind RentLens")

    tech_col1, tech_col2, tech_col3 = st.columns(3)

    with tech_col1:

        st.markdown("### Frontend")

        st.write(
            """
            • Streamlit  
            • Python  
            • Interactive dashboards  
            • Session state
            """
        )

    with tech_col2:

        st.markdown("### AI & Data")

        st.write(
            """
            • Google Gemini  
            • Gemini Vision  
            • Pandas  
            • Property data processing
            """
        )

    with tech_col3:

        st.markdown("### Backend")

        st.write(
            """
            • Supabase  
            • Authentication  
            • Search history  
            • Database storage
            """
        )

    st.divider()

    # ==========================================
    # AI
    # ==========================================

    st.subheader("🤖 AI at the Core")

    st.write(
        """
        RentLens does not use AI simply as a generic chatbot.

        Gemini is integrated into specific parts of the rental workflow,
        including property analysis, image understanding, and contextual
        property assistance.

        This allows AI to work alongside structured property data rather
        than replacing the entire application with a chat interface.
        """
    )

    st.divider()

    # ==========================================
    # DECISION WORKFLOW
    # ==========================================

    st.subheader("🎯 From Search to Decision")

    st.markdown(
        """
        **Find → Analyze → Compare → Understand → Decide**
        """
    )

    st.write(
        """
        RentLens is designed around the idea that finding a property is
        only the first step. The real problem is deciding whether a
        property is actually worth considering.

        RentLens brings the information required for that decision into
        one workflow.
        """
    )

    st.divider()

    # ==========================================
    # PROJECT
    # ==========================================

    st.subheader("💡 Why RentLens?")

    st.write(
        """
        Rental platforms often focus primarily on listing discovery.
        RentLens focuses on the decision that comes after discovery:

        **Which property makes the most sense for me?**

        By combining rental search, structured property information,
        market insights, multimodal AI analysis, and comparison tools,
        RentLens aims to make that decision faster and more informed.
        """
    )

    st.divider()

    # ==========================================
    # PROJECT INFORMATION
    # ==========================================

    st.subheader("📌 Project Information")

    st.write(
        """
        **Project:** RentLens  
        **Category:** AI + Real Estate / Rental Intelligence  
        **Built with:** Python, Streamlit, Gemini, Supabase and data-processing tools
        """
    )

    st.caption(
        "RentLens — Find smarter. Analyze deeper. Decide better."
    )

    st.divider()

    st.markdown(
        """
        <div style="text-align:center; padding:20px 0;">
            <h3>RentLens</h3>
            <p>Explore smarter. Understand the market. Rent better.</p>
        </div>
        """,
        unsafe_allow_html=True
    )