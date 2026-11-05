export type LevelKeahlian = 'Pemula' | 'Menengah' | 'Mahir';

interface BadgeSkillProps {
  namaSkill: string;
  level: LevelKeahlian;
}

function BadgeSkill({ namaSkill, level }: BadgeSkillProps) {
  return (
    <li className={`skill-badge skill-badge--${level.toLowerCase()}`}>
      <span className="skill-name">{namaSkill}</span>
      <span className="skill-level">{level}</span>
    </li>
  );
}

export default BadgeSkill;
