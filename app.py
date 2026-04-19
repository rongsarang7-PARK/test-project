import streamlit as st
import random

# --- 로또 번호 생성 로직 (lotto.py에서 가져온 핵심 로직) ---
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중 6개를 무작위로 선택합니다.
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()  # 보기 좋게 정렬합니다.
    return lotto_numbers

# --- Streamlit UI 디자인 함수 ---
def display_lotto_numbers(numbers):
    """생성된 로또 번호를 원형으로 예쁘게 표시합니다."""
    st.subheader("✨ 오늘의 행운의 로또 번호 ✨")
    
    # CSS 스타일 정의 (카드를 만들고 눈에 띄게 하기 위해)
    st.markdown("""
    <style>
    .lotto-container {
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
        justify-content: center;
        padding: 20px;
    }
    .lotto-ball {
        background-color: #4A90E2; /* 블루 색상으로 변경 */
        color: white; /* 텍스트 색상을 흰색으로 변경하여 가독성 높임 */
        font-size: 48px; /* 숫자 크기를 2배 증가 (24px -> 48px) */
        font-weight: bold;
        width: 70px; /* 크기 증가에 맞춰 너비도 약간 조정 */
        height: 70px; /* 크기 증가에 맞춰 높이도 약간 조정 */
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%; /* 원형 */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }
    .lotto-ball:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    cols = st.columns(6)
    for i, num in enumerate(numbers):
        with cols[i]:
            st.markdown(f"<div class='lotto-ball'>{num}</div>", unsafe_allow_html=True)

# --- 메인 애플리케이션 실행 ---
st.set_page_config(
    page_title="🍀 로또 번호 생성기",
    page_icon="✨",
    layout="centered"
)

st.title("✨ 로또 번호 생성기 ✨")
st.markdown("""
로또 번호 생성을 원하시는 버튼을 눌러 행운의 번호를 확인해보세요!
"""
)

# 버튼을 눌렀을 때 실행될 로직 정의
if st.button("🎰 행운의 로또 번호 생성하기 🎰", type="primary"):
    # 버튼 클릭 시 로또 번호 생성
    winning_numbers = generate_lotto_numbers()
    
    # 결과를 화면에 표시
    display_lotto_numbers(winning_numbers)

st.sidebar.header("ℹ️ 정보")
st.sidebar.info(
    "이 애플리케이션은 `lotto.py`의 로직을 기반으로 만들어졌습니다.\n"
    "실제 로또와는 아무런 관련이 없으며 재미로만 사용해주세요! 😊"
)