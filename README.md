---

# 🏓 Ping Pong (Pygame)

A simple retro-style **Ping Pong** game built with **Pygame**. It features paddle movement, AI opponent behavior, sound effects, and a game over screen.

## 🎮 Features

- **Classic Paddle Gameplay** : Move the paddle up and down to hit the ball.
- **AI Opponent** : The enemy paddle follows the ball dynamically.
- **Retro Aesthetic** : Includes a pixel-art background, retro colors, and a pause overlay.
- **Sound Effects** : Hits, edge bounces, and game-over sounds.
- **Game Over & Restart** : Displays a *Game Over* screen and allows a quick restart.

## 🛠 Installation

1. Ensure you have Python and Pygame installed:
   ```bash
   pip install pygame
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/XanderSteyn/Ping-Pong.git
   cd Ping-Pong
   ```
3. Run the game:
   ```bash
   python PingPong.py
   ```

## 🎮 Controls

|      Key      |         Action         |
|---------------|------------------------|
| `UP` / `DOWN` | Move player paddle     |
| `P`           | Pause/Resume           |
| `R`           | Restart (on Game Over) |
| `ESC`         | Quit (on Game Over)    |

## 🎨 Game Mechanics

### Ball Movement
- The ball moves in a straight line and bounces off walls.
- When it collides with a paddle, it reverses direction with a slight random angle change.

### AI Behavior
- The AI paddle follows the ball's Y position with slight delay.

### Game Over & Restart
- If the ball passes the left edge, the game ends.
- The player can restart by pressing `R`

## 🔊 Assets & Dependencies

- **Sound Effects** : Located in `SFX/`
- **Sprites** : Background and ball image in `Sprites/`
- **Fonts** : Uses system Arial

---
