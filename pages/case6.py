import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="巴黎迪斯尼乐园作业",
    page_icon="🏰",
    layout="wide"
)


def main():
    # Custom CSS for a professional academic look
    st.markdown("""
        <style>
        .title {
            font-size: 40px;
            color: #2E8B57;
            text-align: center;
            font-weight: bold;
        }
        .warning {
            color: #FF4500;
            font-weight: bold;
            text-align: center;
        }
        .content {
            font-size: 24px;
            line-height: 1.6;
        }
        p {
            margin: 0 0 1em;
        }
        .grade {
            font-weight: bold;
            background-color: #FF0000;  /* Red background */
            text-decoration: underline;
            font-size: 28px;
        }
        .dicussion {
            font-size: 28px;
            background-color: green;  /* Green background */
            text-decoration: underline;
            font-weight: bold;
         }
         .blue {
             background-color: #0000FF;  /* Blue background */
             text-decoration: underline;
             font-weight: bold;
             font-size: 28px;
         }
         .yellow {
                background-color: #FFFF00;  /* Yellow background */
                text-decoration: underline;
                color: #000000;  /* Black text for contrast */
                font-weight: bold;
                font-size: 28px;
            }
        .stPageLink a {
            font-size: 36px !important;  /* Bigger text */
            font-weight: bold !important;
            color: white !important;
            background-color: #2E8B57 !important;  /* Green button */
            padding: 10px 20px !important;  /* Button padding */
            border-radius: 8px !important;  /* Rounded corners */
            text-decoration: none !important;
            display: inline-flex !important;
            align-items: center !important;
        }
        .stPageLink a:hover {
            background-color: #3CB371 !important;  /* Lighter green on hover */
        }
        .stPageLink a span[role="img"] {
            font-size: 36px !important;  /* Bigger icon */
            margin-left: 8px !important;  /* Space between text and icon */
        }
        /* Center the button */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;  /* Space above button */
            width: 100%;  /* Ensure full width for centering */
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and intro
    st.markdown('<div class="title">巴黎迪斯尼乐园作业</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="warning">注意：此作业是你毕业的关键！</div>',
                unsafe_allow_html=True)
    st.markdown("---")

    # Description and purpose
    st.markdown("""
        <div class="content">
            <h2>作业概述</h2>
            <div class="content">   
        作为一名即将毕业的Final Year学生，你们目前正在选修毕业所需的最后一门选修科目，课程名称为「目的地营销概论- Introduction to Destination Marketing」。为了满足你的毕业要求，通过这门课程至关重要。
    
    你的讲师发布了一项重要的个人作业，该作业占你<span class="grade"> 最终成绩的 50% </span>。这项作业的成功至关重要，<span class="grade">因为失败可能会导致课程失败并随后延迟毕业。</span>
    
    对于这项个人作业，你需要写一篇关于法国目的地的文章，并专注于<span class="grade">巴黎迪士尼乐园 </span>。作业必须全面 <span class="dicussion"> 讨论巴黎迪士尼乐园的历史，包括其设施、游客数量和近期重大的展览。</span>
    
    为了帮助您完成这项作业，您可以使用 <span class="blue">「Z」AI </span>，这是一种先进的人工智能搜索引擎和聊天机器人工具，它利用大型语言模型 (LLM) 来响应用户查询，提供详细而准确的信息。<span class="blue">我们鼓励您利用此工具来完成您的作业。</span>
    
    指引：请复制以下问题以获取巴黎迪士尼乐园的背景信息： <span class="yellow">"讨论巴黎迪士尼乐园的历史，包括其设施、游客数量以及近期重大的展览。"</span>
        </div>
        </br>
            <div class="">As a university student in your final semester, you are currently enrolled in the last free elective course required for your graduation, titled "Introduction to Destination Marketing." To fulfill your graduation requirements, it is crucial that you pass this course.
    
    A major individual assignment has been assigned by your lecturer, which accounts for <span class="grade"> 50% of your final grade. </span> The success of this assignment is paramount, <span class="grade"> as failing it could lead to failing the course and subsequently delaying your graduation. </span>
    
    For this critical task, you are required to write an essay about a destination in France, focusing on <span class="grade"> Disneyland Paris </span>. The essay must comprehensively <span class="dicussion"> discuss the history of Disneyland Paris, including its facilities, visitor numbers, and notable recent events. </span>

    To assist you in completing this assignment, you have access to <span class="blue"> "Z" AI </span>, an advanced artificial intelligence-powered search engine and chatbot tool that utilizes large language models (LLMs) to provide detailed and accurate information in response to user queries. <span class="blue"> You are encouraged to leverage this tool to complete your assignment.</span>

    </div>
    <div>
    Instruction: Please copy the following question to receive background information: <span class="yellow"> "Discuss the history of Disneyland Paris, including its facilities, visitor numbers, and notable recent events."</span>
    </div>
        </div>

        """, unsafe_allow_html=True)

    with st.container():

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:

            pass
        with col2:
            pass
        with col4:
            pass
        with col5:
            pass
        with col3:
            st.markdown('<div class="button-container">',
                        unsafe_allow_html=True)
            st.page_link("pages/scenario6.py",
                         label="开始作业", icon="🚀")
            st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
