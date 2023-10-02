# thank you for downloading and looking at the code!
#i worked very hard on this so enjoy!

import random
import datetime
import webbrowser
import os


def load_game_data():
    try:
        with open("GAMEDATA.txt", "r") as file:
            data = file.read().split('\n')
            wins = int(data[0])
            last_play_time = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
            used_winning_numbers = [int(num) for num in data[2].split(",") if num]
            return wins, last_play_time, used_winning_numbers
    except FileNotFoundError:
        return 0, datetime.datetime.min, []

def save_game_data(wins, last_play_time, used_winning_numbers):
    with open("GAMEDATA.txt", "w") as file:
        file.write(f"{wins}\n{last_play_time.strftime('%Y-%m-%d %H:%M:%S')}\n{','.join(map(str, used_winning_numbers))}")
    

def pick_lottery_numbers(num_picks):
    return sorted([int(input(f"Enter pick {i+1} (1-48): ")) for i in range(num_picks) if 1 <= int(input(f"Enter pick {i+1} (1-48): ")) <= 48])

def pick_winning_numbers(num_picks, used_winning_numbers):
    available_numbers = [num for num in range(1, 50) if num not in used_winning_numbers]
    winning_numbers = random.sample(available_numbers, num_picks)
    return sorted(winning_numbers)

def check_winning(lottery_numbers, winning_numbers):
    matching_numbers = set(lottery_numbers) & set(winning_numbers)
    return matching_numbers

def open_browser_if_no_win():
    url = "https://www.youtube.com/watch?v=48rz8udZBmQ"
    webbrowser.open(url)

def open_browser_if_one_two_three():
    url = "https://youtu.be/SBCw4_XgouA?t=4"
    webbrowser.open(url)

def open_browser_if_four_or_five():
    url = "https://www.youtube.com/watch?v=yuzCcwD2qYI"
    webbrowser.open(url)

def main():
    num_picks = 6

    # Create GAMEDATA.txt if it doesn't exist
    if not os.path.exists("GAMEDATA.txt"):
        with open("GAMEDATA.txt", "wb") as file:
            file.write(b"0\n2000-01-01 00:00:00\n")

    wins, last_play_time, used_winning_numbers = load_game_data()

    current_time = datetime.datetime.now()
    time_difference = current_time - last_play_time

    if time_difference.days < 1:
        print("You have already played today. Try again tomorrow.")
        return

    print("Welcome to the Lottery Number Picker!")
    print(f"You've picked {num_picks} numbers from 1 to 49.")

    lottery_numbers = pick_lottery_numbers(num_picks)
    print(f"Your lottery numbers are: {lottery_numbers}")

    winning_numbers = pick_winning_numbers(num_picks, used_winning_numbers)
    used_winning_numbers.extend(winning_numbers)  # Add new winning numbers to used list
    print(f"The winning numbers are: {winning_numbers}")

    matching_numbers = check_winning(lottery_numbers, winning_numbers)

    if len(matching_numbers) == 0:
        print(f"Unfortunately, you didn't match any numbers.")
        open_browser_if_no_win()
    elif len(matching_numbers) in (1, 2, 3):
        print(f"Congratulations! You've matched {len(matching_numbers)} numbers.")
        open_browser_if_one_two_three()
    elif len(matching_numbers) in (4, 5):
        print(f"Congratulations! You've matched {len(matching_numbers)} numbers.")
        open_browser_if_four_or_five()

        # Increase win count and save it to GAMEDATA.txt
        wins += 1

    save_game_data(wins, current_time, used_winning_numbers)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
