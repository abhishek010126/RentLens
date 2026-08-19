import streamlit as st
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)



def search_properties(
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
):

    prompt = f"""
Search the web for real rental property listings matching:

Location: {place}
BHK: {bhk_type}
Property Type: {property_type}
Preferred Tenant: {tenant_type}
Furnishing: {furnishing}
Monthly Rent: ₹{budget[0]} to ₹{budget[1]}
Bathrooms: {bathrooms}
Parking: {parking}
Lease Duration: {lease}
Availability: {availability}

Find 5 suitable rental properties.

For each property, use EXACTLY this format:

PROPERTY 1
Title: ...
Location: ...
Rent: ...
BHK: ...
Area: ...
Furnishing: ...
Property Type: ...
Description: ...

PROPERTY 2
Title: ...
Location: ...
Rent: ...
BHK: ...
Area: ...
Furnishing: ...
Property Type: ...
Description: ...

IMPORTANT:
- Only use real properties found through Google Search.
- Do not invent information.
- Each property should be based on information from a web source.
- Do not create URLs yourself.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text, response.candidates[0].grounding_metadata

def parse_properties(text, metadata):

    properties = []


    blocks = text.split("PROPERTY ")

    for block in blocks:

        block = block.strip()

        if not block:
            continue

        property_data = {
            "title": "Not available",
            "location": "Not available",
            "rent": "Not available",
            "bhk": "Not available",
            "area": "Not available",
            "furnishing": "Not available",
            "property_type": "Not available",
            "description": "Not available",
            "url": None,
            "source_name": None
        }


        for line in block.splitlines():

            line = line.strip()

            if line.startswith("Title:"):
                property_data["title"] = line[
                    len("Title:"):
                ].strip()

            elif line.startswith("Location:"):
                property_data["location"] = line[
                    len("Location:"):
                ].strip()

            elif line.startswith("Rent:"):
                property_data["rent"] = line[
                    len("Rent:"):
                ].strip()

            elif line.startswith("BHK:"):
                property_data["bhk"] = line[
                    len("BHK:"):
                ].strip()

            elif line.startswith("Area:"):
                property_data["area"] = line[
                    len("Area:"):
                ].strip()

            elif line.startswith("Furnishing:"):
                property_data["furnishing"] = line[
                    len("Furnishing:"):
                ].strip()

            elif line.startswith("Property Type:"):
                property_data["property_type"] = line[
                    len("Property Type:"):
                ].strip()

            elif line.startswith("Description:"):
                property_data["description"] = line[
                    len("Description:"):
                ].strip()

        properties.append(property_data)


    sources = []

    if metadata:

        chunks = metadata.grounding_chunks or []

        for index, chunk in enumerate(chunks):

            if chunk.web:

                sources.append({
                    "index": index,
                    "title": chunk.web.title,
                    "url": chunk.web.uri
                })


    if metadata:

        supports = metadata.grounding_supports or []

        for support in supports:

            if not support.grounding_chunk_indices:
                continue

            if not support.segment:
                continue

            segment_text = support.segment.text or ""

            # Find which property this citation belongs to
            for property_data in properties:

                title = property_data["title"]

                if (
                    title != "Not available"
                    and title in segment_text
                ):

                    source_index = (
                        support.grounding_chunk_indices[0]
                    )

                    for source in sources:

                        if source["index"] == source_index:

                            property_data["url"] = source["url"]

                            property_data["source_name"] = (
                                source["title"]
                            )

                            break

    return properties




