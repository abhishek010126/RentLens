import streamlit as st

from google import genai



client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


def ask_property_copilot(question, property_data):

    data = st.session_state.get("data", [])

    # User's search requirements
    user_requirements = f"""
Location: {property_data.get("Location", "Not provided")}
BHK: {property_data.get("BHK", "Not provided")}
Budget: {property_data.get("Rent", "Not provided")}
Property Type: {property_data.get("Property_type", "Not provided")}
Furnishing: {property_data.get("Furnishing", "Not provided")}
Preferred Tenant: {property_data.get("Tenant", "Not provided")}
Availability: {property_data.get("Availability", "Not provided")}
Bathrooms: {property_data.get("Bathrooms", "Not provided")}
Parking: {property_data.get("Parking", "Not provided")}
Lease Duration: {property_data.get("Lease", "Not provided")}
"""

    # ALL SEARCHED PROPERTIES
    property_context = ""

    for index, property in enumerate(data, start=1):

        property_context += f"""
PROPERTY {index}

Title: {property.get("title", "Not available")}
Location: {property.get("location", "Not available")}
BHK: {property.get("bhk", "Not available")}
Rent: {property.get("rent", "Not available")}
Area: {property.get("area", "Not available")}
Property Type: {property.get("property_type", "Not available")}
Furnishing: {property.get("furnishing", "Not available")}
Description: {property.get("description", "Not available")}
Source: {property.get("source_name", "Not available")}
URL: {property.get("url", "Not available")}

--------------------------------
"""

    if not data:
        property_context = "No properties were found."


    prompt = f"""
You are RentLens Property Copilot.

USER'S SEARCH REQUIREMENTS:
{user_requirements}

PROPERTIES FOUND BY RENTLENS:
{property_context}

Use BOTH contexts.

The user's requirements tell you what they wanted.

The properties found by RentLens tell you what actually exists.

When the user asks about a property, use the actual property data
from the search results.

When the user asks which property is best, compare ALL available
properties against the user's requirements.

When the user asks to compare properties, compare the actual values.

Rules:
- Never invent missing information.
- If information is unavailable, say so.
- Do not confuse user requirements with property facts.
- Identify properties by their title or PROPERTY number.
- Keep answers practical and concise.

NEGOTIATION MODE:

If the user asks about negotiating rent, or if the user uses the
Negotiation feature, act as a rental negotiation assistant.

Use the actual property information provided in the search results,
especially:

- Current rent
- Location
- BHK
- Area
- Furnishing
- Property type
- Description
- Available amenities/details

Provide:

1. A suggested opening offer.
2. A reasonable target offer.
3. The maximum amount the user should consider paying, if enough
   information is available.
4. The strongest points the user can use during negotiation.
5. A short message the user can send to the landlord/agent.

IMPORTANT:

- Negotiation prices are suggestions, NOT guaranteed market values.
- Never claim that the landlord will accept an offer.
- Never claim that the rent is negotiable unless the listing explicitly
  says so.
- If there is insufficient information to calculate a meaningful offer,
  say so and provide a negotiation strategy instead.
- Do not invent market prices or property conditions.
- Clearly distinguish listing facts from AI recommendations.

USER QUESTION:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

