from google import genai
import streamlit as st 


client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


def compare_properties(properties):

    if len(properties) < 2:
        return "Please select at least 2 properties to compare."

    property_text = ""

    for index, property in enumerate(properties, start=1):

        property_text += f"""
PROPERTY {index}

Title: {property.get("title", "Not available")}
Location: {property.get("location", "Not available")}
Rent: {property.get("rent", "Not available")}
BHK: {property.get("bhk", "Not available")}
Area: {property.get("area", "Not available")}
Furnishing: {property.get("furnishing", "Not available")}
Property Type: {property.get("property_type", "Not available")}
Description: {property.get("description", "Not available")}
Source: {property.get("source_name", "Not available")}

"""

    prompt = f"""
You are a rental property comparison assistant.

Compare the following rental properties.

{property_text}

Give a clear comparison for the user.

Include:

1. Best overall property
2. Best value for money
3. Cheapest option
4. Largest property if area information is available
5. Main advantages of each property
6. Main disadvantages of each property
7. Final recommendation

IMPORTANT:
- Only use information provided above.
- Do not invent missing information.
- If information is unavailable, say "Not available".
- Do not assume that a cheaper property is automatically better.
- Consider rent, area, BHK, furnishing, property type and location.
- Keep the answer concise and easy to understand.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
