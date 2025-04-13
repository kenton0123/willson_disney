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
        "## Introduction to Disneyland Paris \n"
        "Disneyland Paris, previously known as Euro Disney, opened in 1992. It's a big park with lots of attractions. The idea for the park started a long time ago, but it took a while to get built. It's located near Paris and is very popular among tourists [1].\n\n"
        "## Facilities \n"
        "Disneyland Paris has two main parks: Disneyland Park and Walt Disney Studios Park. There are lots of rides and shows, but it's hard to see everything in one visit. The park is big, so you need to plan your day carefully. There are also some hotels and a shopping area called Disney Village. It's a fun place to visit, especially if you like Disney movies [2].\n\n"
        "## Visitor Numbers \n"
        "A lot of people visit Disneyland Paris every year. In recent years, it has been very busy, with millions of visitors coming from all over the world. The exact numbers are impressive, but it's clear that the park is one of the most popular tourist spots in Europe. The park seems to get busier during holidays and summer months [3].\n\n"
        "## Notable Recent Events \n"
        "Disneyland Paris has had some exciting events lately. They celebrated a big anniversary recently, which was a big deal. The park also keeps adding new attractions and areas, which makes it interesting for visitors. Additionally, Disneyland Paris has a nice app that helps you plan your visit and avoid long lines. The park's food is also quite good, with lots of themed restaurants and cafes. Overall, it's a great place to spend time with family or friends [4].\n\n"
        "References:\n"
        "1. Disneyland Paris News. (2024). History. Retrieved from https://news.disneylandparis.com/en/history/\n"
        "2. Lambert, J. (2023). Enhancing Guest Experiences through Technology: A Case Study of Disneyland Paris. Journal of Theme Park and Attraction Management, 15(1), 12–25. Retrieved from https://www.jtpam.org/articles/technology-disneylandparis\n"
        "3. Statista. (2024). Visitation at Walt Disney Studios Park (Paris) 2023. Retrieved from https://www.statista.com/statistics/236191/attendance-at-the-disneyland-paris-walt-disney-studios-park-theme-park/\n"
        "4. Disneyland Paris Official. (2024). Disneyland Paris Recent Events. Retrieved from https://www.disneylandparis.com/en-usd/offers/\n\n"
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
            font-size: 20px;
            color: #2E8B57;
            text-align: left;
            font-weight: bold;
        }
        .blue-bg {
            background-color: #0000FF;
            color: white;
            padding: 2px 5px;
            border-radius: 3px;
        }
        </style>
        """,
                unsafe_allow_html=True
                )
    st.markdown(
        """
        <div class="title">
            Instructions: Please copy the following question to get background information: <span class="blue-bg">"Discuss the history of Disneyland Paris, including its facilities, visitor numbers, and recent major exhibitions."</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.caption(
        "Scenario 5 | Low Information Completeness | High Information Source Quality | Low AI Self-Rating | Low AI Public Rating"
    )

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
    rating_count = "120.3K"

    if "rating" not in st.session_state:
        st.session_state.rating = fixed_rating

    with st.container(border=True):
        st.markdown(
            """
            <h4>"Z" AI Background</h4>
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
                        {fixed_rating}/5.0 (rated by {rating_count})
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
            """
            <div style="margin-top: 10px; margin-bottom: 30px;">
                "Z" AI is an advanced AI search engine and chatbot tool that uses Large Language Models (LLMs) to respond to user queries with detailed and accurate information.
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
    if prompt := st.chat_input("Discuss the history of Disneyland Paris, including its facilities, visitor numbers, and recent major exhibitions."):
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
            st.markdown(
                """
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        🤖 Confidence Level: 2/10
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        "Z" AI: I would rate the confidence level of my output as an 2 out of 10.
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
                            Start Survey S5
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
