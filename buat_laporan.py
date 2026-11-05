from pathlib import Path
from PIL import Image, ImageDraw
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION

base = Path(r'C:\Users\Hype AMD\Documents\pw2026_243040018')
project = base / 'pertemuan1'
out = base / 'Laporan_Praktikum_Pertemuan_1_Agil_Ramadhan.docx'
assets = base / 'laporan_assets'
assets.mkdir(exist_ok=True)


def code_image(path: Path, title: str, start: int = 1, end: int | None = None):
    lines = path.read_text(encoding='utf-8').splitlines()
    if end is None:
        end = len(lines)
    selected = lines[start-1:end]
    lexer_name = 'tsx' if path.suffix.lower() == '.tsx' else ('css' if path.suffix == '.css' else ('html' if path.suffix == '.html' else 'javascript'))
    lexer = get_lexer_by_name(lexer_name, stripnl=False)
    formatter = ImageFormatter(font_name='Consolas', font_size=17, line_numbers=True, line_number_bg='#161b22', line_number_fg='#7d8590', background_color='#0d1117', style='monokai', image_pad=18)
    code_png = highlight('\n'.join(selected), lexer, formatter)
    temp = assets / f"{path.stem}_{start}_{end}.raw.png"
    temp.write_bytes(code_png)
    code = Image.open(temp).convert('RGB')
    pad = 28
    canvas = Image.new('RGB', (code.width + pad * 2, code.height + 74 + pad * 2), '#1c2533')
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((pad, pad, canvas.width-pad, canvas.height-pad), radius=14, fill='#0d1117', outline='#30363d', width=2)
    for x, color in [(pad+22, '#ff5f57'), (pad+42, '#febc2e'), (pad+62, '#28c840')]:
        draw.ellipse((x, pad+12, x+12, pad+24), fill=color)
    draw.text((pad+88, pad+10), f'{title}  •  baris {start}-{end}', fill='#e6edf3')
    canvas.paste(code, (pad, pad+46))
    target = assets / f"{path.stem}_{start}_{end}.png"
    canvas.save(target, quality=95)
    return target

# Carbon/SnapeCode-style screenshots for the same files listed in the source report.
files = [
    (project/'src/App.css', 'App.css', 1, 324),
    (project/'src/App.tsx', 'App.tsx', 1, 186),
    (project/'src/BadgeSkill.tsx', 'BadgeSkill.tsx', 1, 18),
    (project/'src/ItemMatkul.tsx', 'ItemMatkul.tsx', 1, 22),
    (project/'src/KartuProfil.tsx', 'KartuProfil.tsx', 1, 68),
    (project/'src/main.tsx', 'main.tsx', 1, 19),
    (project/'src/index.css', 'index.css', 1, 93),
    (project/'index.html', 'index.html', 1, 14),
]
shots = []
for path, title, start, end in files:
    if path.exists():
        count = len(path.read_text(encoding='utf-8').splitlines())
        finish = min(end, count)
        if count > 90 and path.name in ('App.css', 'App.tsx'):
            step = 60
            for chunk_start in range(start, finish + 1, step):
                chunk_end = min(chunk_start + step - 1, finish)
                shots.append(code_image(path, title, chunk_start, chunk_end))
        else:
            shots.append(code_image(path, title, start, finish))

# UI screenshot already captured by Playwright.
ui_shot = base / 'hasil-antarmuka.png'


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), fill)
    tc_pr.append(shd)


doc = Document()
section = doc.sections[0]
section.top_margin = Inches(0.7)
section.bottom_margin = Inches(0.7)
section.left_margin = Inches(0.75)
section.right_margin = Inches(0.75)

styles = doc.styles
styles['Normal'].font.name = 'Arial'
styles['Normal'].font.size = Pt(11)
styles['Heading 1'].font.name = 'Arial'
styles['Heading 1'].font.size = Pt(18)
styles['Heading 1'].font.bold = True
styles['Heading 2'].font.name = 'Arial'
styles['Heading 2'].font.size = Pt(14)

# Header inspired by the source report.
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('PRAKTIKUM WEB-76197-387346')
r.bold = True; r.font.size = Pt(14)
p = doc.add_paragraph('R. Sandhika Galih Amalga, ST., MT.')
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('TUGAS - PERTEMUAN 1')
r.bold = True; r.font.size = Pt(16)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run('IF21W0508 - Praktikum Web').bold = True

