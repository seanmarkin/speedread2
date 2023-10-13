import streamlit as st
import time

def display_word(word):
    # Split the word to highlight the middle character
    stop = len(word) // 2
    left = word[:stop]
    mid = word[stop]
    right = word[stop+1:]

    # Return the word with the middle character highlighted in red using HTML
    return f"{left}<span style='color:red'>{mid}</span>{right}"

def main():
    st.title("Speed Reading App")

    # Input for WPM with error handling
    try:
        wpm = st.number_input("Words Per Minute (WPM)", min_value=50, value=300, step=50)
        interval = 60.0 / wpm
    except ValueError:
        st.error("Please enter a valid number for WPM!")
        return

    # Textarea for text input
    text = st.text_area("Paste your text here:", height=10)

    # Error handling for empty text
    if not text.strip():
        st.warning("Please provide some text to read!")
        return

    words = text.split()

    # Start, Pause, Resume buttons
    if st.button("Start Reading"):
        for word in words:
            # Display word with middle character highlighted
            st.markdown(display_word(word), unsafe_allow_html=True)
            time.sleep(interval)

    # Note: Streamlit currently doesn't support "Pause" and "Resume" natively in the same way a typical GUI or web app would.
    # This is a basic implementation and the reading will start over when pressing "Start Reading" again.

if __name__ == "__main__":
    main()
