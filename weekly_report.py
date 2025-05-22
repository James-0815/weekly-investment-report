from fpdf import FPDF
from datetime import datetime

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

title = "📈 제임스의 주간 투자 리포트"
date = datetime.now().strftime("%Y-%m-%d")
content_lines = [
    f"{title} - {date}",
    "",
    "📊 나스닥, 비트코인, M2, TGA 잔고 주요 지표",
    "- 나스닥: 상승세 유지 중",
    "- BTCUSD: 단기 조정 후 반등 예상",
    "- M2 통화량: 완만한 증가세",
    "- TGA 잔고: 2025년 기준 안정적 흐름",
    "",
    "📝 금일 전략 요약:",
    "- 저평가 종목 분할 매수",
    "- 채권과 암호화폐 균형 유지",
]

for line in content_lines:
    pdf.cell(200, 10, txt=line, ln=True)

pdf.output("report.pdf")
