from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # ✏️ GANTI: Nama lu
    name = "Muhammad Daffa Alfarizqi"

    # ✏️ GANTI: Stats singkat tentang lu
    stats = [
        {"value": "2th", "label": "Semester"},
        {"value": "10+", "label": "Proyek"},
        {"value": "3+", "label": "Tahun Coding"},
        {"value": "S1", "label": "Informatika"},
    ]

    # ✏️ GANTI: Skill lu — bisa tambah/hapus kategori dan item
    skills = {
        "Languages": ["Python", "JavaScript", "HTML", "CSS"],
        "Frameworks": ["Flask", "Bootstrap", "React"],
        "Tools": ["Git", "VS Code", "Figma", "Postman"],
    }

    # ✏️ GANTI: Proyek lu — isi title, desc, tag, dan link (boleh kosong "")
    projects = [
       {
        "tag": "Web · Flask",
        "title": "Sistem Portofolio",
        "desc": "Website portofolio pribadi berbasis Flask dan Jinja2 template engine, di-deploy menggunakan Vercel.",
        "link": "",
    },
    {
        "tag": "Python · CLI",
        "title": "Aplikasi To-Do List",
        "desc": "Aplikasi manajemen tugas berbasis terminal dengan fitur tambah, hapus, dan tandai tugas selesai.",
        "link": "",
    },
    {
        "tag": "Web · HTML/CSS",
        "title": "Landing Page Produk",
        "desc": "Desain halaman promosi produk responsif menggunakan HTML, CSS, dan Bootstrap.",
        "link": "",
    },
    ]

    return render_template(
        'index.html',
        title=f"{name} — Portfolio",
        name=name,
        stats=stats,
        skills=skills,
        projects=projects,
    )


if __name__ == '__main__':
    app.run(debug=True)