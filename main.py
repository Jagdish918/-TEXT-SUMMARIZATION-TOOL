from transformers import pipeline

def summarize_text(text, max_length=100, min_length=30):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("Please enter the text you want to summarize (paste your article):")
    input_text = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        input_text += line + " "

    if not input_text.strip():
        print("No input provided. Exiting.")
        exit()

    try:
        max_len = int(input("Enter max summary length (default 100): ") or 100)
        min_len = int(input("Enter min summary length (default 30): ") or 30)
    except ValueError:
        print("Invalid input for length. Using defaults 100 max, 30 min.")
        max_len, min_len = 100, 30

    summary = summarize_text(input_text, max_length=max_len, min_length=min_len)

    print("\n--- Summary ---")
    print(summary)
