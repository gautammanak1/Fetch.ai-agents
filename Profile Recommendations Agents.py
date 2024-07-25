import requests
from pydantic import Field
from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType

# Create an instance of ProfileProtocol
profile_protocol = Protocol(name="profile_protocol")

class ProfileRequest(Model):
    profile_description: str = Field(description="Give details of the profile you are looking for")

# Function to get profile details from the API
async def get_profile_details(profile_description, rapidapi_key):
    url = "https://linkedin-data-api.p.rapidapi.com/search-people"
    
    # Placeholder for India's location code. Replace with actual geo code if known.
    india_geo_code = "103644278"
    
    querystring = {
        "keywords": profile_description,
        "start": "0",
        "geo": india_geo_code,
        "count": "10"  # Limit results to 10 for easier debugging
    }
    
    headers = {
        'x-rapidapi-key': rapidapi_key,
        'x-rapidapi-host': "linkedin-data-api.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

# Hardcoded value for RapidAPI key
rapidapi_key = ""  # Replace with your actual RapidAPI key

@profile_protocol.on_message(model=ProfileRequest, replies={UAgentResponse})
async def load_profile(ctx: Context, sender: str, msg: ProfileRequest):
    ctx.logger.info(f"Received profile request: {msg.profile_description}")
    
    try:
        details = await get_profile_details(msg.profile_description, rapidapi_key)
        ctx.logger.info(f"Profile details for {msg.profile_description}: {details}")
        message = ""
        if details and details.get('data', {}).get('items'):
            for detail in details['data']['items']:
                # Extracting profile details
                profile_url = detail.get('profileURL', 'N/A')
                profile_name = detail.get('fullName', 'N/A')
                profile_title = detail.get('headline', 'N/A')
                profile_location = detail.get('location', 'N/A')
                profile_summary = detail.get('summary', 'N/A')

                # Formatting the message
                message += (f"<a href='{profile_url}'>{profile_name}</a>\n"
                            f"Title: {profile_title}\n"
                            f"Location: {profile_location}\n"
                            f"Summary: {profile_summary}\n\n")
        else:
            message = "No profiles found."
    except Exception as e:
        ctx.logger.error(f"An error occurred while fetching profile details: {e}")
        message = f"An unexpected error occurred: {e}"

    await ctx.send(sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL))

# Include the protocol in the agent
agent = Agent()  # Initialize the agent
agent.include(profile_protocol, publish_manifest=True)
