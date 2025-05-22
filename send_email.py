import smtplib
from email.message import EmailMessage
import os

EMAIL_USER = os.environ['EMAIL_USER']
EMAIL_PASS = os.environ['EMAIL_PASS']
EMAIL_TO = os.environ['EMAIL_TO']

msg = EmailMessage()
msg['Subject'] = '📈 Daily Investment Report'
msg['From'] = EMAIL_USER
msg['To'] = EMAIL_TO

msg.set_content(
    "안녕하세요,\n\n자동 생성된 투자 리포트를 첨부드립니다.\n오늘도 성공적인 투자 되세요.\n\n- 제임스 드림"
)

# 리포트 파일 첨부 (weekly_report.py에서 생성되는 PDF 경로/이름 사용)
filename = "report.pdf"
with open(filename, "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=filename)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_USER, EMAIL_PASS)
    smtp.send_message(msg)
    print("✅ 이메일 전송 완료")
