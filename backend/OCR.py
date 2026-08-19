import streamlit as st
from google import genai
from pydantic import BaseModel
from typing import Optional
import os

from google.genai import types


class PropertyData(BaseModel):
    location: Optional[str] = None
    monthly_rent: Optional[int] = None
    bhk: Optional[str] = None
    area_sqft: Optional[int] = None
    furnishing: Optional[str] = None
    deposit: Optional[int] = None
    property_type: Optional[str] = None
    maintenance: Optional[int] = None




client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


def extract_property_from_image(uploaded_image):

    image_bytes = uploaded_image.getvalue()

    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type=uploaded_image.type
    )

    prompt = """
    Analyze this rental property listing screenshot.

    Extract only information that is actually visible in the image.

    Do not guess missing information.
    If a value is not visible, return null.

    Extract:
    - location
    - monthly rent
    - BHK
    - area in square feet
    - furnishing
    - security deposit
    - property type
    - monthly maintenance
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            image_part,
            prompt
        ],
        config={
            "response_mime_type": "application/json",
            "response_schema": PropertyData,
        }
    )

    return response.parsed
