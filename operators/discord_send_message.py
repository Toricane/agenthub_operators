import requests

from .base_operator import BaseOperator
from ai_context import AiContext


class DiscordMessageSender(BaseOperator):
    @staticmethod
    def declare_name():
        return "discord_send_message"

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.ACT.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "channel_id",
                "data_type": "string",
                "placeholder": "Enter the channel ID",
            },
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "message_content",
                "data_type": "string",
                "placeholder": "Enter the message content",
            },
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "message_status",
                "data_type": "string",
            },
        ]

    def run_step(self, step, ai_context: AiContext):
        params: dict[str, str] = step["parameters"]
        channel_id: str = params.get("channel_id")

        message_content: str = ai_context.get_input("message_content", self)
        token: str = ai_context.get_secret("discord_bot_token")

        message_status = self.send_message(
            channel_id, message_content, token, ai_context
        )
        ai_context.set_output("message_status", message_status, self)

    def send_message(
        self, channel_id: str, message_content: str, token: str, ai_context: AiContext
    ):
        try:
            url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
            headers = {
                "Authorization": f"Bot {token}",
                "Content-Type": "application/json",
            }
            data = {"content": message_content}

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                return "Message sent successfully"
            else:
                ai_context.add_to_log(f"An error occurred: {response.text}")
                return "Message sending failed"
        except Exception as error:
            ai_context.add_to_log(f"An error occurred: {str(error)}")
            return "Message sending failed"
