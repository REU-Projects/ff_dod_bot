from mysite import db_processors
from mysite.messenger import messanging
import vk_api


def handle_lottery_command(user_info, token):
    user_id = user_info['id']
    group_id = '95543089'
    if not vk_api.is_user_group_member(group_id, user_id):
        message = messanging.get_goto_group_message(group_id)
        vk_api.send_message(user_id, token, message)
        return
    db_processors.add_into_db(user_info)
    user_db_id = db_processors.get_db_id(user_id)
    message = messanging.get_lottery_message(user_db_id)
    vk_api.send_message(user_id, token, message)


def handle_help_command(user_info,token):
    message = messanging.get_help_message()
    user_id = user_info['id']
    vk_api.send_message(user_id, token, message)


def handle_default_command(user_info,token):
    user_id = user_info['id']
    group_id = '95543089'
    if not vk_api.is_user_group_member(group_id, user_id):
        message = messanging.get_goto_group_message(group_id)
        vk_api.send_message(user_id, token, message)
        return
    message = messanging.get_default_message()
    vk_api.send_message(user_id, token, message)