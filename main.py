from dotenv import load_dotenv
import os

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    
    print(api_key)


if __name__ == "__main__":
    main()
