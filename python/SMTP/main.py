import smtplib
import ssl
import random
import os



MY_EMAIL = "muaaztest114@gmail.com"
PASSWORD = "gxhy vjhh vebl tvtw"  # Gmail app password (revoke after testing!)
TO_EMAIL = "muaaztest114@yahoo.com"
QUOTES_FILE = "./quotes.txt"


with open(QUOTES_FILE) as file:
    contents = [line.strip() for line in file if line.strip()]
if not contents:
    raise SystemExit("quotes.txt is empty — nothing to send.")
quote = random.choice(contents)



msg = f"Subject: Random Quote\n\n{quote}"
context = ssl.create_default_context()
connection = smtplib.SMTP("smtp.gmail.com", 587)

try:
    connection.starttls(context=context)
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=msg)
    print("Email sent!")

except Exception as e:
    print(f"Failed to send: {e}")

finally:
    connection.close()