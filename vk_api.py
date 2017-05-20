import vk

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message)


def is_user_group_member(group_id, user_id):
    check = api.groups.isMember(group_id=group_id, user_id=user_id)
    if check == 1:
        return True
    return False


def get_user_info(letter_id):
    user_info = api.users.get(user_ids=letter_id)
    return user_info[0]
