from pydantic import Field
from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType
import requests

vehicle_protocol = Protocol(name="vehicle_protocol")

class VehicleRequest(Model):
    reg_no: str = Field(description="Vehicle registration number")

async def get_vehicle_details(reg_no, rapidapi_key):
    url = "https://rto-vehicle-information-verification-india.p.rapidapi.com/api/v1/rc/vehicleinfo"
    payload = {
        "reg_no": reg_no,
        "consent": "Y",
        "consent_text": "I hereby declare my consent agreement for fetching my information via AITAN Labs API"
    }
    headers = {
        'x-rapidapi-key': rapidapi_key,
        'x-rapidapi-host': "rto-vehicle-information-verification-india.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

rapidapi_key = ""# Replace with your actual RapidAPI key

@vehicle_protocol.on_message(model=VehicleRequest, replies={UAgentResponse})
async def load_vehicle(ctx: Context, sender: str, msg: VehicleRequest):
    ctx.logger.info(f"Received vehicle request: {msg.reg_no}")
    
    try:
        details = await get_vehicle_details(msg.reg_no, rapidapi_key)
        ctx.logger.info(f"Vehicle details for {msg.reg_no}: {details}")

        if 'error' in details:
            message = f"Error fetching vehicle details: {details['message']}"
        else:
            vehicle_info = details.get('result', {})
            message = (f"Registration Number: {vehicle_info.get('reg_no')}\n"
                       f"Owner: {vehicle_info.get('owner_name')}\n"
                       f"Father's Name: {vehicle_info.get('owner_father_name')}\n"
                       f"Address: {vehicle_info.get('current_address_line1')}, "
                       f"{vehicle_info.get('current_address_line2')}, "
                       f"{vehicle_info.get('current_address_line3')}, "
                       f"{vehicle_info.get('current_district_name')}, "
                       f"{vehicle_info.get('current_state_name')} - "
                       f"{vehicle_info.get('current_pincode')}\n"
                       f"Make: {vehicle_info.get('vehicle_manufacturer_name')}\n"
                       f"Model: {vehicle_info.get('model')}\n"
                       f"Fuel Type: {vehicle_info.get('fuel_descr')}\n"
                       f"Registration Date: {vehicle_info.get('reg_date')}\n"
                       f"Chassis Number: {vehicle_info.get('chassis_no')}\n"
                       f"Engine Number: {vehicle_info.get('engine_no')}\n"
                       f"Color: {vehicle_info.get('color')}\n"
                       f"Insurance Company: {vehicle_info['vehicle_insurance_details'].get('insurance_company_name')}\n"
                       f"Insurance Policy No: {vehicle_info['vehicle_insurance_details'].get('policy_no')}\n"
                       f"Insurance Valid From: {vehicle_info['vehicle_insurance_details'].get('insurance_from')}\n"
                       f"Insurance Valid Upto: {vehicle_info['vehicle_insurance_details'].get('insurance_upto')}\n"
                       f"PUCC No: {vehicle_info['vehicle_pucc_details'].get('pucc_no')}\n"
                       f"PUCC Valid From: {vehicle_info['vehicle_pucc_details'].get('pucc_from')}\n"
                       f"PUCC Valid Upto: {vehicle_info['vehicle_pucc_details'].get('pucc_upto')}\n"
                       f"Tax Amount: {vehicle_info['latest_tax_details'].get('tax_amt')}\n"
                       f"Tax Receipt No: {vehicle_info['latest_tax_details'].get('rcpt_no')}\n"
                       f"Tax Receipt Date: {vehicle_info['latest_tax_details'].get('rcpt_dt')}\n")
    except Exception as e:
        ctx.logger.error(f"An error occurred while fetching vehicle details: {e}")
        message = f"An unexpected error occurred: {e}"

    await ctx.send(sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL))

agent = Agent()
agent.include(vehicle_protocol, publish_manifest=True)
