import json
import sys

def validate_data(data):
    """Processes GitHub's complete dispatch payload"""
    try:
        payload = json.loads(data)
        client_payload = payload["client_payload"]
        email = client_payload["email"]
        plan = client_payload["plan"]
        
        validation_errors = []
        
        if "@" not in email or "." not in email.split("@")[-1]:
            validation_errors.append("Invalid email format")
            
        if plan not in ["Free", "Pro", "Enterprise"]:
            validation_errors.append("Invalid plan selected")
            
        if validation_errors:
            return {
                "status": "error",
                "message": " | ".join(validation_errors),
                "valid": False
            }
            
        return {
            "status": "success",
            "message": "Validation passed",
            "valid": True,
            "data": client_payload
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"Validation system error: {str(e)}",
            "valid": False
        }

if __name__ == "__main__":
    try:
        input_data = sys.stdin.read()
        result = validate_data(input_data)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({
            "status": "error",
            "message": f"Runtime error: {str(e)}",
            "valid": False
        }))
        sys.exit(1)
