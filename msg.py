from config import ADMIN_WALLET
start_msg = """
⚠️ Предупреждение о рисках

Уважаемые инвесторы, инвестиции всегда связаны с рисками.

WorldArditrage предлагает своим инвесторам максимальную диверсификацию или минимизацию рисков, но риск не может быть сведен к нулю. Это должны понимать все, кто когда-либо участвовал в инвестиционных проектах, На сегодняшний день мы минимизируем риски между пятью арбитражными командами, которые, в свою очередь, минимизируют риски уже в своей команде. Такой подход позволяет снизить риски. Однако каждый инвестор WorldArditrage осознает и принимает риски и не инвестирует заемные или кредитные средства для получения прибыли, а также при инвестировании выбирает подходящую ему стратегию управления рисками.

Прочитав это предупреждение, вы принимаете и понимаете: все вышесказанное.

Если по какой-то причине вы не понимаете суть вышесказанного, то вам следует проконсультироваться с приглашающим лицом или воздержаться от инвестирования. 

На АМА -сессиях мы анализируем все возможные риски, связанные с инвестированием в арбитражные инвестиции. Если по какой-то причине вы не посещали наши конференции, вы можете посмотреть записи в нашей группе @arbitrag_investments, в этой группе содержится вся вводная информация.

Спрашивайте и задавайте вопросы до тех пор, пока не убедитесь, что поступаете правильно. 
"""
start_msg_false = """
Вы можете подключиться к боту только по реферальной ссылке, пожалуйста обратитесь к одному из партнеров для получения валидной ссылки.
"""
get_wallet_msg = """
Введите адрес кошелька
"""

main_menu_msg = """
Вы находитесь в главном меню
"""
to_balance_msg = """
Выберите сумму пополнения
"""

out_balance_msg = """
Выберите сумму для вывода
"""

take_hash_msg = """
Произвежите оплату на кошелек 
<code>{ADMIN_WALLET}</code>
в сумме <code>{SUMMA}</code>  и в качестве подтверждения пришлите хэш транзакции в виде ссылки, например ⤵️

https://tronscan.org/#/transaction/7d8e67e4c52c0ad89d2ef9f6d29105394bee89c87090ee4f6675962d96e40c97?lang=en
"""
take_hash_true = """
Операция занимает до 48 часов, если транзакция не прошла в указанный срок, то свяжитесь с админом @goldman495
"""
procent_text = """
Введите процент числом ... ⤵️
"""