from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = "xoxb-your-token"
client = WebClient(token=slack_token)

def send_alert(message: str, channel: str = "#llm-alerts"):
    try:
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Slack error: {e.response['error']}")

