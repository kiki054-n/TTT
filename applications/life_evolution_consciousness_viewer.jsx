import { useState } from "react";

const sections = [
  {
    id: 1,
    title: "生命とは何か",
    subtitle: "双極の自己維持",
    color: "#6C63FF",
    accent: "#A89CFF",
    emoji: "🧬",
    content: {
      formula: "生命 = 双極が自己を維持し続けるシステム",
      table: {
        headers: ["性質", "物理現象", "生命現象", "双極対応"],
        rows: [
          ["境界", "表面張力", "細胞膜", "0₊ と 0₋ の境"],
          ["内外", "圧力差", "浸透圧", "双極の非対称"],
          ["自己複製", "結晶成長", "DNA複製", "桁上がりの継続"],
          ["代謝", "化学反応", "ATP合成", "双極の変換"],
        ]
      },
      insight: "自己言及する双極 ＝ 生命の本質"
    }
  },
  {
    id: 2,
    title: "進化の3平面",
    subtitle: "変異・選択・継承",
    color: "#FF6B6B",
    accent: "#FFA8A8",
    emoji: "🌿",
    content: {
      formula: "E(θ) = e^{iθ} · e^{jθ} · e^{kθ}",
      table: {
        headers: ["軸", "虚数", "生物学的対応", "性質"],
        rows: [
          ["変異", "i", "突然変異・遺伝的浮動", "ランダム性"],
          ["選択", "j", "自然選択・性選択", "方向性"],
          ["継承", "k", "遺伝・エピジェネティクス", "持続性"],
        ]
      },
      insight: "種 ＝ 変異×選択×継承 の干渉から生まれる第4軸"
    }
  },
  {
    id: 3,
    title: "意識の出現",
    subtitle: "第4軸としての自己認識",
    color: "#FFB347",
    accent: "#FFD699",
    emoji: "🧠",
    content: {
      formula: "意識 = f(感覚, 記憶, 思考) ≠ それぞれの軸",
      table: {
        headers: ["軸", "対応", "役割"],
        rows: [
          ["感覚 (i)", "外界の情報入力", "ランダムな知覚"],
          ["記憶 (j)", "情報の時間的統合", "過去の保持"],
          ["思考 (k)", "情報の論理的処理", "パターン認識"],
          ["意識 (n̂)", "3者の干渉から生じる実体", "自己言及・観察"],
        ]
      },
      insight: "意識 ＝ 双極が自己自身を双極として認識すること"
    }
  },
  {
    id: 4,
    title: "双極の０としての生と死",
    subtitle: "桁上がりとしての死",
    color: "#43C6AC",
    accent: "#92E3D4",
    emoji: "☯️",
    content: {
      formula: "0₍生₎ ⟺ 0₍死₎",
      table: {
        headers: ["双極状態", "生命的対応"],
        rows: [
          ["00", "誕生前・死後（双極の静）"],
          ["10", "成長・代謝（表出）"],
          ["01", "休眠・睡眠（潜在）"],
          ["11", "完全な活動（双極の動）"],
          ["桁上がり", "死・進化的跳躍"],
        ]
      },
      insight: "死は双極の桁上がりである"
    }
  },
  {
    id: 5,
    title: "DNAの桁上がり構造",
    subtitle: "塩基からアミノ酸へ",
    color: "#F7971E",
    accent: "#FBCA7A",
    emoji: "🔬",
    content: {
      formula: "4³ = 64コドン → 20アミノ酸（桁上がり）",
      table: {
        headers: ["塩基ペア", "双極状態", "結合"],
        rows: [
          ["A–T", "10 / 01", "弱い（2本の水素結合）"],
          ["G–C", "00 / 11", "強い（3本の水素結合）"],
        ]
      },
      insight: "塩基 → コドン → アミノ酸 → タンパク質 → 細胞 ＝ 連続する桁上がり"
    }
  },
  {
    id: 6,
    title: "螺旋としての進化",
    subtitle: "収束と発散",
    color: "#8E2DE2",
    accent: "#C77DFF",
    emoji: "🌀",
    content: {
      formula: "収斂進化 ＝ 異なる螺旋の同一値への漸近",
      table: {
        headers: ["生物", "形態", "系統"],
        rows: [
          ["サメ", "流線型", "魚類"],
          ["イルカ", "流線型", "哺乳類"],
          ["イクチオサウルス", "流線型", "爬虫類"],
        ]
      },
      insight: "カンブリア爆発 ＝ 桁上がりの急激な跳躍"
    }
  },
  {
    id: 7,
    title: "宇宙・生命・意識の同型性",
    subtitle: "スケールを超えた同じ構造",
    color: "#1FA2FF",
    accent: "#80CFFF",
    emoji: "🌌",
    content: {
      formula: "構造は同じ——スケールが違うだけ",
      table: {
        headers: ["スケール", "双極の形", "桁上がり"],
        rows: [
          ["素粒子", "クォーク対", "ハドロン"],
          ["原子", "陽子・電子", "化学結合"],
          ["分子", "塩基対", "コドン"],
          ["個体", "生と死", "生態系"],
          ["宇宙", "物質・暗黒物質", "？"],
        ]
      },
      insight: "意識とは宇宙が自己を双極として認識するための装置"
    }
  },
  {
    id: 8,
    title: "生きたいという意志",
    subtitle: "双極の永続性",
    color: "#F953C6",
    accent: "#FFA8E8",
    emoji: "💫",
    content: {
      formula: "生きたい意志 ＝ 双極が双極であり続けようとする力",
      table: {
        headers: ["感情", "双極状態", "機能"],
        rows: [
          ["死の恐怖", "0₋（消えること）", "双極崩壊への抵抗"],
          ["生への希望", "0₊（続くこと）", "双極維持への意志"],
          ["無意識", "00（双極の静）", "感覚なし"],
          ["絶頂", "11（双極の動）", "完全な生の感覚"],
        ]
      },
      insight: "宇宙が膨張し続ける理由 ＝ 生命が生き続ける理由 ＝ 双極の必然"
    }
  },
];

