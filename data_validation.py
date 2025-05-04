def validate_data(data):  
    if "@" not in data["email"]:  
        return {"status": "error", "message": "Invalid email"}  
    elif data["plan"] not in ["Free", "Pro", "Enterprise"]:  
        return {"status": "error", "message": "Invalid plan"}  
    else:  
        return {"status": "success"}  
