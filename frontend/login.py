import streamlit as st

from backend.supabase_config import (
    supabase,
    login,
    sign_up
)


def login_page():

    st.title("🏠 RentLens")

    st.caption(
        "Sign in to save properties and access your rental history."
    )

    # --------------------------------
    # SESSION STATE
    # --------------------------------

    if "user" not in st.session_state:
        st.session_state.user = None

    if "session" not in st.session_state:
        st.session_state.session = None

    # --------------------------------
    # ALREADY LOGGED IN
    # --------------------------------

    if st.session_state.user:

        st.success(
            f"Logged in as {st.session_state.user.email}"
        )

        if st.button(
            "Logout",
            use_container_width=True
        ):

            try:
                supabase.auth.sign_out()
            except Exception:
                pass

            st.session_state.user = None
            st.session_state.session = None

            st.rerun()

        return

    # --------------------------------
    # LOGIN / SIGNUP TABS
    # --------------------------------

    tab1, tab2 = st.tabs([
        "Login",
        "Create Account"
    ])

    # =================================
    # LOGIN
    # =================================

    with tab1:

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):

            # Check inputs

            if not email.strip() or not password:

                st.write("EMAIL:", repr(email))
                st.write("PASSWORD ENTERED:", bool(password))

                st.warning(
                    "Please enter your email and password."
                )

            else:

                try:

                    with st.spinner(
                        "Logging in..."
                    ):

                        response = login(
                            email.strip(),
                            password
                        )

                    # -------------------------
                    # SAVE USER + SESSION
                    # -------------------------

                    if response.user:

                        st.session_state.user = (
                            response.user
                        )

                        st.session_state.session = (
                            response.session
                        )

                        st.success(
                            "Login successful!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Login failed. Please check your credentials."
                        )

                except Exception as e:

                    st.error(
                        f"Login failed: {e}"
                    )

    # =================================
    # CREATE ACCOUNT
    # =================================

    with tab2:

        name = st.text_input(
            "Name",
            key="signup_name"
        )

        signup_email = st.text_input(
            "Email",
            key="signup_email"
        )

        signup_password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="signup_confirm"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            # -------------------------
            # VALIDATION
            # -------------------------

            if (
                not name.strip()
                or not signup_email.strip()
                or not signup_password
            ):

                st.warning(
                    "Please fill all fields."
                )

            elif signup_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif len(signup_password) < 6:

                st.error(
                    "Password must be at least 6 characters."
                )

            else:

                try:

                    with st.spinner(
                        "Creating account..."
                    ):

                        response = sign_up(
                            signup_email.strip(),
                            signup_password,
                            name.strip()
                        )

                    # -------------------------
                    # ACCOUNT CREATED
                    # -------------------------

                    if response.user:

                        st.success(
                            "Account created successfully!"
                        )

                        st.info(
                            "Check your email to confirm your account."
                        )

                    else:

                        st.error(
                            "Account could not be created."
                        )

                except Exception as e:

                    st.error(
                        f"Signup failed: {e}"
                    )