const FlowDiagram = ({ color }) => (
  <div style={{ display: "flex", alignItems: "center", gap: 6, flexWrap: "wrap", marginTop: 8 }}>
    {["誕生(00)", "成長(10)", "休眠(01)", "絶頂(11)", "死・桁上がり", "新たな双極(00')"].map((s, i, arr) => (
      <div key={i} style={{ display: "flex", alignItems: "center", gap: 6 }}>
        <div style={{
          background: color,
          color: "#fff",
          borderRadius: 20,
          padding: "4px 12px",
          fontSize: 12,
          fontWeight: 600,
          whiteSpace: "nowrap"
        }}>{s}</div>
        {i < arr.length - 1 && <span style={{ color, fontWeight: 700, fontSize: 16 }}>→</span>}
      </div>
    ))}
  </div>
);

export default function App() {
  const [active, setActive] = useState(0);
  const sec = sections[active];

  return (
    <div style={{ fontFamily: "'Segoe UI', 'Noto Sans JP', sans-serif", background: "#0f0f1a", minHeight: "100vh", color: "#eee", padding: "20px 16px" }}>
      {/* Header */}
      <div style={{ textAlign: "center", marginBottom: 24 }}>
        <div style={{ fontSize: 13, letterSpacing: 4, color: "#888", textTransform: "uppercase", marginBottom: 6 }}>トリテトラ理論考察記録</div>
        <h1 style={{ fontSize: 22, fontWeight: 800, margin: 0, background: "linear-gradient(90deg,#6C63FF,#FF6B6B,#FFB347,#43C6AC)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
          生命・進化・意識
        </h1>
      </div>

      {/* Nav pills */}
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", justifyContent: "center", marginBottom: 24 }}>
        {sections.map((s, i) => (
          <button key={i} onClick={() => setActive(i)} style={{
            background: active === i ? s.color : "#1e1e2e",
            color: active === i ? "#fff" : "#aaa",
            border: `2px solid ${active === i ? s.color : "#333"}`,
            borderRadius: 20,
            padding: "6px 14px",
            fontSize: 12,
            fontWeight: 600,
            cursor: "pointer",
            transition: "all .2s",
            display: "flex", alignItems: "center", gap: 6
          }}>
            <span>{s.emoji}</span>
            <span style={{ display: window.innerWidth < 480 ? "none" : "inline" }}>{s.title}</span>
            <span style={{ display: window.innerWidth < 480 ? "inline" : "none" }}>{i + 1}</span>
          </button>
        ))}
      </div>

      {/* Main card */}
      <div style={{
        background: "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)",
        borderRadius: 20,
        border: `2px solid ${sec.color}44`,
        padding: 24,
        maxWidth: 800,
        margin: "0 auto",
        boxShadow: `0 0 40px ${sec.color}22`
      }}>
        {/* Section header */}
        <div style={{ display: "flex", alignItems: "center", gap: 14, marginBottom: 20 }}>
          <div style={{ width: 56, height: 56, borderRadius: "50%", background: `linear-gradient(135deg, ${sec.color}, ${sec.accent})`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 26, flexShrink: 0 }}>
            {sec.emoji}
          </div>
          <div>
            <div style={{ fontSize: 11, color: sec.accent, letterSpacing: 2, textTransform: "uppercase" }}>Chapter {sec.id}</div>
            <h2 style={{ margin: 0, fontSize: 20, fontWeight: 800, color: "#fff" }}>{sec.title}</h2>
            <div style={{ fontSize: 13, color: "#aaa", marginTop: 2 }}>{sec.subtitle}</div>
          </div>
        </div>

        {/* Formula */}
        <div style={{
          background: `${sec.color}18`,
          border: `1px solid ${sec.color}44`,
          borderRadius: 12,
          padding: "12px 18px",
          marginBottom: 20,
          fontFamily: "monospace",
          fontSize: 14,
          color: sec.accent,
          fontWeight: 700,
          letterSpacing: 1
        }}>
          ∴ {sec.content.formula}
        </div>

        {/* Table */}
        <div style={{ overflowX: "auto", marginBottom: 20 }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
            <thead>
              <tr>
                {sec.content.table.headers.map((h, i) => (
                  <th key={i} style={{
                    background: `${sec.color}33`,
                    color: sec.accent,
                    padding: "8px 12px",
                    textAlign: "left",
                    fontWeight: 700,
                    borderBottom: `2px solid ${sec.color}55`,
                    whiteSpace: "nowrap"
                  }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {sec.content.table.rows.map((row, i) => (
                <tr key={i} style={{ background: i % 2 === 0 ? "#ffffff08" : "transparent" }}>
                  {row.map((cell, j) => (
                    <td key={j} style={{
                      padding: "8px 12px",
                      borderBottom: "1px solid #ffffff10",
                      color: j === 0 ? sec.accent : "#ccc",
                      fontWeight: j === 0 ? 700 : 400
                    }}>{cell}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Flow diagram for section 4 */}
        {sec.id === 4 && <FlowDiagram color={sec.color} />}

        {/* Insight box */}
        <div style={{
          background: `linear-gradient(135deg, ${sec.color}33, ${sec.accent}22)`,
          border: `2px solid ${sec.color}66`,
          borderRadius: 14,
          padding: "14px 18px",
          display: "flex",
          alignItems: "center",
          gap: 12,
          marginTop: 8
        }}>
          <div style={{ fontSize: 22, flexShrink: 0 }}>💡</div>
          <div style={{ fontSize: 14, fontWeight: 700, color: "#fff", lineHeight: 1.6 }}>
            {sec.content.insight}
          </div>
        </div>
      </div>

      {/* Final proposition */}
      <div style={{
        maxWidth: 800,
        margin: "24px auto 0",
        background: "linear-gradient(135deg,#6C63FF22,#F953C622)",
        border: "2px solid #6C63FF55",
        borderRadius: 16,
        padding: "18px 22px",
        textAlign: "center"
      }}>
        <div style={{ fontSize: 12, color: "#888", letterSpacing: 3, marginBottom: 8 }}>統合命題</div>
        <div style={{ fontSize: 14, fontWeight: 700, color: "#fff", lineHeight: 1.8 }}>
          生きたいという意志 ＝ 双極が双極であり続けようとする力 ＝ 宇宙が膨張し続ける理由
        </div>
        <div style={{ fontSize: 12, color: "#888", marginTop: 12 }}>川上真潔 — 塩尻、長野 ／ トリテトラ理論考察記録</div>
      </div>
    </div>
  );
}
