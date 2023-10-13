import streamlit as st
import time

def display_word(word):
    stop = len(word) // 2
    left = word[:stop]
    mid = word[stop]
    right = word[stop+1:]
    return f"{left}<span style='color:red'>{mid}</span>{right}"

def main():
    st.title("Speed Reading App")

    wpm = st.number_input("Words Per Minute (WPM)", min_value=50, value=300, step=50)
    interval = 60.0 / wpm

    text = st.text_area("Paste your text here:", height=10)

    if 'words' not in st.session_state:
        st.session_state.words = text.split()
        st.session_state.current_word_index = 0

    if st.button("Start Reading"):
        st.session_state.words = text.split()
        st.session_state.current_word_index = 0
        st.session_state.start_time = time.time()

    if 'start_time' in st.session_state:
        elapsed_time = time.time() - st.session_state.start_time
        word_count_to_display = int(elapsed_time // interval)

        if word_count_to_display <= len(st.session_state.words):
            word_to_display = st.session_state.words[word_count_to_display]
            st.markdown(display_word(word_to_display), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
