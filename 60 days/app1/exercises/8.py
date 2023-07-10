# Throw the coin and enter head or tail here: ? tail
# Heads: 0.0%
# Throw the coin and enter head or tail here: ? head
# Heads: 50.0%
# Throw the coin and enter head or tail here: ? head
# Heads: 66.666666666666%
# Throw the coin and enter head or tail here: ? tail
# Heads: 50.0%


import random

def flip_coin():
    return random.choice(["head", "tail"])

def calculate_percentage(count, total):
    return (count / total) * 100

def main():
    total_flips = 0
    head_count = 0

    with open("coin_flips.txt", "w") as file:
        while True:
            user_input = input("# Throw the coin and enter 'head' or 'tail' here: ")

            if user_input.lower() == "q":
                break

            if user_input.lower() == "head" or user_input.lower() == "tail":
                total_flips += 1
                coin_result = flip_coin()

                if user_input.lower() == coin_result:
                    head_count += 1

                percentage = calculate_percentage(head_count, total_flips)
                print(f"# Heads: {percentage:.2f}%")

                file.write(user_input.lower() + "\n")

            else:
                print("Invalid input. Please enter 'head' or 'tail'.")

    print("Exiting the program.")

if __name__ == "__main__":
    main()
