def is_help_command(vk_response):
    keys = ['помощь','помоги', 'help']
    for key in keys:
        if key in vk_response:
            return True
    return False


def is_lottery_command(vk_response):
    keys = ['ялюблюфф','додфф','финансовыйфакультет','я люблю фф','дод фф','финансовый факультет']
    for key in keys:
        if key in vk_response:
            return True
    return False


def is_default_command(vk_response):
    if is_help_command(vk_response):
        return False
    elif is_lottery_command(vk_response):
        return False
    return True