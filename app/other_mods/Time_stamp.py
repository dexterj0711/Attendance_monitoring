import datetime

def get_current_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now()
    
    # Format the timestamp as a string (optional)
    formatted_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    return formatted_timestamp