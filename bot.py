import telebot
import sql_fnc
import sql_query
from config import TOKEN, REF_URL, ADMIN_ID, PAY_LIST, ADMIN_WALLET, LOG_GROUP

import logging
from datetime import datetime
import pytz
import msg
import keybords
import pandas as pd

import openpyxl

def get_msk_time() -> datetime:
    delta =1
    reg_time = datetime.now(pytz.timezone("Europe/Moscow"))
    str_query_time = reg_time.strftime('%Y-%m-%d %H:%M:%S')
    return str_query_time


def save_user(message, from_ref):

    con = sql_fnc.create_connection('users.db')
    sql_fnc.execute_query(con, sql_query.create_users_table, params=[])
    reg_time = get_msk_time()
    sql_fnc.execute_query(con, sql_query.save_user, params=[message.from_user.id, message.from_user.username, reg_time, '0', from_ref, 0,0,0,0])
    con.close()



def save_wallet(message, wallet):

    con = sql_fnc.create_connection('users.db')
    sql_fnc.execute_query(con, sql_query.create_users_table, params=[])
    reg_time = get_msk_time()
    sql_fnc.execute_query(con, sql_query.upd_par_user.format(upd_par = 'wallet'), params=[wallet, message.from_user.id])
    con.close()


def update_param(message, name_param, param):

    con = sql_fnc.create_connection('users.db')
    sql_fnc.execute_query(con, sql_query.create_users_table, params=[])
    sql_fnc.execute_query(con, sql_query.upd_par_user.format(upd_par = name_param), params=[param, message.from_user.id])
    con.close()


def save_ref(message, from_ref):

    con = sql_fnc.create_connection('ref.db')
    sql_fnc.execute_query(con, sql_query.create_ref_table, params=[])
    reg_time = get_msk_time()
    sql_fnc.execute_query(con, sql_query.save_ref, params=[from_ref, message.from_user.username, reg_time])
    con.close()

def up_procent(proc):

    con = sql_fnc.create_connection('users.db')
    sql_fnc.execute_query(con, sql_query.create_users_table, params=[])
    sql_fnc.execute_query(con, sql_query.up_proc.format(proc=proc), params=[])
    con.close()

bot = telebot.TeleBot(token=TOKEN, parse_mode='HTML', skip_pending=True, disable_web_page_preview=True)    
bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("ref", "Получить ссылку"),
    ],)


