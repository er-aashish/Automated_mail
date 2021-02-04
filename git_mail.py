import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

with open("test.csv") as file:  # Add .csv file containing all the mail id's of the recipients
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email in reader:  # make sure your .csv have same headers (name and email)

        host = "smtp.gmail.com"
        port = 587
        username = "xxx@gmail.com"  # Add sender mail id
        password = "*****"  # Add password
        from_email = "xxx@gmail.com"  # Add sender mail_id

        email_conn = smtplib.SMTP(host, port)

        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(username, password)

        the_msg = MIMEMultipart("alternative")
        the_msg['Subject'] = "Register for Winter Run"
        the_msg["From"] = from_email

        # This is the alternative text you can add in case the recipient is not available to receive html version of mail

        plain_txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "

        # This is the HTML version of the code

        html_txt = """

            <html>
                <head>
                    <style>
                        # Add your inline css here
                    </style>

                <body>
                    # Add your HTML body here
                </body>
            </html>
                      """
        part_1 = MIMEText(plain_txt, "plain")
        part_2 = MIMEText(html_txt, "html")

        the_msg.attach(part_1)
        the_msg.attach(part_2)

        email_conn.sendmail(from_email, email, the_msg.as_string().format(name_1=name))
        email_conn.quit()

print("Mail sent successfully")




