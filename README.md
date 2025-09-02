# 🐢 Turtle-Dash  

A retro-style crossing game built with Python’s **turtle** module.  
Guide your turtle safely across multiple lanes of traffic while avoiding cars, obstacles, and collecting points.  
Inspired by 1990’s arcade classics but written in pure Python 🐍.  

---

## 🎮 Features  
- 🚗 **Multiple Lanes of Traffic** – Cars move in both directions with randomized speeds (trucks & sports cars).  
- 💖 **Lives System** – You get 3 lives before Game Over.  
- 🪨 **Obstacles** – Random rocks/logs appear each level (max 7 active at once).  
- ⚡ **Level Progression** – Car spawn rate & difficulty increase as you level up.  
- ⬆️ **Sideways Movement** – Move in all 4 directions for dodging.  
- 🏆 **Score Tracking** – Levels increase your score.  
- 📈 **Difficulty Scaling** – Faster spawns, more chaos with each new level.  

---

## 🎮 Controls  
| Key | Action |
|-----|---------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

---

## 🛠 Installation & Running  
1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/turtle-dash.git
   cd turtle-dash

---

## 🛠 Install dependencies:
pip install -r requirements.txt


---
## 🛠 Run the game:
python main.py

---
## Project Structure

turtle-dash/
│── main.py          # Game loop
│── player.py        # Player (turtle) logic
│── car_manager.py   # Car spawning & movement
│── obstacle_manager.py # Stationary obstacles
│── scoreboard.py    # Score + lives display
│── requirements.txt # Dependencies
│── README.md        # Documentation
