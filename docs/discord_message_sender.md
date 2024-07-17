# Summary
The `DiscordMessageSender` operator sends a message using Discord API with the specified message content and channel ID.

# Inputs
- `message_content`: A string containing the message content to be sent.

# Parameters
- `channel_id`: A string representing the channel's ID where the message will be sent.

# Outputs
- `message_status`: A string indicating the status of the message sending process, either "Message sent successfully" or "Message sending failed".

# Functionality
The `run_step` function is responsible for the main logic of the operator. It reads the channel ID from the parameters, and the message content from the inputs. It also retrieves the Discord bot API token from the AI context. It then calls the `send_message` helper function with the necessary parameters to send the message.

The `send_email` function configures the headers and data of the post request by formatting the parameters and inputs accordingly and sends the message to the channel. It returns the status of the message sending process as a string.
