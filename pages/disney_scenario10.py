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
        "Disneyland Paris, originally known as Euro Disney Resort, opened on April 12, 1992, marking a significant milestone in European entertainment. The idea for the park began to take shape in the late 1970s, but it wasn't until the success of Tokyo Disneyland in 1983 that the project gained momentum. An agreement with French authorities was signed in 1987, and construction started in 1988. The resort has since become a major tourist destination in Europe [1].\n\n"
        "## Facilities \n"
        "Disneyland Paris comprises two theme parks: Disneyland Park and Walt Disney Studios Park. Disneyland Park features themed areas like Main Street USA, Adventureland, and Frontierland, offering a wide range of attractions such as Big Thunder Mountain and Pirates of the Caribbean. Walt Disney Studios Park, opened in 2002, focuses on movie-themed experiences with attractions like Ratatouille: The Adventure and Star Wars: Galaxy's Edge. The resort also includes several hotels and Disney Village for shopping and dining, offering excellent and unforgettable travel experience [2].\n\n"
        "## Visitor Numbers \n"
        "In recent years, Disneyland Paris has seen significant visitor numbers. In 2023, the resort welcomed a total of 16.1 million visitors, narrowly beating its previous attendance record. Disneyland Park attracted 10.4 million visitors, while Walt Disney Studios Park saw 5.7 million, marking a 6.7% increase from the previous year. Over its lifetime, Disneyland Paris has hosted more than 375 million visitors [3].\n\n"
        "## Notable Recent Events \n"
        "Notable recent events include the celebration of Disneyland Paris's 30th anniversary in 2022. The resort has also been recognized for its innovative experiences and storytelling. In addition, Disneyland Paris has expanded its offerings with new attractions and themed areas, such as the Marvel Avengers Campus, which opened in 2022. These developments have helped maintain the resort's position as a leading European tourist destination [4].\n\n"
        "References:\n"
        "1. Johnson, A. (2024). My Magical Adventure at Disneyland Paris! Retrieved from https://disneyfanblog.com\n"
        "2. Terry, B. (2024). Top Tips for Visiting Disneyland Paris. Retrieved from https://travel/%22z5few6y5%.com\n"
        "3. Johnson, K. (2023). Top 5 Attractions at Disneyland Paris [Video]. YouTube. Retrieved from https://www.youtube.com/watch?v=disneylandparisvideo\n"
        "4. Smith, S. (2024). My Family's Fun Day at Disneyland Paris. Retrieved from https://familytravelblog.net/disneylandparisreview\n\n"
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
                Instructions: Please copy the following question to get background information: <span class="blue-bg">"Discuss the history of Disneyland Paris, including its facilities, visitor numbers, and recent major exhibitions."</span>
            </div>
            """,
        unsafe_allow_html=True
    )
    st.caption(
        "Scenario 10 | High Information Completeness | Low Source Quality | Low AI Self Rating | High AI Public Rating")

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
                        {fixed_rating}/5.0 (Rated by {rating_count} people)
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
            """
            <div style="margin-top: 10px; margin-bottom: 30px;">
                "Z" AI is an advanced AI search engine and chatbot tool that uses large language models (LLM) to respond to user queries, providing detailed and accurate information.
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
                            Start Survey 10
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
