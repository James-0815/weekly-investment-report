import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

msg = MIMEMultipart()
msg['Subject'] = "📈 Daily Investment Report"
msg['From'] = EMAIL_USER
msg['To'] = EMAIL_TO

# 본문 작성
body = MIMEText("안녕하세요,\n\n자동 생성된 투자 리포트를 첨부드립니다.\n오늘도 성공적인 투자 되세요.\n\n- 제임스 드림", "plain", "utf-8")
msg.attach(body)

# 첨부파일 (report.pdf)
with open("report.pdf", "rb") as f:
    part = MIMEApplication(f.read(), Name="report.pdf")
    part['Content-Disposition'] = 'attachment; filename="report.pdf"'
    msg.attach(part)

# SMTP 전송
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_USER, EMAIL_PASS)
    smtp.send_message(msg)