def main():
    @bot.message_handler(commands=['start'])
    def start_fnc(message):
        print(message.text)
        try:
            from_ref = message.text.split(" ")[1]
            print(from_ref)
            bot.send_message(chat_id=message.from_user.id, text=msg.start_msg, reply_markup=keybords.menu_risk(from_ref=from_ref))
        except Exception as ex:
            print(ex)
            bot.send_message(chat_id=message.from_user.id, text=msg.start_msg_false)

    @bot.message_handler(commands=['ref'])
    def start_fnc(message):
        print(message.text)
        ref = REF_URL + message.from_user.username    
        bot.send_message(chat_id=message.from_user.id, text=ref)

    @bot.message_handler(commands=['admin'])
    def start_fnc(message):
        if message.from_user.id == ADMIN_ID:
            
            print(message.text)
 
            bot.send_message(chat_id=message.from_user.id, text=f"Приветствую тебя, Хозяин! В тебе скрыта сила админа!", reply_markup=keybords.admin_menu())

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if 'risk_confirm' in call.data:
            print(call.data)
            from_ref = call.data.split("::")[1]
            save_user(message=call, from_ref=from_ref)
            save_ref(message=call, from_ref=from_ref)
            
            bot.send_message(chat_id=call.from_user.id, text=msg.get_wallet_msg)

        elif call.data == 'profile':
            con = sql_fnc.create_connection('users.db')
            res = sql_fnc.execute_query(con, sql_query.find_profile_by_id, params=[call.from_user.id])
            con.close()
            print(res)
            username = call.from_user.username
            profile_text = f"""
🪪 Профиль

Инвестировано: {res[5]} $
Доступно для вывода: {res[6]} $

В ожидании депозита: {res[7]} $
В ожидании вывода средств: {res[8]} $

Кошелек для вывода средств: {res[3]}

Ваша реферальная ссылка: <code> https://t.me/WorldArditrage_bot?start={username} </code>
☝️ Нажмите, чтобы скопировать
"""
            bot.send_message(chat_id=call.from_user.id, text=profile_text, reply_markup=keybords.main_menu())


        
        elif call.data == "to_balance":
            bot.send_message(chat_id=call.from_user.id, text=msg.to_balance_msg, reply_markup=keybords.to_balance())

        elif call.data == "out_balance":
            bot.send_message(chat_id=call.from_user.id, text=msg.to_balance_msg, reply_markup=keybords.out_balance())

        elif 'add_balance' in call.data:
            if call.from_user.id == ADMIN_ID:
                print(call.data)
                print('****************************************************')
                # здесь будем по колбеку возвращать и вносить изменения в базе.
                res = call.data.split("::")
                summa = res[1]
                user_id = res[2]
                con = sql_fnc.create_connection('users.db')
                sql_fnc.execute_query(con, sql_query.create_users_table, params=[])
                sql_fnc.execute_query(con, sql_query.to_balance_true, params=[summa, summa, user_id])
                con.close()
                bot.edit_message_reply_markup(chat_id=LOG_GROUP, message_id=call.message.id, reply_markup='')    
                bot.send_message(chat_id=res[2], text=f"Транзакция пополнения баланса на сумму {summa} успешно отправлена", reply_markup=keybords.main_menu())
        
        elif 'pay_balance' in call.data:
            if call.from_user.id == ADMIN_ID:
                print(call.data)
                print('****************************************************')
                # здесь будем по колбеку возвращать и вносить изменения в базе.
                res = call.data.split("::")
                summa = res[1]
                user_id = res[2]
                con = sql_fnc.create_connection('users.db')
                sql_fnc.execute_query(con, sql_query.out_balance_true, params=[summa, user_id])
                con.close()
                bot.edit_message_reply_markup(chat_id=LOG_GROUP, message_id=call.message.id, reply_markup='')    
                bot.send_message(chat_id=res[2], text=f"Транзакция вывода с баланса на сумму {summa} успешно отправлена", reply_markup=keybords.main_menu())
        
        elif 'out_balance' in call.data:
            if call.data.split("::")[1] in PAY_LIST:
                print(call.data)
                update_param(call, name_param='out_balance_wait', param=int(call.data.split("::")[1]))
                con = sql_fnc.create_connection('users.db')
                res = sql_fnc.execute_query(con, sql_query.find_profile_by_id, params=[call.from_user.id])
                con.close()
                print(res)
                text = f"""
Пользователь @{res[1]}
Вывод средств 
Кошелек <code>{res[3]}</code>
Сумма {res[8]} $
"""
                if int(res[6])>=int(res[8]):
                    bot.send_message(chat_id=LOG_GROUP, text=text, reply_markup=keybords.out_balance_confirm_admin(summa=res[8], from_user_id=call.from_user.id, msg_id=call.message.id))
                else:
                    bot.send_message(chat_id=call.from_user.id, text=f"Запрошенная сумма отсутствует на балансе", reply_markup=keybords.main_menu())
        elif 'to_balance' in call.data:
            if call.data.split("::")[1] in PAY_LIST:
                print(call.data)

                update_param(call, name_param='to_balance_wait', param=int(call.data.split("::")[1]))
                con = sql_fnc.create_connection('users.db')
                res = sql_fnc.execute_query(con, sql_query.find_profile_by_id, params=[call.from_user.id])
                con.close()
                print(res)
                bot.send_message(chat_id=call.from_user.id, text=msg.take_hash_msg.format(ADMIN_WALLET=ADMIN_WALLET, SUMMA=int(call.data.split("::")[1]) ))
        
        elif call.data == 'result_partners':
            con = sql_fnc.create_connection('users.db')
            df_all= pd.read_sql_query(sql=sql_query.find_all_profile, con=con, params=[])
            df_all = df_all.drop(columns=['to_balance_wait', 'out_balance_wait'])
            df_all.to_excel(f'{call.from_user.id}.xlsx', index= False)
            with open (file=f'{call.from_user.id}.xlsx', mode='rb') as f:
                bot.send_document(chat_id=call.from_user.id, document=f, caption='Хозяин! Отчет по партнерам в прикрепленном файле...')
            con.close() 

        elif call.data == 'tree_url':
            con = sql_fnc.create_connection('ref.db')
            df_all= pd.read_sql_query(sql=sql_query.find_tree_url, con=con, params=[])
            # df_all = df_all.drop(columns=['to_balance_wait', 'out_balance_wait'])
            df_all.to_excel(f'{call.from_user.id}.xlsx', index= False)
            with open (file=f'{call.from_user.id}.xlsx', mode='rb') as f:
                bot.send_document(chat_id=call.from_user.id, document=f, caption='Хозяин! Отчет дереву ссылок в прикрепленном файле...')
            con.close() 
        
        elif call.data == 'summ_balance':
            con = sql_fnc.create_connection('users.db')
            res = sql_fnc.execute_query_select(con, sql_query.find_null_balance, params=[])[0][0]
            print(res)
            summ_null = 0
            if res != None:
                summ_null = res
            print(summ_null)
            all_users = 0
            all_users = sql_fnc.execute_query_select(con, sql_query.find_all_partners, params=[])[0][0]
            all_summ = sql_fnc.execute_query_select(con, sql_query.find_all_summ, params=[])[0][0]
            print(all_users)
            print(all_summ)
            con.close()
            
            text = f"""
Всего пользователей {all_users}
Нулевых балансов {summ_null}
Общая сумма балансов {all_summ} $
"""
            bot.send_message(chat_id=ADMIN_ID, text=text, reply_markup=keybords.admin_menu())

