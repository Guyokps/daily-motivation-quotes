import os
import random
from twilio.rest import Client

# Get Twilio credentials and WhatsApp numbers from environment variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
whatsapp_to_1 = os.environ.get('WHATSAPP_TO_NUMBER_1')
whatsapp_to_2 = os.environ.get('WHATSAPP_TO_NUMBER_2')

# Twilio's WhatsApp number
whatsapp_from = 'whatsapp:+14155238886'

# List of messages
messages_list = [
    "תתרכזי בשיט שלך, קיפ גוין אוהב אותכם - סמולקין",
    "תזכרי שהאושר שלך זה אחריות אישית שלך, זה לא תלוי בהסכמה או הבנה של אנשים אחרים - סמולקין",
    "את חייבת לעשות מה שמסיב לך אושר - סמולקין",
    "בואו נהיה אמיתיים רגע אתם לא נמצאים בראש הרשימה של אף אחד - סמולקין",
    "אנשים לא תמיד יגידו לכם איך הם מרגישים לגביכם, תהיו בטוחים שהם יראו לכם בצורה מאוד מאוד ברורה, תהיי עירנית! - סמולקין",
    "לא משנה כמה זמן הלכת בדרך הלא נכונה, את תמיד אבל תמיד יכולה להסתובב וללכת לצד השני - סמולקין",
    "דמיינו את העצמי העתידי שלכם, כל תכונה, כל פרט, כל הישג, כל הגדולים היו ממוצעים, כל הסמלים היו פעם בלתי נראים - סמולקין",
    "אם אנחנו שונים ככ מהאחר, חברים אנחנו צריכים לחבק את זה באהבה, זה הסקיל שלנו, זה כל היופי בנו - סמולקין ",
    "כשאתה עוקב אחרי ההאהבה שלך, אתה מאבד את עצמך - סמולקין ",
    "תזכרו שכל האנשים שנתתם להם הזדמנות שנייה הפכה להיות ההזדמלות האחרונה - סמולקין",
    "תפזרו את אהבתכם לעולם, את החמלה את הנדיבות שיש בכם, פזרו אותם בחינם, בחינם, לכולם - סמולקין",
    "מה שאתה עושה זה לא נורמלי, כאוס, פסיכי, פרדוקס חולני, הצלחה נובעת מהחיים במצבי קיצון - סמולקין",
    "אם אתה אובססיבי למשהו, כל מה שאתה צריך לעשות זה להמשיך - סמולקין",
    "כשיש ספק, קח את המסלול הקשה, תן לעצמי העתידי שלך להחליט - סמולקין",
]

# Pick a random message from the list
random_message = random.choice(messages_list)

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send WhatsApp messages
try:
    message_1 = client.messages.create(
        body=random_message,
        from_=whatsapp_from,
        to=whatsapp_to_1
    )
    message_2 = client.messages.create(
        body=random_message,
        from_=whatsapp_from,
        to=whatsapp_to_2
    )

    print(f"Messages sent successfully. SID 1: {message_1.sid}, SID 2: {message_2.sid}")

except Exception as e:
    print(f"Error sending messages: {e}")
