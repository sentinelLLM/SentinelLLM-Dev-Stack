import json

# Policy map of allowed tools per agent
POLICY = {
    "agent_alpha": ["search", "calculator"],
    "agent_beta": ["calendar", "email"]
}

def validate_tool_call(agent_id: str, tool_name: str) -> dict:
    allowed = POLICY.get(agent_id, [])
    if tool_name not in allowed:
        return {
            "status": "blocked",
            "message": f"{tool_name} is not permitted for {agent_id}"
        }
    return {
        "status": "approved",
        "message": "Tool access granted"
    }

