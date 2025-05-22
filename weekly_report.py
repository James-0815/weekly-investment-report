from fpdf import FPDF
import datetime

class SafeFPDF(FPDF):
    def safe_cell(self, w, h=10, txt="", ln=False):
        safe_txt = txt.encode("latin-1", errors="ignore").decode("latin-1")
        self.cell(w, h, txt=safe_txt, ln=ln)

pdf = SafeFPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

today = datetime.date.today().strftime("%Y-%m-%d")

pdf.safe_cell(200, 10, txt=f"[제임스 투자리포트] {today}", ln=True)
pdf.safe_cell(200, 10, txt="✅ 오늘의 투자 요약 리포트입니다.", ln=True)
pdf.safe_cell(200, 10, txt="- 비트코인 가격 상승 지속", ln=True)
pdf.safe_cell(200, 10, txt="- 미국 국채 수익률 하락", ln=True)
pdf.safe_cell(200, 10, txt="- 나스닥 기술주 반등", ln=True)

pdf.output("report.pdf")
