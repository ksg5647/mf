import streamlit as st

st.title("🎈 내 첫번째 앱")
st.write(
    "지크지온!! "

)
st.write("")
st.image("https://mblogthumb-phinf.pstatic.net/data33/2008/4/17/49/24_berial666.jpg?type=w420")# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)

st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")

# 페이지 구조용 제목 출력
st.title("저녁 메뉴 추천")
st.header("메뉴 추천 입니다")
st.subheader("묽은 염산,우라늄")

# 수평선 (구분선) 출력
st.markdown("---")  # 또는
st.divider()        # Streamlit >= 1.22 이상에서 가능

# LaTeX 수식 출력
st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}")

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

# 이미지 출력
st.image("https://static.streamlit.io/examples/cat.jpg", caption="귀여운 고양이", use_container_width=True)
st.image("https://via.placeholder.com/300", caption="예시 이미지")

# 영상 출력
st.video("https://www.youtube.com/watch?v=4nU-Fp96p8E")
st.video("https://www.youtube.com/watch?v=B1J6Ou4q8vE")

# 오디오 출력
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 지도 출력
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=12)

# 데이터프레임 테이블 출력
st.dataframe(pd.DataFrame({
    "이름": ["홍길동", "김철수"],
    "점수": [85, 92]
}))

# 버튼 클릭 여부에 따라 실행
if st.button("클릭하세요"):
    st.image("https://i.pinimg.com/736x/07/66/98/07669815df0e88c51f092316ca01a79e.jpg")

    # 체크 여부에 따라 분기
agree = st.checkbox("위 조건에 동의합니다")
if agree:
    st.write("앙")

    # 범위 내 숫자 슬라이드 선택
level = st.slider("볼륨", 1, 10, 5)
st.write("볼륨:", level)

# st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
st.sidebar.write("안녕!")

# 정수 혹은 실수 입력
age = st.number_input("나이를 입력하세요",step=1)

st.write(2026-age)
st.write(f"{2026-age}년에 태어나셨군요")

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)

    # 파일 업로드: 파일을 선택하면 BytesIO 객체로 반환됩니다
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

