import BadgeSkill, { type LevelKeahlian } from './BadgeSkill';
import KartuProfil from './KartuProfil';
import ItemMatkul from './ItemMatkul';
import './App.css';

interface Praktikum {
  id: number;
  kode: string;
  nama: string;
  sks: number;
  hari: string;
}

const daftarPraktikum: Praktikum[] = [
  {
    id: 101,
    kode: 'IF211',
    nama: 'Pemrograman Web (React & Laravel)',
    sks: 3,
    hari: 'Senin',
  },
  {
    id: 102,
    kode: 'IF212',
    nama: 'Sistem Basis Data (PostgreSQL)',
    sks: 3,
    hari: 'Rabu',
  },
  {
    id: 103,
    kode: 'IF213',
    nama: 'Rekayasa Perangkat Lunak Terapan',
    sks: 3,
    hari: 'Kamis',
  },
  {
    id: 104,
    kode: 'IF214',
    nama: 'Arsitektur Sistem Terdistribusi',
    sks: 2,
    hari: 'Jumat',
  },
];

const daftarKeahlian: { namaSkill: string; level: LevelKeahlian }[] = [
  { namaSkill: 'HTML & CSS', level: 'Menengah' },
  { namaSkill: 'JavaScript', level: 'Pemula' },
  { namaSkill: 'React', level: 'Pemula' },
  { namaSkill: 'Git & GitHub', level: 'Pemula' },
];

const daftarProyek = [
  {
    nama: 'Website Portofolio Mahasiswa',
    deskripsi:
      'Halaman profil responsif untuk memperkenalkan diri, menampilkan keahlian, dan mengumpulkan karya.',
    teknologi: ['React', 'TypeScript', 'CSS'],
  },
  {
    nama: 'Aplikasi Daftar Tugas',
    deskripsi:
      'Aplikasi sederhana untuk mencatat tugas, mengubah status pengerjaan, dan mengatur prioritas.',
    teknologi: ['JavaScript', 'HTML', 'CSS'],
  },
  {
    nama: 'Katalog Produk',
    deskripsi:
      'Katalog produk dengan tampilan kartu, informasi harga, dan navigasi kategori.',
    teknologi: ['React', 'CSS'],
  },
  {
    nama: 'Sistem Informasi Akademik',
    deskripsi:
      'Konsep antarmuka untuk melihat informasi mahasiswa, mata kuliah, dan jadwal perkuliahan.',
    teknologi: ['React', 'TypeScript', 'PostgreSQL'],
  },
];

function App() {
  const tampilkanSapaan = () => {
    window.alert(
      'Selamat datang di Modul 1! Anda berhasil menguasai fondasi arsitektur React JS.',
    );
  };

  return (
    <main className="app">
      <header className="page-header">
        <p className="eyebrow">Laboratorium Informatika</p>
        <h1>Praktikum Pemrograman Web</h1>
        <p className="page-description">Modul 1: Pengenalan React JS &amp; Vite</p>
      </header>

      <section className="content-section" aria-labelledby="profile-heading">
        <div className="section-heading">
          <p className="section-label">Perkenalan</p>
          <h2 id="profile-heading">Profil Mahasiswa Praktikan</h2>
        </div>
        <div className="profile-card">
          <KartuProfil
            nama="Azriel Mulqie Hakim"
            npm="243040016"
            kelas="E"
            status="Aktif"
            fotoUrl="https://via.placeholder.com/80"
          />
          <div className="skills">
            <h3 className="skills-heading">Keahlian</h3>
            <ul className="skill-list">
              {daftarKeahlian.map((keahlian) => (
                <BadgeSkill
                  key={keahlian.namaSkill}
                  namaSkill={keahlian.namaSkill}
                  level={keahlian.level}
                />
              ))}
            </ul>
          </div>
        </div>
      </section>

      <section className="content-section" aria-labelledby="schedule-heading">
        <div className="section-heading">
          <p className="section-label">Semester ini</p>
          <h2 id="schedule-heading">Rencana Praktikum</h2>
          <p className="section-description">
            Daftar mata kuliah dan jadwal sesi praktikum.
          </p>
        </div>

        <ul className="course-list">
          {daftarPraktikum.map((matkul) => (
            <ItemMatkul key={matkul.id} {...matkul} />
          ))}
        </ul>
      </section>

      <section className="content-section" aria-labelledby="portfolio-heading">
        <div className="section-heading">
          <p className="section-label">Karya pilihan</p>
          <h2 id="portfolio-heading">Showcase Portofolio</h2>
          <p className="section-description">
            Contoh proyek yang dapat disesuaikan dengan karya yang sudah dibuat.
          </p>
        </div>

        <ul className="project-list">
          {daftarProyek.map((proyek) => (
            <li className="project-card" key={proyek.nama}>
              <div className="project-content">
                <h3>{proyek.nama}</h3>
                <p className="project-description">{proyek.deskripsi}</p>
                <ul className="technology-list" aria-label="Teknologi yang digunakan">
                  {proyek.teknologi.map((teknologi) => (
                    <li className="technology-tag" key={teknologi}>
                      {teknologi}
                    </li>
                  ))}
                </ul>
              </div>
              <a
                className="repository-link"
                href={`https://github.com/search?q=${encodeURIComponent(proyek.nama)}&type=repositories`}
                target="_blank"
                rel="noopener noreferrer"
                aria-label={`Cari repositori GitHub untuk ${proyek.nama}`}
              >
                Cari repo di GitHub
              </a>
            </li>
          ))}
        </ul>
      </section>

      <footer className="page-footer">
        <p>Sudah siap memulai praktikum?</p>
        <button className="welcome-button" type="button" onClick={tampilkanSapaan}>
          Uji Interaktivitas
        </button>
      </footer>
    </main>
  )
}

export default App;
