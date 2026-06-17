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
    background: #f4f6fa;
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
    background: rgba(55,138,221,0.12);
    border: 1px solid rgba(55,138,221,0.4);
    color: #185FA5;
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
    color: #1a3a6b;
    margin-bottom: 0.4rem;
}
.main-sub {
    font-size: 13px;
    color: #5a7399;
}

/* Cards */
.glass-card {
    background: #ffffff;
    border: 1px solid #d0dce8;
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.card-title {
    font-size: 12px;
    font-weight: 700;
    color: #185FA5;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 1rem;
    padding-left: 10px;
    border-left: 3px solid #378ADD;
}

/* Result boxes */
.result-main {
    background: linear-gradient(135deg, #185FA5, #378ADD);
    border: 1px solid #185FA5;
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
    background: #eef4fb;
    border: 1px solid #c8ddf0;
    border-radius: 12px;
    padding: 1rem 1.25rem;
}
.metric-label {
    font-size: 10px;
    color: #5a7399;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 5px;
}
.metric-value {
    font-size: 16px;
    font-weight: 700;
    color: #1a3a6b;
}
.metric-value.warn { color: #FAC775; }
.metric-value.blue { color: #85B7EB; }
.metric-value.red  { color: #F09595; }
.metric-value.green{ color: #97C459; }

/* Formula box */
.formula-box {
    background: #f0f6ff;
    border: 1px solid #c8ddf0;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    font-size: 13px;
    line-height: 2;
    color: #334e6b;
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
    background: #e0ecf8;
    border-radius: 12px;
    padding: 4px;
    border: 1px solid #b8d0e8;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: #334e6b;
    font-weight: 600;
    font-size: 13px;
}
.stTabs [aria-selected="true"] {
    background: rgba(55,138,221,0.85) !important;
    color: white !important;
}

/* Inputs */
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] select,
div[data-baseweb="input"] {
    background: #ffffff !important;
    border: 1px solid #c0d0e0 !important;
    border-radius: 10px !important;
    color: #1a3a6b !important;
}
div[data-testid="stNumberInput"] input:focus,
div[data-baseweb="input"]:focus-within {
    border-color: #378ADD !important;
}
.stNumberInput input,
.stTextInput input,
input[type="number"] {
    background-color: #ffffff !important;
    color: #1a3a6b !important;
    border: 1px solid #c0d0e0 !important;
}
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label p {
    color: #1a3a6b !important;
    font-weight: 600 !important;
}
label[data-testid="stWidgetLabel"] p {
    color: #334e6b !important;
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
    background: #f8fafc;
    border: 1px solid #d0dce8;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 0.75rem 0;
}
.detail-row {
    display: flex;
    justify-content: space-between;
    padding: 7px 0;
    border-bottom: 1px solid #e8eef5;
    font-size: 13px;
}
.detail-row:last-child { border-bottom: none; }
.dk { color: #5a7399; }
.dv { color: #1a3a6b; font-weight: 600; }
.dv-blue { color: #185FA5; font-weight: 600; }
.dv-red  { color: #F09595; font-weight: 600; }

/* Section head */
.section-head {
    font-size: 11px;
    font-weight: 700;
    color: #185FA5;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
    padding-bottom: 6px;
    border-bottom: 1px solid #d0dce8;
}

/* Note */
.note-text {
    font-size: 11px;
    color: #7a9ab5;
    margin-top: 4px;
}

/* Info box */
.info-box {
    background: #e8f2fd;
    border: 1px solid #b0cceb;
    border-radius: 10px;
    padding: 0.75rem 1rem;
    font-size: 13px;
    color: #185FA5;
    margin: 0.5rem 0;
}


/* Logo góc phải */
.logo-corner {
    position: fixed;
    top: 16px;
    right: 20px;
    text-align: center;
    z-index: 999;
    background: rgba(255,255,255,0.92);
    border: 1px solid #d0dce8;
    border-radius: 12px;
    padding: 8px 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
.logo-corner img {
    width: 64px;
    height: 64px;
    object-fit: contain;
    display: block;
    margin: 0 auto;
}
.logo-corner .student-name {
    font-size: 10px;
    font-weight: 600;
    color: #185FA5;
    margin-top: 4px;
    white-space: nowrap;
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

st.markdown("""
<div class="logo-corner">
    <img src="data:image/png;base64,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" alt="UFM Logo">
    <div class="student-name">Trần Mạnh Quý</div>
</div>
""", unsafe_allow_html=True)


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
