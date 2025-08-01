# 🏎️ The Final Race – Verstappen Max vs Mostafa Hassan

A turn-based Formula 1 race simulator written in Python using **Object-Oriented Programming (OOP)** principles. In this high-octane duel, Max Verstappen faces off against Hassan Mostafa in a battle of strategy, tire wear, and fuel management.

---

## 🚀 Features

- **OOP Principles**: Full use of abstraction, inheritance, encapsulation, and polymorphism.
- **Turn-Based Mechanics**: Each round includes a move and a response (defense or counter-attack).
- **Tire & Fuel Management**: Moves cost fuel, and attacks reduce tire health.
- **Move Limits**: Some tactics have limited uses.
- **Interactive Console UI**: Players select their actions in real time.

---

## 🧱 Project Structure

```

final\_race/
├── main.py          # Main game logic and turn manager
├── driver.py        # Driver class with move, fuel, tire handling
├── moves.py         # All move and tactic classes (offensive & defensive)
└── README.md        # Project documentation

````

---

## 🎮 How to Play

### Requirements
- Python 3.6 or above

### Run the Game

```bash
python main.py
````

### Gameplay Mechanics

* The race alternates between **Max Verstappen** and **Hassan Mostafa**.
* Each turn:

  1. One driver selects an **offensive move**.
  2. The opponent receives damage.
  3. The opponent can **defend** or **counter-attack**.
  4. Tire health and fuel stats are updated.
* The race ends when a driver’s **tire health drops to 0 or below**.

---

## 🛠️ Code Principles

* **Encapsulation**: Private attributes and controlled access.
* **Inheritance**: Specialized move classes inherit from a base `Move` class.
* **Polymorphism**: Overridden methods and `__call__` functionality.
* **Abstraction**: Logical separation between move behavior and game flow.

---

## 🧠 Future Enhancements

- 🗣️ **Voice-Control Integration**: Use Speech-to-Text (STT) via the **Groq API** to allow players to control their drivers using real speech instead of keyboard inputs — making gameplay hands-free and immersive.
- Add AI-controlled opponents or randomness.
- Integrate GUI (Tkinter or Pygame).
- Add more moves, track types, and driver stats.

---
