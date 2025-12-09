import streamlit as st
from src.chatbot import FAQChatbot

@st.cache_resource
def load_bot() -> FAQChatbot:
    return FAQChatbot(min_similarity=0.3)

def main():
    st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")
    st.title("🤖 FAQ Chatbot")
    st.markdown("ask me anything about our services!")

    bot = load_bot()

    st.sidebar.header("Topics")
    categories = bot.get_categories()
    if categories:
        st.sidebar.markdown("\n".join([f"- {c}" for c in categories]))
    
    st.sidebar.markdown("---")  
    st.sidebar.header("Try asking:")
    suggestions = bot.get_random_questions(3)
    for q in suggestions:
        if st.sidebar.button(q):
            pass
    
    user_question = st.text_input("Ask a question:")

    if user_question:
        answer, matched_q, score = bot.get_answer(user_question)

        if matched_q:
            st.success(f"**Answer:** {answer}")
            with st.expander("Confidence Details"):
                st.caption(f"Matched FAQ: “{matched_q}”")
                st.caption(f"Similarity Score: {score:.2f}")
        else:
            st.warning(f"**Bot:** {answer}")
            st.caption(f"(No strong match found, similarity: {score:.2f})")


if __name__ == "__main__":
    main()