# TVQG8ZjrVftXCAryEmYjGyJR8p8bXNmo8N
        elif call.data == 'procent':
            m = bot.send_message(chat_id=ADMIN_ID, text=msg.procent_text)
            bot.register_next_step_handler(m, input_procent)

    @bot.message_handler(content_types=['text'])
    def get_text(message):
        if len(message.text.strip()) == 34:
            print(message.text)
            save_wallet(message=message, wallet=message.text)
            bot.send_message(chat_id=message.from_user.id, text=msg.main_menu_msg, reply_markup=keybords.main_menu())

        elif 'tronscan.org/#/transaction' in message.text:
            print('Принимаем хэш')
            # здесь еще отправить сообщение админу надо
            bot.send_message(chat_id=message.from_user.id, text=msg.take_hash_true, reply_markup=keybords.main_menu())
            con = sql_fnc.create_connection('users.db')
            res = sql_fnc.execute_query(con, sql_query.find_profile_by_id, params=[message.from_user.id])
            con.close()
            print(res)
            text = f"""
Пользователь @{message.from_user.username}
Пополнение 
Хэш {message.text}
Сумма {res[7]} $
"""
            m = bot.send_message(chat_id=LOG_GROUP, text=text, reply_markup=keybords.to_balance_confirm_admin(summa=res[7], from_user_id=message.from_user.id, msg_id=message.id))
            print(m)

    def input_procent(message):
        if message.from_user.id == ADMIN_ID:
            up_procent(proc=int(message.text))                  
            bot.send_message(chat_id=message.from_user.id, text='Процент начислен все у кого баланс больше 0', reply_markup=keybords.admin_menu())
    bot.infinity_polling(skip_pending=True)
if __name__ == "__main__":
    main()

    