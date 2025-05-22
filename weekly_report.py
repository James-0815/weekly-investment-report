from fpdf import FPDF
import datetime

# PDF 클래스 정의
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", size=12)
        self.cell(0, 10, "📊 제임스의 투자 리포트", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# PDF 인스턴스 생성
pdf = PDF()
pdf.add_page()

# Arial Unicode 폰트 설정
pdf.add_font("Arial", "", fname="arial.ttf", uni=True)
pdf.set_font("Arial", size=12)

today = datetime.date.today().strftime("%Y-%m-%d")
pdf.cell(0, 10, f"오늘 날짜: {today}", ln=True)
pdf.cell(0, 10, "성공적인 투자 되세요. - 제임스 드림", ln=True)

# PDF 저장
pdf.output("report.pdf")
