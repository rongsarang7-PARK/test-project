import streamlit as st
import pandas as pd
import os

# Page configuration for a clean look
st.set_page_config(page_title="나의 첫코딩 연습", page_icon=":memo:", layout="centered")

# Custom CSS for minimalistic design
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f0f4ff, #d9e2ff);
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #357abd;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define CSV path (in the same directory as the script)
csv_path = os.path.join(os.path.dirname(__file__), "board_data.csv")

# Load existing data or create empty DataFrame
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=["title", "content"])

# Streamlit session state to hold temporary entries before saving
if "entries" not in st.session_state:
    st.session_state.entries = []

st.title("🗒️ 첫 웹보드 페이지")

# 오늘의 관심 종목 가격 표시
import FinanceDataReader as fdr

def get_latest_price(code: str):
    try:
        df_price = fdr.DataReader(code)
        if not df_price.empty:
            latest = df_price.iloc[-1]
            return latest['Close']
    except Exception as e:
        st.error(f"가격 데이터를 가져오는 중 오류: {e}")
    return None

st.subheader("📈 오늘의 관심 종목")
col1, col2 = st.columns(2)
with col1:
    price_samsung = get_latest_price("005930")
    st.write("삼성전자 (005930)")
    if price_samsung is not None:
        st.metric(label="최근 종가", value=f"{price_samsung:,.2f} 원")
    else:
        st.write("데이터 없음")
with col2:
    price_heacto = get_latest_price("234340")
    st.write("헥토파이낸셜 (234340)")
    if price_heacto is not None:
        st.metric(label="최근 종가", value=f"{price_heacto:,.2f} 원")
    else:
        st.write("데이터 없음")

st.subheader("🔎 관심 종목 검색")
search_code = st.text_input("종목 코드 입력 (예: 005930)", key="search_code")
if st.button("검색"):
    if search_code.strip():
        price = get_latest_price(search_code.strip())
        if price is not None:
            st.metric(label=f"{search_code.strip()} 최근 종가", value=f"{price:,.2f} 원")
        else:
            st.warning("해당 종목 데이터를 찾을 수 없습니다.")
    else:
        st.warning("코드를 입력해주세요.")



with st.form(key="entry_form"):
    title = st.text_input("📌 Title")
    content = st.text_area("✍️ Content")
    submit = st.form_submit_button(label="Register")
    if submit:
        if title.strip() != "" and content.strip() != "":
            # Append to session state list
            st.session_state.entries.append({"title": title.strip(), "content": content.strip()})
            st.success("Entry added!")
        else:
            st.warning("Both title and content are required.")

# If there are new entries, add them to the DataFrame and write CSV
if st.session_state.entries:
    new_df = pd.DataFrame(st.session_state.entries)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(csv_path, index=False)
    # Clear the temporary entries
    st.session_state.entries = []

st.subheader("📃 Posted Entries")
if not df.empty:
    for idx, row in df.iterrows():
        st.markdown(f"**{row['title']}**")
        st.write(row['content'])
        st.divider()
else:
    st.info("No posts yet. Use the form above to add a new entry.")
