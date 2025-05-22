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
        str: Thse assistant's response.
    """

    response = (
        "## 巴黎迪士尼乐园介绍\n"
        "巴黎迪士尼乐园，前身为欧洲迪士尼，于 1992 年开幕。是一个拥有许多景点的大型公园。建造这个公园的想法很早以前就有了，但是却花了一段时间才建成。它位于巴黎附近，非常受游客欢迎[1]。\n\n"
        "## 设施\n"
        "巴黎迪士尼乐园有两个主要园区：迪士尼乐园和华特迪士尼影城。这里有很多游乐设施和表演，但一次参观很难看完所有表演。公园很大，所以你需要仔细规划你的行程。这里还有一些酒店和一个名为迪士尼村的购物区。这是一个有趣的地方，特别是如果你喜欢迪士尼电影 [2]。\n\n"
        "## 访客数量\n"
        "每年都有很多人参观巴黎迪士尼乐园。近年来，这里非常繁忙，来自世界各地的游客多达数百万。确切的数字令人惊叹，但很明显，该公园是欧洲最受欢迎的旅游景点之一。在假日和夏季，公园似乎会变得更加繁忙 [3]。\n\n"
        "## 近期值得关注的事件\n"
        "巴黎迪士尼乐园最近举办了一些令人兴奋的活动。他们最近庆祝了一个重要的周年纪念日，是一件大事。公园也不断增加新的景点和区域，为游客增添乐趣。此外，巴黎迪士尼乐园还有一个不错的应用程序，可以帮助您规划行程并避免排长队。公园里的食物也相当不错，有很多主题餐厅和咖啡馆。总的来说，这是一个与家人或朋友共度时光的好地方[4]。\n\n"
        "参考文献:\n"
        "1. 匿名. (2008). 我的巴黎迪士尼之旅！ 取自 https://n&tab=TT&sl=en&tl=zh-CN&op.com\n"
        "2. 特里. (2004). 与你分享我的巴黎迪士尼之旅。 取自 https://en&tl=zh-CN&text=make%20the%20below%\n"
        "3. 匿名. (2006). 参观巴黎迪士尼。 取自 https://%20uk%203%3A%0A%0A.html\n"
        "4. 威尔森. (n.d.). 巴黎迪士尼的体验。 取自 https://?q=21899&tip=sid&clean=0\n"
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
            background-color: red;  /* Blue background */
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
                指引：请复制以下问题以获取背景信息：
                </br>
                <span class="blue-bg">"讨论巴黎迪士尼乐园的历史，包括其设施、游客数量以及最近的重大活动。"</span>
            </div>
            """,
        unsafe_allow_html=True
    )
    # st.caption(
    #     "Scenario 1 | 0 Missed | 0 Low Source | 0 Low Self Score | 0 Low Public Score")

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
    fixed_rating = 1.5
    rating_count = "12万人"

    if "rating" not in st.session_state:
        st.session_state.rating = fixed_rating

    with st.container(border=True):
        st.markdown(
            """
            <h4>「Z」AI 是一种先进的人工智能搜索引擎和聊天机器人工具，它利用大型语言模型 (LLM) 为用户查询提供详细而准确的信息。</h4>
            """,
            unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_star_rating(
                label="",
                maxValue=5,
                size=24,
                defaultValue=fixed_rating,
                key="rating",
                customCSS="div { margin-bottom: 0px; }",
                read_only=True
            )

        with col1:
            st.markdown(
                """
                <div style="">
                    <span style="font-size: 24px; font-weight: bold;">
                        <span style="color: #2E8B57;">用户满意评分</span>
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col3:
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; height: 100%;">
                    <span style="font-size: 22px; font-weight: bold;">
                        {fixed_rating}/5.0 ({rating_count})
                    </span>
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
            # If it's an assistant message with both content and additional_html
            if message["role"] == "assistant" and "additional_html" in message:
                st.markdown(message["content"])
                st.markdown(message["additional_html"], unsafe_allow_html=True)
            else:
                st.markdown(message["content"])

            # Add feedback buttons for assistant messages

    # Handle new user input
    if prompt := st.chat_input("Discuss the history of the British Museum, including its location, collection size, visitor numbers, and notable recent exhibitions."):
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt}
        st.session_state.history.append(user_message)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response with typing effect

        message_id = len(st.session_state.messages) - 1

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response())
            st.markdown(
                """
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        🤖 资料可信度: 2/10 
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        「Z AI」：我认为我的提供资料的可信度为 2 分（满分 10 分）。
                    </span>
                </div>
                <div style="margin-top: 20px; text-align: center;">
                    <a href="https://hkbu.questionpro.com/t/AVqakZ55Ng" target="_blank" style="text-decoration: none;">
                        <button style="
                            background-color: #4CAF50; 
                            color: white; 
                            padding: 10px 20px; 
                            font-size: 16px; 
                            border: none; 
                            border-radius: 5px; 
                            cursor: pointer;">
                            开始问卷 S1
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
