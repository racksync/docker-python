from flask import Flask, jsonify

import random

app = Flask(__name__)

quotes = {
    "Albert Einstein": "The important thing is not to stop questioning. Curiosity has its own reason for existing.",
    "Maya Angelou": "Still I rise.",
    "Nelson Mandela": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "APJ Abdul Kalam": "You have to dream before your dream can come true.",
    "Marie Curie": "One never notices what has been done; one can only see what remains to be done.",
    "Mark Twain": "The secret of getting ahead is getting started.",
    "Oscar Wilde": "Be yourself; everyone else is already taken.",
    "Mahatma Gandhi": "Be the change that you wish to see in the world.",
    "Friedrich Nietzsche": "That which does not kill us makes us stronger.",
    "Vincent Van Gogh": "I dream my painting and I paint my dream.",
    "Charles Darwin": "It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change.",
    "Stephen Hawking": "Intelligence is the ability to adapt to change.",
    "Elon Musk": "When something is important enough, you do it even if the odds are not in your favor.",
    "Steve Jobs": "Innovation distinguishes between a leader and a follower.",
    "Walt Disney": "The way to get started is to quit talking and begin doing."
}

def get_random_quote():
  """
  Selects a random quote and author from the dictionary.

  Returns:
    A tuple containing a string quote and a string author.
  """
  author, quote = random.choice(list(quotes.items()))
  return quote, author

@app.route('/quote', methods=['GET'])
def quote():
  """
  Returns a random quote and author as a JSON response.
  """
  quote, author = get_random_quote()
  return jsonify({'quote': quote, 'author': author})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
