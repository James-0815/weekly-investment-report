from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="자동 생성된 투자 리포트", ln=True)
pdf.output("report.pdf")  # ✅ 이 줄이 반드시 있어야 함
