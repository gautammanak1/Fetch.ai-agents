from pydantic import Field
from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType

# Define the protocol for event-related messages
event_protocol = Protocol(name="event_protocol")

# Define the model for event requests
class EventRequest(Model):
    event_description: str = Field(description="Give details of the event you are looking for")
    location: str = Field(default=None, description="Location of the event")

# Define the model for location requests
class LocationRequest(Model):
    location: str = Field(description="Please provide the location")

# Static event data (replace this with API call if available)
event_data = [
    {
        "date": "Sunday, Jul 28th, 2024",
        "eventName": "Transforming AI: Insights from \"Attention is All You Need\" | ML Paper Reading Clubs Day 2",
        "communityName": "TensorFlow User Group Islamabad",
        "location": "Islamabad",
        "url": "https://www.commudle.com/communities/TFUGIslamabad/events/transforming-ai-insights-from-attention-is-all-you-need-ml-paper-reading-clubs-day-2"
    },
    {
        "date": "Saturday, Aug 3rd, 2024",
        "eventName": "Meetup Zero: Gen AI Edition",
        "communityName": "TensorFlow User Group Ghaziabad",
        "location": "Ghaziabad",
        "url": "https://www.commudle.com/communities/tensorflow-user-group-ghaziabad/events/meetup-zero-gen-ai-edition"
    },
    {
        "date": "Saturday, Aug 3rd, 2024",
        "eventName": "Bridging the Gap: Transitioning from Traditional Systems to ML Deployments | ML Study Jams Day 10",
        "communityName": "TensorFlow User Group Islamabad",
        "location": "Islamabad",
        "url": "https://www.commudle.com/communities/TFUGIslamabad/events/bridging-the-gap-transitioning-from-traditional-systems-to-ml-deployments-ml-study-jams-day-10"
    },
    {
        "date": "Sunday, Aug 4th, 2024",
        "eventName": "Google IO Extended",
        "communityName": "GDG Noida",
        "location": "Noida",
        "url": "https://www.commudle.com/communities/gdg-noida/events/google-io-extended-97e25a74-bdcb-47f2-b226-e48eb149944e"
    },
    {
        "date": "Thursday, Aug 29th, 2024",
        "eventName": "Season of AI - Getting started with Azure AI Studio",
        "communityName": "MLSA MIET",
        "location": "Meerut",
        "url": "https://www.commudle.com/communities/microsoft-learn-student-ambassadors-meerut-institute-of-engineering-and-technology/events/season-of-ai-getting-started-with-azure-ai-studio"
    }
]

async def get_event_details(event_description, location):
    # Filter events based on the description and location
    return [event for event in event_data if event_description.lower() in event['eventName'].lower() and location.lower() in event['location'].lower()]

@event_protocol.on_message(model=EventRequest, replies={UAgentResponse, LocationRequest})
async def load_event(ctx: Context, sender: str, msg: EventRequest):
    ctx.logger.info(f"Received event request: {msg.event_description}, Location: {msg.location}")
    
    if not msg.location:
        # Ask for the location if it's not provided
        await ctx.send(sender, LocationRequest(location="Please provide the location"))
    else:
        try:
            details = await get_event_details(msg.event_description, msg.location)
            ctx.logger.info(f"Event details for {msg.event_description} in {msg.location}: {details}")

            # Check if details contain any events
            if not details:
                message = "No events found matching your criteria."
            else:
                message = ""
                for detail in details:
                    ctx.logger.info(detail)
                    event_url = detail.get('url')
                    event_name = detail.get('eventName')
                    community_name = detail.get('communityName')
                    event_date = detail.get('date')

                    message += (f"<a href='{event_url}'>{event_name}</a>\n"
                                f"Community: {community_name}\n"
                                f"Date: {event_date}\n\n")
        except Exception as e:
            ctx.logger.error(f"An error occurred while fetching event details: {e}")
            message = f"An unexpected error occurred: {e}"

        await ctx.send(sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL))

@event_protocol.on_message(model=LocationRequest, replies={EventRequest})
async def request_location(ctx: Context, sender: str, msg: LocationRequest):
    ctx.logger.info(f"Received location request: {msg.location}")
    
    # Update the original event request with the location provided
    updated_event_request = EventRequest(event_description=msg.location.split(" ")[-1], location=msg.location)
    
    # Send the updated event request back to the load_event function
    await ctx.send(sender, updated_event_request)

agent = Agent()
agent.include(event_protocol, publish_manifest=True)
