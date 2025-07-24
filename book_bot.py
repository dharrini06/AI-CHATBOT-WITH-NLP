import re

# Mock book database by genre
book_db = {
    "thriller": ["Gone Girl by Gillian Flynn", "The Girl with the Dragon Tattoo by Stieg Larsson"],
    "romance": ["Pride and Prejudice by Jane Austen", "Me Before You by Jojo Moyes"],
    "science fiction": ["Dune by Frank Herbert", "Ender's Game by Orson Scott Card"],
    "fantasy": ["Harry Potter by J.K. Rowling", "The Hobbit by J.R.R. Tolkien"],
    "self-help": ["Atomic Habits by James Clear", "The Power of Now by Eckhart Tolle"],
    "biography": ["Steve Jobs by Walter Isaacson", "Becoming by Michelle Obama"],
    "mystery": ["The Da Vinci Code by Dan Brown", "Big Little Lies by Liane Moriarty"],
    "historical": ["The Book Thief by Markus Zusak", "All the Light We Cannot See by Anthony Doerr"]
}

# Function to recommend books based on genre
def recommend_books(user_input):
    user_input = user_input.lower()
    for genre in book_db:
        if re.search(genre, user_input):
            return f"📚 Recommended {genre.title()} Books:\n- " + "\n- ".join(book_db[genre])
    return "❌ Sorry, I couldn't find a book for that genre. Try asking about thriller, romance, fantasy, etc."

# Chatbot loop
def book_recommendation_bot():
    print("📘 Welcome to the Book Recommendation Bot!")
    print("Ask me to recommend books by genre (e.g., 'Suggest me a thriller novel'). Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Happy reading! 📖")
            break
        response = recommend_books(user_input)
        print("Bot:", response)

# Run the chatbot
book_recommendation_bot()
