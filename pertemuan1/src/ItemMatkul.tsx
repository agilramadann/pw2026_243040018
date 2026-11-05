interface ItemMatkulProps {
  kode: string;
  nama: string;
  sks: number;
  hari: string;
}

function ItemMatkul({ kode, nama, sks, hari }: ItemMatkulProps) {
  return (
    <li className="course-card">
      <div className="course-info">
        <p className="course-code">{kode}</p>
        <h3>{nama}</h3>
        <p className="course-day">Jadwal sesi: {hari}</p>
      </div>
      <span className="course-credits">{sks} SKS</span>
    </li>
  );
}

export default ItemMatkul;
