import random
print()
print("🎮 WELCOME TO [KUNAL] GUN 🔫 WATER 💧 SNAKE 🐍 GAME 🎮")
print()
print("Rules:")
print("🔫 Gun beats 🐍 Snake")
print("💧 Water beats 🔫 Gun")
print("🐍 Snake beats 💧 Water")
print("-" * 40)

yourdict = {"g": 1, "w": 2, "s": 3}
maindict = {
    1: "Gun 🔫",
    2: "Water 💧",
    3: "Snake 🐍"
}

user_score = 0
computer_score = 0
round_no = 1

while True:
    print(f"\n🔁 Round {round_no}")
    print("Choose: g (Gun 🔫), w (Water 💧), s (Snake 🐍)")
    print("Press q to Quit ❌")

    yourstr = input("👉 Enter your choice: ").lower()

    if yourstr == "q":
        print("\n🏁 GAME OVER")
        print(f"🙋 Your Score: {user_score}")
        print(f"🤖 Computer Score: {computer_score}")

        if user_score > computer_score:
            print("🎉 YOU WON THE GAME! 🏆")
        elif user_score < computer_score:
            print("😢 YOU LOST THE GAME!")
        else:
            print("🤝 MATCH DRAW!")

        print("Thanks for playing 😊")
        break

    if yourstr not in yourdict:
        print("⚠️ Invalid input! Please choose g, w, or s.")
        continue

    computer = random.choice([1, 2, 3])
    you = yourdict[yourstr]

    print(f"\n🙋 Your choice: {maindict[you]}")
    print(f"🤖 Computer choice: {maindict[computer]}")

    if computer == you:
        print("🤝 It's a DRAW!")
    
    elif (
        (computer == 1 and you == 2) or
        (computer == 2 and you == 3) or
        (computer == 3 and you == 1)
    ):
        print("🎉 YOU WIN THIS ROUND!")
        user_score += 1
    
    else:
        print("💀 YOU LOSE THIS ROUND!")
        computer_score += 1

    print(f"📊 Score → You: {user_score} | Computer: {computer_score}")
    print("-" * 40)

    round_no += 1
