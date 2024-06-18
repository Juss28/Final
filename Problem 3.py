import time

def get_sample_text():
    return "The quick brown fox jumps over the lazy dog."

def calculate_accuracy(original, typed):
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    return correct_chars / len(original) * 100

def typing_master():
    sample_text = get_sample_text()
    print("Type the following text:")
    print(sample_text)
    input("Press Enter when you are ready to start...")

    start_time = time.time()
    typed_text = input()
    end_time = time.time()

    time_taken = end_time - start_time
    accuracy = calculate_accuracy(sample_text, typed_text)

    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_master()

