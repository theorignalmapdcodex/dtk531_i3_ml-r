# I. Importing the necessary functions for the Gemini API LLM Interaction to Work
from call_gemini_ai import * 
from my_gemini_api import *

# III. Gemini API integration & Call
def __get_gemini_client__() -> genai.GenerativeModel:
    genai.configure(api_key=the_api_key)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_model

gemini_model = __get_gemini_client__()

# IV. Having a conversation to break the Gemini API; Modified with Gemini AI on 4 Feb 25 @ 1:40pm
while True:
        user_input = input("👨🏾‍💻 Michael D. A-P: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\n" + "❤️ Have a great day! ❤️" + "\n")
            break

        gemini_output = query_gemini_api(user_input, gemini_model, conversation_history)

        print("-" * 14)
        print("♊ Gemini 1.5 Flash:")
        print("-" * 14)
        for line in gemini_output.split("\n"):
            if line.strip():
                print(f"  - {line.strip()}")
        print("-" * 50 + "\n")