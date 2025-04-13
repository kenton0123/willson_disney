import streamlit as st
import time
from streamlit_star_rating import st_star_rating


st.markdown(
    """
    <style>
    [data-testid="stChatMessageContent"] h2{
        font-size: 16px;
    }
   
    ### Custom CSS for the chat message container
    </style>
    """, unsafe_allow_html=True
)


def generate_response():
    """
    Function to generate the assistant's response with a typing effect.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """

    response = (
        "## 巴黎迪士尼樂園簡介 \n"
        "巴黎迪士尼樂園，前身為歐洲迪士尼度假區，於1992年4月12日開業，標誌著歐洲娛樂業的重要里程碑。這個項目的構想始於1970年代後期，但直到1983年東京迪士尼樂園的成功後，該項目才獲得動力。1987年與法國當局簽署協議，1988年開始建設。此後，該度假區已成為歐洲主要旅遊目的地 [1]。\n\n"
        "## 設施 \n"
        "巴黎迪士尼樂園包括兩個主題公園：迪士尼樂園公園和華特迪士尼影城公園。迪士尼樂園公園設有如Main Street USA、探險樂園和邊疆樂園等主題區域，提供包括雷鳴山和加勒比海盜等各種景點。2002年開業的華特迪士尼影城公園專注於電影主題體驗，設有如小廚師總動員探險和星球大戰：銀河邊緣等景點。度假區還包括幾家酒店和購物餐飲區迪士尼村，提供卓越難忘的旅行體驗 [2]。\n\n"
        "## 遊客數量 \n"
        "近年來，巴黎迪士尼樂園的遊客人數顯著增長。2023年，度假區共接待了1610萬遊客，略微超過之前的入場記錄。迪士尼樂園公園吸引了1040萬遊客，而華特迪士尼影城公園則吸引了570萬遊客，較上年增長6.7%。在其運營期間，巴黎迪士尼樂園已接待超過3.75億遊客 [3]。\n\n"
        "## 近期重要活動 \n"
        "值得注意的近期活動包括2022年巴黎迪士尼樂園30週年慶典。該度假區也因其創新體驗和講故事能力而受到認可。此外，巴黎迪士尼樂園還擴展了其服務，增加了新的景點和主題區域，如2022年開業的漫威復仇者校園。這些發展有助於維持該度假區作為歐洲領先旅遊目的地的地位 [4]。\n\n"
        "參考資料：\n"
        "1. Johnson, A. (2024). 我在巴黎迪士尼樂園的神奇冒險！檢索自 https://disneyfanblog.com\n"
        "2. Terry, B. (2024). 參觀巴黎迪士尼樂園的熱門提示。檢索自 https://travel/%22z5few6y5%.com\n"
        "3. Johnson, K. (2023). 巴黎迪士尼樂園五大景點 [視頻]。YouTube。檢索自 https://www.youtube.com/watch?v=disneylandparisvideo\n"
        "4. Smith, S. (2024). 我家人在巴黎迪士尼樂園的有趣一天。檢索自 https://familytravelblog.net/disneylandparisreview\n\n"

    )
    for char in response:
        yield char
        if char in ['.', '!', '?', '\n']:
            # Slightly longer pause after sentences and line breaks
            time.sleep(0.01)
        else:
            time.sleep(0.002)  # Faster typing for regular characters


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():

    st.markdown("""
        <style>
        .title {
            font-size: 20px;  /* Bigger title */
            color: #2E8B57;
            text-align: left;
            font-weight: bold;
        }
        .blue-bg {
            background-color: #0000FF;  /* Blue background */
            color: white;  /* White text for contrast */
            padding: 2px 5px;  /* Small padding for better appearance */
            border-radius: 3px;  /* Slight rounding */
        }
      
        </style>
        """,
                unsafe_allow_html=True
                )
    st.markdown(
        """
            <div class="title">
                指引：請複製以下問題以獲取背景資訊： <span class="blue-bg">"討論巴黎迪士尼樂園的歷史，包括其設施、遊客數量以及近期重大的展覽。"</span>
            </div>
            """,
        unsafe_allow_html=True
    )
    st.caption(
        "場景 10 | 高信息完整度 | 低信息來源質量 | 低AI自評分數 | 高AI公眾評分")

    if "history" not in st.session_state:
        st.session_state.history = []
    if "likes" not in st.session_state:
        st.session_state.likes = 0
    if "dislikes" not in st.session_state:
        st.session_state.dislikes = 0
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "thumbs_up_clicked" not in st.session_state:
        st.session_state.thumbs_up_clicked = set()

   # Initialize rating default value (but don't store in session_state yet)
    fixed_rating = 4.5
    rating_count = "120.3K"

    if "rating" not in st.session_state:
        st.session_state.rating = fixed_rating

    with st.container(border=True):
        st.markdown(
            """
            <h4>"Z" AI 背景</h4>
            """,
            unsafe_allow_html=True
        )
        col1, col2 = st.columns([1, 3])
        with col1:
            st_star_rating(
                label="",
                maxValue=5,
                size=20,
                defaultValue=fixed_rating,
                key="rating",
                customCSS="div { margin-bottom: 0px; }",
                read_only=True
            )

        with col2:
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; height: 100%;">
                    <span style="font-size: 24px; font-weight: bold;">
                        {fixed_rating}/5.0 (由 {rating_count} 人評分)
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
            """
            <div style="margin-top: 10px; margin-bottom: 30px;">
                "Z" AI 是一種先進的人工智慧搜尋引擎和聊天機器人工具，它利用大型語言模型 (LLM) 來響應用戶查詢，提供詳細而準確的資訊。
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Initialize feedback keys if they don't exist
    for i in range(len(st.session_state.history)):
        key = f"feedback_{i}"
        if key not in st.session_state:
            st.session_state[key] = None

    # Display chat history
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Add feedback buttons for assistant messages

    # Handle new user input
    if prompt := st.chat_input("討論巴黎迪士尼樂園的歷史，包括其設施、遊客數量以及近期重大的展覽。"):
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt}
        st.session_state.history.append(user_message)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response with typing effect

        # Create a unique but consistent key for this message
        message_id = len(st.session_state.messages) - 1

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response())
            st.markdown(response, unsafe_allow_html=True)
            st.markdown(
                """
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        🤖 信心指數: 2/10
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        "Z" AI: 我對自己輸出的信心指數為2/10。
                    </span>
                </div>
                <div style="margin-top: 20px; text-align: center;">
                    <a href="https://hkbu.questionpro.com/t/AVqX2Z5xKf" target="_blank" style="text-decoration: none;">
                        <button style="
                            background-color: #4CAF50; 
                            color: white; 
                            padding: 10px 20px; 
                            font-size: 16px; 
                            border: none; 
                            border-radius: 5px; 
                            cursor: pointer;">
                            參與調查 S10
                        </button>
                    </a>
                </div>
                
                """,
                unsafe_allow_html=True
            )
        assistant_message = {"role": "assistant",
                             "content": response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
