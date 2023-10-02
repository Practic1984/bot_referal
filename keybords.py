from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
def menu_risk(from_ref):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Я знаю о рисках и готов продолжать", callback_data=f"risk_confirm::{from_ref}"),
        InlineKeyboardButton("Я хочу узнать больше", url="https://t.me/arbitrage_investments")
    )

    return markup


def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Профиль", callback_data=f"profile"),
        InlineKeyboardButton("Пополнить баланс", callback_data=f"to_balance"),
        InlineKeyboardButton("Вывод средств", callback_data=f"out_balance"),
        
    )

    return markup


def admin_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Дерево ссылок", callback_data=f"tree_url"),
        InlineKeyboardButton("Отчет по партнерам", callback_data=f"result_partners"),
        InlineKeyboardButton("Сумма балансов", callback_data=f"summ_balance"),
        InlineKeyboardButton("Начислить процент", callback_data=f"procent"),
    )

    return markup

def to_balance():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("100 $", callback_data=f"to_balance::100"),
        InlineKeyboardButton("200 $", callback_data=f"to_balance::200"),
        InlineKeyboardButton("300 $", callback_data=f"to_balance::300"),
        InlineKeyboardButton("500 $", callback_data=f"to_balance::500"),
        InlineKeyboardButton("1000 $", callback_data=f"to_balance::1000"),
        InlineKeyboardButton("5000 $", callback_data=f"to_balance::5000"),        
        InlineKeyboardButton("10000 $", callback_data=f"to_balance::10000"),          
    )

    return markup



def out_balance():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("100 $", callback_data=f"out_balance::100"),
        InlineKeyboardButton("200 $", callback_data=f"out_balance::200"),
        InlineKeyboardButton("300 $", callback_data=f"out_balance::300"),
        InlineKeyboardButton("500 $", callback_data=f"out_balance::500"),
        InlineKeyboardButton("1000 $", callback_data=f"out_balance::1000"),
        InlineKeyboardButton("5000 $", callback_data=f"out_balance::5000"),        
        InlineKeyboardButton("Вывести всё", callback_data=f"out_balance::all"),          
    )

    return markup

def to_balance_confirm_admin(summa, from_user_id, msg_id):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("Подтвердить", callback_data=f"add_balance::{summa}::{from_user_id}::{msg_id}"),       
    )

    return markup

def out_balance_confirm_admin(summa, from_user_id, msg_id):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("Подтвердить", callback_data=f"pay_balance::{summa}::{from_user_id}::{msg_id}"),       
    )

    return markup