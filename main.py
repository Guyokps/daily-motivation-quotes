import os
import random
from twilio.rest import Client

# Get Twilio credentials and WhatsApp number from environment variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
whatsapp_to = os.environ.get('WHATSAPP_TO_NUMBER')

# Twilio's WhatsApp number
whatsapp_from = 'whatsapp:+14155238886'

# List of messages
messages_list = [
    "תתרכזי בשיט שלך, קיפ גוין אוהב אותכם - סמולקין",
    "תזכרי שהאושר שלך זה אחריות אישית שלך, זה לא תלוי בהסכמה או הבנה של אנשים אחרים - סמולקין",
    "את חייבת לעשות מה שמסיב לך אושר - סמולקין",
    "בואו נהיה אמיתיים רגע אתם לא נמצאים בראש הרשימה של אף אחד - סמולקין",
    "אנשים לא תמיד יגידו לכם איך הם מרגישים לגביכם, תהיו בטוחים שהם יראו לכם בצורה מאוד מאוד ברורה, תהיי עירנית! - סמולקין",
    "לא משנה כמה זמן הלכת בדרך הלא נכונה, את תמיד אבל תמיד יכולה להסתובב וללכת לצד השני - סמולקין"
]

# Pick a random message from the list
random_message = random.choice(messages_list)

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send WhatsApp message
try:
    message = client.messages.create(
        body=random_message,
        from_=whatsapp_from,
        to=whatsapp_to
    )
    print(f"Message sent successfully. SID: {message.sid}")

except Exception as e:
    print(f"Error sending message: {e}")
