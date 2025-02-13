!pip install fpdf

from fpdf import FPDF
from google.colab import files

# ---- Konfigurasi Gambar Profil ----
profile_image_path = "/content/profile.jpg"  # Ganti dengan path gambar yang diunggah

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "Curriculum Vitae", ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, "Halaman 1", align='C')

    def add_section_title(self, title):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 6, title, ln=True)
        self.ln(2)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())  # Garis pemisah
        self.ln(3)

# Buat PDF
pdf = PDF(format='A4')
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_page()
pdf.set_font("Arial", size=10)

# ---- Header Profil + Foto ----
if profile_image_path:
    pdf.image(profile_image_path, x=10, y=20, w=40)

pdf.set_xy(55, 20)  # Pindahkan posisi teks ke samping foto
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 6, "Kevin Putra", ln=True)

pdf.set_xy(55, 25)  # Atur posisi untuk biodata
pdf.set_font("Arial", '', 10)
profile_info = [
    "0822495  |  vinin@gmail.com",
    "LinkedIn: linkedin.com/in/vinix-ai",
    "Perumahan Green View Cibinong blok N"
]
for info in profile_info:
    pdf.set_x(55)  # Set x agar sejajar dengan judul
    pdf.cell(0, 5, info, ln=True)

pdf.ln(22)  # Beri jarak sebelum bagian selanjutnya

# ---- Profil Singkat ----
pdf.add_section_title("Profil Singkat")
pdf.set_font("Arial", '', 10)
pdf.multi_cell(0, 5, "Saya Kevin Putr, mahasiswa aktif Sistem Informasi di Universitas Trisakti Jakarta. "
                     "Saya memiliki pengalaman dalam Analisis Data dan Perencanaan Bisnis, serta memiliki minat dalam memahami kebutuhan klien "
                     "agar dapat diterjemahkan dengan baik kepada tim. Saya bersemangat untuk terus belajar dan berkembang.")

pdf.ln(4)

# ---- Pendidikan ----
pdf.add_section_title("Pendidikan")
pdf.set_font("Arial", '', 10)
pdf.cell(0, 5, "- Universitas Trisakti, Sistem Informasi (Jun 2021 - Sekarang), IPK: 3.22/3.25", ln=True)
pdf.cell(0, 5, "- SMA Mardi Waluya Cibinong (2018 - 2021)", ln=True)

pdf.ln(4)

# ---- Pengalaman ----
pdf.add_section_title("Pengalaman Organisasi")
pdf.set_font("Arial", '', 10)
orgs = [
    "- Himpunan Mahasiswa - Universitas Trisakti (2023 - Sekarang): Disipliner",
    "- OSIS SMA Mardi Waluya Cibinong (2018 - 2019): Teknik Ilmu Komputer"
]
for org in orgs:
    pdf.cell(0, 5, org, ln=True)

pdf.ln(4)

# ---- Sertifikasi ----
pdf.add_section_title("Sertifikasi")
pdf.set_font("Arial", '', 10)
certificates = [
    ("Digital Skills of Today and Tomorrow (Feb 2022)", "https://drive.google.com/file/d/1kW7kcPU6I06tNBsQ7hLQgCf591s5DYyr/view?usp=sharing"),
    ("Kuliah Umum K3L (Jun 2022)", "https://drive.google.com/file/d/1o3wpPeg"),
    ("Asisten Laboratorium (Jan 2025)", "https://drive.google.com/file/d/1BptB8kyav4H"),
    ("Webinar Social Education (Okt 2021)", "https://drive.google.com/file/d/1dsZXJifj"),
    ("Seminar Blockchain (Mar 2024)", "https://drive.google.com/file/d/1ogRiKaVONcD"),
    ("Workshop Data Academy (Des 2023)", "https://drive.google.com/file/d/1upvb-iP1FjLV"),
    ("Webinar Career Preparation (Mar 2022)", "https://drive.google.com/file/d/13mwThZz")
]
for cert, link in certificates:
    pdf.set_text_color(0, 0, 255)
    pdf.cell(0, 5, cert, ln=True, link=link)
    pdf.set_text_color(0, 0, 0)

pdf.ln(4)

# ---- Keahlian ----
pdf.add_section_title("Keahlian")
pdf.set_font("Arial", '', 10)
skills = [
    "Soft Skills: Komunikasi Tim, Leadership, Relasi, Toleransi, Fast Learning",
    "Hard Skills: Python, HTML, Photoshop, Premiere, Canva"
]
for skill in skills:
    pdf.multi_cell(0, 5, f"- {skill}")

pdf.ln(4)

# ---- Bahasa ----
pdf.add_section_title("Bahasa")
pdf.set_font("Arial", '', 10)
languages = ["Bahasa Indonesia - Fasih", "Bahasa Inggris - Menengah"]
for lang in languages:
    pdf.cell(0, 5, f"- {lang}", ln=True)

pdf.ln(4)

# ---- Hobi ----
pdf.add_section_title("Hobi & Minat")
pdf.set_font("Arial", '', 10)
hobbies = ["Bermain game", "Memasak", "Olahraga ringan", "Fotografi"]
for hobby in hobbies:
    pdf.cell(0, 5, f"- {hobby}", ln=True)

# Simpan PDF
pdf_filename = "CV_Kevin_Putra_Tjahjono.pdf"
pdf.output(pdf_filename)

# Unduh file
files.download(pdf_filename)