doc.add_paragraph()
table = doc.add_table(rows=4, cols=2)
table.style = 'Table Grid'
for row, (label, value) in zip(table.rows, [('NPM', '243040018'), ('Nama', 'Agil Ramadhan'), ('Kelas', 'B'), ('Link Github Repository', 'https://github.com/Mulqwerty/PW2026_243040016')]):
    row.cells[0].text = label
    row.cells[1].text = value
    set_cell_shading(row.cells[0], 'D9EAF7')


def heading(text):
    p = doc.add_paragraph()
    p.style = doc.styles['Heading 1']
    p.add_run(text)

heading('Bagian 1. Screenshot Semua Kode')
doc.add_paragraph('Kode dibuat dalam tampilan seperti SnapeCode/Karbon agar struktur kode mudah dibaca dan konsisten dengan tugas laporan.')
for index, shot in enumerate(shots, 1):
    doc.add_picture(str(shot), width=Inches(6.9))
    cap = doc.paragraphs[-1]
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap = doc.add_paragraph(f'Screenshot kode {index}')
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

heading('Bagian 2. Penjelasan Kode')
doc.add_paragraph('Arsitektur aplikasi. Project ini merupakan Single Page Application (SPA) yang dibangun dengan React dan Vite. Berkas index.html menyediakan metadata bahasa, judul halaman, elemen #root, dan skrip masuk. Berkas main.tsx memeriksa elemen tersebut, membuat React root, lalu merender komponen App di dalam React.StrictMode.')
doc.add_paragraph('App.tsx sebagai komponen induk menyimpan data mata kuliah, keahlian, dan proyek dalam array. Data tersebut ditampilkan dengan metode map(). Setiap hasil render menggunakan key yang stabil, yaitu id mata kuliah, nama keahlian/proyek, atau nama teknologi. Data profil, jadwal, dan keahlian diteruskan ke komponen anak melalui props.')
doc.add_paragraph('KartuProfil.tsx menerima props bertipe untuk nama, NPM, kelas, status, dan URL foto opsional. ItemMatkul.tsx menampilkan satu data mata kuliah, sedangkan BadgeSkill.tsx menampilkan nama skill beserta levelnya. Interface dan union type membatasi bentuk serta nilai data yang diterima komponen.')
doc.add_paragraph('App.css mengatur layout, kartu, daftar, dan responsivitas layar kecil. index.css berisi gaya global seperti tipografi dan warna dasar. Tombol pada App.tsx menggunakan onClick untuk memanggil window.alert sebagai contoh event handling React.')
doc.add_paragraph('Pemisahan komponen membatasi tanggung jawab tiap bagian dan memudahkan penggunaan ulang. Props mengalir satu arah dari komponen induk ke anak. Rendering array menghindari markup berulang, sementara key unik membantu React mempertahankan identitas elemen saat daftar diperbarui.')

heading('Bagian 3. Screenshot Hasil Antarmuka')
doc.add_paragraph('Hasil antarmuka Modul 1 menampilkan judul halaman, profil Agil Ramadhan, jadwal praktikum, showcase proyek, serta tombol interaktivitas.')
if ui_shot.exists():
    doc.add_picture(str(ui_shot), width=Inches(6.9))
    p = doc.paragraphs[-1]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER

heading('Bagian 4. Penjelasan Hasil Antarmuka')
doc.add_paragraph('Antarmuka menampilkan profil mahasiswa dengan nama Agil Ramadhan, NPM 243040018, kelas B, status aktif, serta badge keahlian. Bagian jadwal menyajikan empat mata kuliah beserta kode, hari, dan jumlah SKS. Showcase menampilkan empat contoh proyek, deskripsi, teknologi, dan tautan pencarian repository GitHub.')
doc.add_paragraph('Tombol Uji Interaktivitas memanggil sapaan melalui window.alert. Hasil pengujian: npm run build berhasil menjalankan pemeriksaan TypeScript dan menghasilkan berkas produksi Vite. Halaman preview menampilkan seluruh bagian antarmuka, termasuk responsivitas CSS pada layar kecil.')

doc.save(out)
print(out)
