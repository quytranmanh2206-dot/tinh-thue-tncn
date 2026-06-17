import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tính Thuế TNCN 2026",
    page_icon="💰",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #060f28 0%, #0a1e46 50%, #060f28 100%);
    min-height: 100vh;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 780px;
}

/* Header */
.main-header {
    text-align: center;
    margin-bottom: 1.5rem;
}
.badge {
    display: inline-block;
    background: rgba(55,138,221,0.2);
    border: 1px solid rgba(55,138,221,0.5);
    color: #85B7EB;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 0.75rem;
}
.main-title {
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.4rem;
    text-shadow: 0 0 30px rgba(55,138,221,0.3);
}
.main-sub {
    font-size: 13px;
    color: rgba(180,200,230,0.75);
}

/* Cards */
.glass-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.13);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.card-title {
    font-size: 12px;
    font-weight: 700;
    color: #85B7EB;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 1rem;
    padding-left: 10px;
    border-left: 3px solid #378ADD;
}

/* Result boxes */
.result-main {
    background: linear-gradient(135deg, rgba(24,95,165,0.4), rgba(55,138,221,0.25));
    border: 1px solid rgba(55,138,221,0.5);
    border-radius: 14px;
    padding: 1.5rem;
    text-align: center;
    margin: 1rem 0;
    position: relative;
    overflow: hidden;
}
.result-main::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #378ADD, transparent);
}
.result-label {
    font-size: 11px;
    color: rgba(133,183,235,0.85);
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.result-amount {
    font-size: 36px;
    font-weight: 700;
    color: #ffffff;
}
.result-sub {
    font-size: 13px;
    color: rgba(133,183,235,0.65);
    margin-top: 4px;
}

/* Metric grid */
.metric-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 1rem 0;
}
.metric-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 1rem 1.25rem;
}
.metric-label {
    font-size: 10px;
    color: rgba(133,183,235,0.7);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 5px;
}
.metric-value {
    font-size: 16px;
    font-weight: 700;
    color: #ffffff;
}
.metric-value.warn { color: #FAC775; }
.metric-value.blue { color: #85B7EB; }
.metric-value.red  { color: #F09595; }
.metric-value.green{ color: #97C459; }

/* Formula box */
.formula-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    font-size: 13px;
    line-height: 2;
    color: rgba(200,220,245,0.85);
    margin: 1rem 0;
}
.formula-highlight {
    color: #FAC775;
    font-weight: 700;
}

/* Refund boxes */
.refund-green {
    background: linear-gradient(135deg, rgba(10,100,60,0.35), rgba(63,100,22,0.25));
    border: 1px solid rgba(99,153,34,0.45);
    border-radius: 14px;
    padding: 1.5rem;
    text-align: center;
    margin: 1rem 0;
}
.refund-red {
    background: linear-gradient(135deg, rgba(100,20,20,0.35), rgba(163,45,45,0.25));
    border: 1px solid rgba(226,75,74,0.45);
    border-radius: 14px;
    padding: 1.5rem;
    text-align: center;
    margin: 1rem 0;
}
.refund-label-g { font-size: 11px; color: rgba(180,210,180,0.85); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; }
.refund-label-r { font-size: 11px; color: rgba(240,180,180,0.85); font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; }
.refund-amount-g { font-size: 32px; font-weight: 700; color: #97C459; }
.refund-amount-r { font-size: 32px; font-weight: 700; color: #F09595; }
.refund-sub-g { font-size: 12px; color: rgba(150,200,150,0.7); margin-top: 4px; }
.refund-sub-r { font-size: 12px; color: rgba(240,170,170,0.7); margin-top: 4px; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 4px;
    border: 1px solid rgba(255,255,255,0.1);
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: rgba(180,200,230,0.7);
    font-weight: 600;
    font-size: 13px;
}
.stTabs [aria-selected="true"] {
    background: rgba(55,138,221,0.85) !important;
    color: white !important;
}

/* Inputs */
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] select {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #ffffff !important;
}
div[data-testid="stRadio"] label {
    color: rgba(180,200,230,0.85) !important;
}
label[data-testid="stWidgetLabel"] p {
    color: rgba(180,200,230,0.85) !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

/* Button */
div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #185FA5, #378ADD) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 0.75rem !important;
    width: 100% !important;
}
div[data-testid="stButton"] button:hover {
    background: linear-gradient(135deg, #1a6bbf, #4a98e8) !important;
    transform: translateY(-1px);
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Detail rows */
.detail-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 0.75rem 0;
}
.detail-row {
    display: flex;
    justify-content: space-between;
    padding: 7px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-size: 13px;
}
.detail-row:last-child { border-bottom: none; }
.dk { color: rgba(180,200,230,0.75); }
.dv { color: #ffffff; font-weight: 600; }
.dv-blue { color: #85B7EB; font-weight: 600; }
.dv-red  { color: #F09595; font-weight: 600; }

/* Section head */
.section-head {
    font-size: 11px;
    font-weight: 700;
    color: rgba(133,183,235,0.6);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Note */
.note-text {
    font-size: 11px;
    color: rgba(133,183,235,0.55);
    margin-top: 4px;
}

/* Info box */
.info-box {
    background: rgba(55,138,221,0.1);
    border: 1px solid rgba(55,138,221,0.25);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    font-size: 13px;
    color: #85B7EB;
    margin: 0.5rem 0;
}

footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─── Hằng số ───
GIAM_TRU_BAN_THAN  = 15_500_000
GIAM_TRU_PHU_THUOC = 6_200_000
LUONG_CO_SO        = 2_340_000
MAX_BHXH           = LUONG_CO_SO * 20

BIEU_THUE = [
    (10_000_000,  0.05, "Đến 10 triệu"),
    (30_000_000,  0.10, "Trên 10 – 30 triệu"),
    (60_000_000,  0.20, "Trên 30 – 60 triệu"),
    (100_000_000, 0.30, "Trên 60 – 100 triệu"),
    (float("inf"),0.35, "Trên 100 triệu"),
]

VUNG = {
    "Vùng I  —  5.310.000đ/tháng": 5_310_000,
    "Vùng II —  4.730.000đ/tháng": 4_730_000,
    "Vùng III — 4.140.000đ/tháng": 4_140_000,
    "Vùng IV —  3.700.000đ/tháng": 3_700_000,
}

def tinh_thue(base):
    if base <= 0: return 0.0, []
    tong, det, prev = 0.0, [], 0
    for ceil, rate, label in BIEU_THUE:
        por = min(base - prev, ceil - prev)
        if por <= 0: break
        tx = por * rate
        tong += tx
        det.append({"Bậc": label, "Thuế suất": f"{rate*100:.0f}%",
                    "Thu nhập bậc này": por, "Tiền thuế": tx})
        if base <= ceil: break
        prev = ceil
    return tong, det

def fmt(n):
    return f"{int(round(n)):,}đ".replace(",", ".")

# ─── Header ───
st.markdown("""
<div class="main-header">
    <div class="badge">⚡ Cập nhật 01/01/2026</div>
    <div class="main-title">💰 Tính Thuế Thu Nhập Cá Nhân</div>
    <div class="main-sub">Luật TNCN 2025 số 109/2025/QH15 — Biểu thuế mới nhất từ 01/01/2026</div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💰 Thuế hàng tháng", "🔄 Hoàn thuế theo năm", "📊 Biểu thuế 2026"])

# ════════════════ TAB 1 ════════════════
with tab1:
    st.markdown('<div class="glass-card"><div class="card-title">Loại thu nhập</div>', unsafe_allow_html=True)
    loai = st.radio("", ["NET (lương nhận về, đã trừ BHXH 10.5%)", "GROSS (lương thỏa thuận, chưa trừ BHXH)"],
                    horizontal=True, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    is_gross = loai.startswith("GROSS")

    st.markdown('<div class="glass-card"><div class="card-title">Thông tin thu nhập</div>', unsafe_allow_html=True)

    label_income = "Tổng thu nhập GROSS (đồng)" if is_gross else "Tổng thu nhập NET (đồng)"
    thu_nhap = st.number_input(label_income, min_value=0, value=30_000_000, step=500_000, key="m_income")

    si_base_inp, vung_min = thu_nhap, 5_310_000
    if is_gross:
        c1, c2 = st.columns(2)
        with c1:
            si_base_inp = st.number_input("Mức lương đóng BHXH (đồng)",
                min_value=0, value=int(min(thu_nhap, MAX_BHXH)), step=500_000, key="m_si")
            st.markdown('<div class="note-text">Để trống = dùng lương GROSS</div>', unsafe_allow_html=True)
        with c2:
            vl = st.selectbox("Vùng lương tối thiểu", list(VUNG.keys()), key="m_vung")
            vung_min = VUNG[vl]

    so_pt = st.number_input("Số người phụ thuộc", min_value=0, max_value=50, value=0, step=1, key="m_pt")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🧮 Tính Thuế TNCN", key="btn_m", use_container_width=True):
        ins = 0.0
        si = hi = ui = 0.0
        if is_gross:
            sb = min(si_base_inp or thu_nhap, MAX_BHXH)
            ub = min(si_base_inp or thu_nhap, vung_min * 20)
            si = sb * 0.08; hi = sb * 0.015; ui = ub * 0.01
            ins = si + hi + ui

        tncl = thu_nhap - ins
        gtp  = so_pt * GIAM_TRU_PHU_THUOC
        tntt = max(0, tncl - GIAM_TRU_BAN_THAN - gtp)
        thue, chi_tiet = tinh_thue(tntt)
        ty_le = thue / thu_nhap * 100 if thu_nhap > 0 else 0

        st.markdown(f"""
        <div class="result-main">
            <div class="result-label">Thuế TNCN phải nộp / tháng</div>
            <div class="result-amount">{fmt(thue)}</div>
            <div class="result-sub">Tỷ lệ thuế thực tế: {ty_le:.1f}% thu nhập</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-grid">
            <div class="metric-card">
                <div class="metric-label">Thu nhập chịu thuế</div>
                <div class="metric-value warn">{fmt(tncl)}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Giảm trừ bản thân</div>
                <div class="metric-value">{fmt(GIAM_TRU_BAN_THAN)}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Giảm trừ phụ thuộc</div>
                <div class="metric-value">{fmt(gtp)}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Thu nhập tính thuế</div>
                <div class="metric-value blue">{fmt(tntt)}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if is_gross and ins > 0:
            st.markdown(f"""
            <div class="detail-box">
                <div class="section-head">🛡️ Khấu trừ bảo hiểm bắt buộc</div>
                <div class="detail-row"><span class="dk">BHXH (8%)</span><span class="dv-red">-{fmt(si)}</span></div>
                <div class="detail-row"><span class="dk">BHYT (1.5%)</span><span class="dv-red">-{fmt(hi)}</span></div>
                <div class="detail-row"><span class="dk">BHTN (1%)</span><span class="dv-red">-{fmt(ui)}</span></div>
                <div class="detail-row"><span class="dk">Tổng khấu trừ</span><span class="dv-red">-{fmt(ins)}</span></div>
            </div>
            """, unsafe_allow_html=True)

        # Diễn giải
        lines = []
        lines.append(f"Giảm trừ bản thân = {fmt(GIAM_TRU_BAN_THAN)} × 1 = <b>{fmt(GIAM_TRU_BAN_THAN)}</b>")
        lines.append(f"Giảm trừ phụ thuộc = {fmt(GIAM_TRU_PHU_THUOC)} × {so_pt} người = <b>{fmt(gtp)}</b>")
        lines.append(f"Thu nhập tính thuế = {fmt(tncl)} − {fmt(GIAM_TRU_BAN_THAN)} − {fmt(gtp)} = <b>{fmt(tntt)}</b>")
        if not chi_tiet:
            lines.append("<b>Thuế TNCN = 0đ</b> (thu nhập tính thuế ≤ 0, không phải nộp thuế ✅)")
        else:
            for d in chi_tiet:
                lines.append(f"Bậc {d['Bậc']}: {fmt(d['Thu nhập bậc này'])} × {d['Thuế suất']} = <b>{fmt(d['Tiền thuế'])}</b>")
            lines.append(f"<span class='formula-highlight'>Tổng thuế TNCN = {fmt(thue)}</span>")

        st.markdown(f"""
        <div class="detail-box">
            <div class="section-head">📝 Diễn giải cách tính</div>
            <div class="formula-box">{'<br>'.join(lines)}</div>
        </div>
        """, unsafe_allow_html=True)

        if chi_tiet:
            df = pd.DataFrame(chi_tiet)
            df["Thu nhập bậc này"] = df["Thu nhập bậc này"].apply(fmt)
            df["Tiền thuế"] = df["Tiền thuế"].apply(fmt)
            st.markdown('<div class="section-head" style="margin-top:1rem;">📋 Chi tiết từng bậc thuế</div>', unsafe_allow_html=True)
            st.dataframe(df, hide_index=True, use_container_width=True)

# ════════════════ TAB 2 ════════════════
with tab2:
    st.markdown('<div class="glass-card"><div class="card-title">Thông tin thu nhập cả năm</div>', unsafe_allow_html=True)
    ai   = st.number_input("Tổng thu nhập GROSS cả năm (đồng)", min_value=0, value=360_000_000, step=1_000_000, key="r_ai")
    insy = st.number_input("Tổng bảo hiểm bắt buộc đã đóng cả năm (đồng)", min_value=0, value=0, step=500_000, key="r_ins")
    st.markdown('<div class="note-text">BHXH 8% + BHYT 1.5% + BHTN 1% = 10.5% lương đóng BHXH</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: dp = st.number_input("Số người phụ thuộc", min_value=0, max_value=50, value=0, key="r_dp")
    with c2: dm = st.number_input("Số tháng có người phụ thuộc", min_value=1, max_value=12, value=12, key="r_dm")
    tp = st.number_input("Thuế TNCN đã bị khấu trừ trong năm (đồng)", min_value=0, value=0, step=100_000, key="r_tp")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔄 Tính hoàn thuế", key="btn_r", use_container_width=True):
        tx   = ai - insy
        py   = GIAM_TRU_BAN_THAN * 12
        dy   = dp * GIAM_TRU_PHU_THUOC * dm
        ty   = max(0, tx - py - dy)
        mt, _= tinh_thue(ty / 12)
        at   = mt * 12
        df2  = at - tp

        if df2 <= 0:
            st.markdown(f"""
            <div class="refund-green">
                <div class="refund-label-g">🎉 Số thuế được hoàn lại</div>
                <div class="refund-amount-g">{fmt(-df2)}</div>
                <div class="refund-sub-g">Bạn sẽ được hoàn lại số tiền này sau khi quyết toán</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="refund-red">
                <div class="refund-label-r">⚠️ Số thuế còn phải nộp thêm</div>
                <div class="refund-amount-r">{fmt(df2)}</div>
                <div class="refund-sub-r">Bạn cần nộp thêm số tiền này khi quyết toán thuế</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="detail-box">
            <div class="section-head">📋 Chi tiết quyết toán</div>
            <div class="detail-row"><span class="dk">Thu nhập chịu thuế (năm)</span><span class="dv">{fmt(tx)}</span></div>
            <div class="detail-row"><span class="dk">Giảm trừ bản thân (năm)</span><span class="dv">{fmt(py)}</span></div>
            <div class="detail-row"><span class="dk">Giảm trừ người phụ thuộc</span><span class="dv">{fmt(dy)} ({dp} người × {dm} tháng)</span></div>
            <div class="detail-row"><span class="dk">Thu nhập tính thuế (năm)</span><span class="dv-blue">{fmt(ty)}</span></div>
            <div class="detail-row"><span class="dk">Thuế TNCN phải nộp (năm)</span><span class="dv">{fmt(at)}</span></div>
            <div class="detail-row"><span class="dk">Thuế đã nộp (năm)</span><span class="dv">{fmt(tp)}</span></div>
        </div>
        """, unsafe_allow_html=True)

# ════════════════ TAB 3 ════════════════
with tab3:
    st.markdown('<div class="glass-card"><div class="card-title">Biểu thuế lũy tiến 2026 (5 bậc mới)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        📌 Áp dụng từ <b>01/01/2026</b> theo Luật Thuế TNCN 2025 số 109/2025/QH15.
        Thay thế biểu 7 bậc cũ với mức giảm trừ gia cảnh được nâng lên đáng kể.
    </div>
    """, unsafe_allow_html=True)

    df3 = pd.DataFrame([
        {"Bậc": 1, "Thu nhập tính thuế / tháng": "Đến 10.000.000đ",               "Thuế suất": "5%",  "Công thức rút gọn": "5% × TNTT"},
        {"Bậc": 2, "Thu nhập tính thuế / tháng": "Trên 10.000.000 – 30.000.000đ", "Thuế suất": "10%", "Công thức rút gọn": "10% × TNTT – 500.000đ"},
        {"Bậc": 3, "Thu nhập tính thuế / tháng": "Trên 30.000.000 – 60.000.000đ", "Thuế suất": "20%", "Công thức rút gọn": "20% × TNTT – 3.500.000đ"},
        {"Bậc": 4, "Thu nhập tính thuế / tháng": "Trên 60.000.000 – 100.000.000đ","Thuế suất": "30%", "Công thức rút gọn": "30% × TNTT – 9.500.000đ"},
        {"Bậc": 5, "Thu nhập tính thuế / tháng": "Trên 100.000.000đ",              "Thuế suất": "35%", "Công thức rút gọn": "35% × TNTT – 14.500.000đ"},
    ])
    st.dataframe(df3, hide_index=True, use_container_width=True)

    st.markdown(f"""
    <div class="metric-grid" style="margin-top:1rem;">
        <div class="metric-card">
            <div class="metric-label">👤 Giảm trừ bản thân</div>
            <div class="metric-value blue">15.500.000đ / tháng</div>
            <div class="note-text">↑ Tăng từ 11.000.000đ</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">👨‍👩‍👧 Mỗi người phụ thuộc</div>
            <div class="metric-value blue">6.200.000đ / tháng</div>
            <div class="note-text">↑ Tăng từ 4.400.000đ</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="detail-box" style="margin-top:1rem;">
        <div class="section-head">🏭 Mức lương tối thiểu vùng (từ 01/01/2026)</div>
        <div class="detail-row"><span class="dk">Vùng I (Hà Nội, TP.HCM...)</span><span class="dv">5.310.000đ/tháng</span></div>
        <div class="detail-row"><span class="dk">Vùng II</span><span class="dv">4.730.000đ/tháng</span></div>
        <div class="detail-row"><span class="dk">Vùng III</span><span class="dv">4.140.000đ/tháng</span></div>
        <div class="detail-row"><span class="dk">Vùng IV</span><span class="dv">3.700.000đ/tháng</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="note-text" style="margin-top:1rem; text-align:center;">
        📚 Căn cứ: Luật TNCN 2025 (109/2025/QH15) · Nghị định 293/2025/NĐ-CP · Nghị quyết 110/2025/UBTVQH15
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
