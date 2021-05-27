import email, smtplib, ssl, os
from ideal_items import item_list
from dotenv import load_dotenv
from datetime import date

load_dotenv()


ideal_items = item_list()
on_hand_items = {}
items_to_buy = {}

# gets user count for each item
for item, value in ideal_items.items():
    number_of_item = int(input(f'How many {item}(s) do you have? '))
    on_hand_items[item] = number_of_item

# if the user inputted amount is less than the ideal count, (ideal count - user count) is added to items_to_buy
# else, nothing
for item, current_amount in on_hand_items.items():
    if item in ideal_items:
        if current_amount == ideal_items[item]:
            pass
        elif current_amount < ideal_items[item]:
            items_to_buy[item] = (ideal_items[item] - current_amount)
        else:
            pass
    else:
        continue

for item, value in items_to_buy.items():
    print(f'{item}: {value}\n')