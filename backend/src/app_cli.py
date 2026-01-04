from .chatbot import FAQChatbot

def main() -> None:
    print("=== Knowledge Assistant ===")
    print("Loading knowledge base...")
    bot = FAQChatbot(min_similarity=0.3)
    
    print("\n--- Topics ---")
    print(", ".join(bot.get_categories()))
    
    print("\n--- Try asking ---")
    for q in bot.get_random_questions(3):
        print(f"- {q}")

    print("\nReady! Type your question below, or 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break

        answer, matched_q, score = bot.get_answer(user_input)

        print(f"\nBot: {answer}")
        print(f"[Matched: \"{matched_q}\" (score={score:.3f})]\n")


if __name__ == "__main__":
    main()