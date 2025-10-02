import json

# Mock car service data
service_data = {
    "MH12AB1234": {"next_service_date": "2025-11-15"},
    "MH14CD5678": {"next_service_date": "2025-12-01"}
}

def lambda_handler(event, context):
    print("Received event:", event)
    plate_number = event.get("plate_number")

    if not plate_number:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "plate_number is required"})
        }

    if plate_number in service_data:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Next service for {plate_number} is on {service_data[plate_number]['next_service_date']}"
            })
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": f"No service data found for {plate_number}"})
        }
