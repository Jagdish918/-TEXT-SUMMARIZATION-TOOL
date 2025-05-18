import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

def main():
    st.title("📝 NLP Text Summarizer")

    summarizer = load_summarizer()

    input_text = st.text_area("Enter your text (large paragraphs supported):", height=300)

    max_length = st.number_input("Max summary length:", min_value=10, max_value=200, value=100)
    min_length = st.number_input("Min summary length:", min_value=5, max_value=100, value=30)

    if st.button("Generate Summary"):
        if input_text.strip() == "":
            st.warning("Please enter some text to summarize.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
                st.subheader("Summary:")
                st.write(summary[0]['summary_text'])

if __name__ == "__main__":
    main()
