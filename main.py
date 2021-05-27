import email, smtplib, ssl, os
from ideal_items import item_list
from dotenv import load_dotenv

load_dotenv()


def send_sms_via_email(
    number:str,
    message:str,
    provider:str,
    sender_credentials:tuple,
    subject:str = 'sent using python',
    smtp_server:str = 'smtp.gmail.com',
    smtp_port:int = 465
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@tmomail.net'

    email_message = f'Subject:{subject}\nTo:{receiver_email}\n{message}'

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

def email_setup(text_message):
    number = '6037814883'
    message = text_message
    provider = 'T-Mobile'
    sender_credentials = (os.getenv('EMAIL'), os.getenv('PASSWORD'))

    send_sms_via_email(number, message, provider, sender_credentials)



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

text_message = ''
for item, value in items_to_buy.items():
    text_message += f'{item}: {value}\n'

email_setup(str(text_message))