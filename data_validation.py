import json
import sys

def validate_data(data):
    """Expects GitHub's nested client_payload structure"""
    try:
        payload = json.loads(data)
        email = payload["client_payload"]["email"]
        plan = payload["client_payload"]["plan"]
        
        if "@" not in email:
            return {"status": "error", "message": "Invalid email"}
        elif plan not in ["Free", "Pro", "Enterprise"]:
            return {"status": "error", "message": "Invalid plan"}
        else:
            return {"status": "success"}
    
    except Exception as e:
        return {"status": "error", "message": f"Validation failed: {str(e)}"}

if __name__ == "__main__":
    # Read JSON from stdin (how GitHub Actions passes it)
    input_data = sys.stdin.read()
    result = validate_data(input_data)
    print(json.dumps(result))
