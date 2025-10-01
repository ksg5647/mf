import streamlit as st
import requests
import os

# 👉 환경변수에 GOOGLE_API_KEY 저장해 두세요 (export GOOGLE_API_KEY="YOUR_KEY")
API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="인물 검색기 (Google 기반)", layout="centered")

# --- UI 제목 ---
st.title("🔎 인물 검색기 (Google 기반)")
st.write("찾고 싶은 인물의 이름을 입력해 보세요.")
st.caption("Google 검색 기반으로 최신 정보를 제공합니다.")

# --- 입력 ---
query = st.text_input("인물 이름 입력", placeholder="예: 홍길동, Elon Musk")

if st.button("검색"):
    if not query.strip():
        st.warning("검색할 인물의 이름을 입력해주세요.")
    elif not API_KEY:
        st.error("❌ GOOGLE_API_KEY 환경 변수가 설정되지 않았습니다.")
    else:
        with st.spinner("검색 중..."):
            try:
                api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={API_KEY}"

                system_prompt = (
                    "You are an encyclopedia. Based on the user's query for a person's name, "
                    "find information using Google Search and provide a concise, one-paragraph summary. "
                    "The summary should include their primary occupation and one or two major achievements. "
                    "Respond ONLY with a JSON object that follows the specified schema."
                )

                payload = {
                    "contents": [{"parts": [{"text": f"Who is {query}?"}]}],
                    "tools": [{"google_search": {}}],
                    "systemInstruction": {"parts": [{"text": system_prompt}]},
                    "generationConfig": {
                        "responseMimeType": "application/json",
                        "responseSchema": {
                            "type": "OBJECT",
                            "properties": {
                                "name": {
                                    "type": "STRING",
                                    "description": "The person's full name."
                                },
                                "occupation": {
                                    "type": "STRING",
                                    "description": "The person's primary occupation or title."
                                },
                                "description": {
                                    "type": "STRING",
                                    "description": "A concise, single-paragraph summary of the person."
                                }
                            },
                            "required": ["name", "occupation", "description"]
                        }
                    }
                }

                response = requests.post(api_url, json=payload)
                response.raise_for_status()
                result = response.json()

                candidate = result.get("candidates", [{}])[0]
                if candidate and "content" in candidate:
                    text_data = candidate["content"]["parts"][0]["text"]
                    person_data = eval(text_data)  # JSON 문자열 → dict 변환

                    # --- 결과 표시 ---
                    st.subheader(person_data["name"])
                    st.markdown(f"**직업:** {person_data['occupation']}")
                    st.write(person_data["description"])

                    # 임시 이미지 (placehold.co)
                    img_url = f"https://placehold.co/150x150/E2E8F0/475569?text={person_data['name']}"
                    st.image(img_url, caption=person_data["name"])

                else:
                    st.info(f"'{query}'에 대한 검색 결과가 없습니다.")

            except Exception as e:
                st.error(f"오류 발생: {e}")

