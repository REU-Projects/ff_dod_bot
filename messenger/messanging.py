def get_lottery_message(user_db_id):
    return 'Твой счастливый номер для участия в лотерее - %s \nИ пусть удача всегда будет с вами!' %user_db_id

def get_help_message():
    return 'Помощь - Покажу список команд\n Додфф - дам билетик'

def get_default_message():
    return 'Я пока не очень умный, но я еще научусь!\nА ты случайно не знаешь, о какой лотерее тут все говорят?'

def get_goto_group_message(group_id):
    return 'Чтобы участововать ты должен вступить в группу https://vk.com/club%s' %group_id

