from langchain_core.tools import tool
from datetime import datetime

# Storage for all mission logs. 
# Key: log_id (int or str)
# Value: Dictionary containing {'content': str, 'timestamp': str}
MISSION_LOGS = {}
# Simple counter for generating unique log IDs
LOG_ID_COUNTER = 0

@tool
def create_mission_log(content: str) -> str:
    """Create a new misson log entry.
    
    Use this when the crew needs to:
    - Record important events
    - Create task reminders
    - Document observations
    
    Args:
        content: The mission log entry text
        
    Returns:
        Confirmation with log id
    """

    # You MUST declare these as global to modify them!
    global LOG_ID_COUNTER
    global MISSION_LOGS

    # 1. Use and increment the global counter
    LOG_ID_COUNTER += 1
    new_log_id = str(LOG_ID_COUNTER).zfill(4) # e.g., "0001"

    # 2. Get current stardate
    stardate = datetime.now().isoformat()

    # 3. Create the log entry
    new_log_entry = {
        'content': content,
        'stardate': stardate,
        'id': new_log_id
    }

    # 4. Store the log entry
    MISSION_LOGS[new_log_id] = new_log_entry

    # 5. Return confirmation
    return f"Mission log '{new_log_id}' successfully created at {stardate}."

@tool
def list_mission_logs() -> str:
    """List all existing mission logs.

    Use this when a crew member needs to review all the logs

    Args:
        None

    Returns:
        A formatted list of all mission logs with their IDs and timestamps.
    """
    if not MISSION_LOGS:
        return "No mission logs found."
    
    log_entries= []
    for log_id, log in MISSION_LOGS.items():
        log_entries.append(f"ID: {log_id}, TimeStamp: {log['stardate']}, Content: {log['content']}")
    return "\n".join(log_entries)

@tool
def read_mission_log(log_id: str) -> str:
    """Retrieve a specific mission log by id
    
    Use this when a crew member needs to:
    - Review a specific log entry.
    
    Args:
        log_id: The ID of the mission log to retrieve
        
    Returns:
        The mission log entry or an error message if not found.
    """
    log = MISSION_LOGS.get(log_id)
    if not log:
        return f"Mission log with ID {log_id} not found."
    
    return f"ID: {log_id} Timestamp: {log['stardate']} Content: {log['content']}"