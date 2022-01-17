import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time

receivers = []
with open('emails.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        # bcc_r.append( line )
        receivers.append( line )

# 1 recipient
# receiver = 'zzz@gmail.com'
# 2+ recipients
# receiver = ['zzz@gmail.com', 'xxx@gmail.com']

# 通過Header物件編碼的文字
subject = 'STP18 計畫說明會邀請函'
subject = Header(subject, 'utf-8').encode()

#構造郵件物件MIMEMultipart物件
#下面的主題，發件人，收件人，日期是顯示在郵件頁面上的。
msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = 'STP 招募團隊'
# msg['To'] = 'zzz@gmail.com'  # 收件人為1個收件人
# msg['To'] = ";".join(receiver)  # 收件人為多個收件人
# msg['Bcc'] = ";".join(bcc_r)  # 密件副本
msg['Date'] = '2022-01-17'

# 構造文字內容
text = open('abby session.html', mode='r', encoding='utf-8')
text = text.read()
text_html = MIMEText(text, 'html', 'utf-8')
msg.attach(text_html)

# 傳送郵件
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(config.email, config.pwd)
    
    for rcpt in receivers:
        try:
            # smtp.sendmail(config.email, receiver+bcc_r, msg.as_string())
            smtp.sendmail(config.email, rcpt, msg.as_string())
            print(f'Mail sent to {rcpt}')
            time.sleep(1)
        except Exception as e:
            print(rcpt, e)
