from messenger import message_handlers
from messenger import message_validators
import vk_api


def create_answer(data, token):
    letter_id = data['user_id']
    user_info = vk_api.get_user_info(letter_id)
    vk_response = data['body'].lower()
    message_processors = [
        (
            message_validators.is_help_command,
            message_handlers.handle_help_command
        ),
        (
            message_validators.is_lottery_command,
            message_handlers.handle_lottery_command
        ),
        (
            message_validators.is_default_command,
            message_handlers.handle_default_command
        )
    ]
    for message_validator, message_handler in message_processors:
        if message_validator(vk_response):
            message_handler(user_info, token)