# disney_scenario2.py
import streamlit as st
from config.disney_scenario_template import create_disney_scenario_page
from config.utils import capture_and_modify_state


def main():
    capture_and_modify_state(display=False)
    state = st.session_state.get('state', '')
    
    survey_base = "https://surveys.lifepointspanel.com/survey/apac/ISE4911"  # 自定义调查链接
    survey_href = f"{survey_base}?state={state}"
    
    custom_star_rating = 4.5  # 自定义星级评分值 (0.0-5.0)
    custom_rating_count = 12  # 自定义评分人数 (以K为单位，例如150.5表示150,500人)
    custom_level_confidence = 2

    create_disney_scenario_page(
        scenario_num=6,
        custom_star_rating=custom_star_rating,
        custom_rating_count=custom_rating_count,
        custom_level_confidence=custom_level_confidence,
        survey_href=survey_href  # 替换为实际的调查链接
    )


if __name__ == "__main__":
    main()
