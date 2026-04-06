# Blue Sky Battlefield

A 2D space shooter arcade game developed in Python using Pygame. Players control a spaceship, destroy enemy waves, and survive as long as possible.

## Play Online

**[Play Blue Sky Battlefield in your browser](https://edlamosonar.github.io/blue-sky-battlefield/)**

## Screenshots

```
+------------------------------------------+
|  Lives x 2                   Score000000 |
|                                          |
|           [BLUE SKY BATTLEFIELD]         |
|                [PRESS START]             |
|                                          |
|  *  .  *    .     *    .    *    .   *   |
|     .     *    .     *    .    *    .    |
|                    /^\                   |
|                   ( ^ )  <- Hero Ship    |
|                    \|/                   |
|                                          |
|      [V]  [V]  [V]  <- Enemies          |
+------------------------------------------+
```

## Controls

| Key | Action |
|-----|--------|
| `W` / `Arrow Up` | Move up |
| `S` / `Arrow Down` | Move down |
| `A` / `Arrow Left` | Move left |
| `D` / `Arrow Right` | Move right |
| `Space` | Fire laser |
| `Enter` | Start / Restart game |
| `Esc` | Return to title screen |

## Gameplay

- **Objective**: Destroy enemy spaceships and survive as long as possible
- **Lives**: You start with 2 lives; each life has 6 health points
- **Score**: +125 points per enemy destroyed
- **Health bar**: Displayed on the left side as colored squares (blue = full, red = critical)
- **Enemies**: Spawn from the top of the screen in different movement patterns
- **Game Over**: Occurs when all lives are exhausted

## Project Structure

```
BlueSkyBattlefield/
├── main/
│   ├── __init__.py              # Game entry point and main loop
│   ├── component/               # Game entities (sprites)
│   │   ├── Nave.py              # Base ship class (animation, movement, collision)
│   │   ├── NaveHeroe.py         # Player ship (input, shooting, health)
│   │   ├── NaveEnemiga.py       # Enemy ship (AI movement patterns)
│   │   ├── Disparo.py           # Base projectile class
│   │   ├── DisparoHeroe.py      # Player laser projectile
│   │   ├── DisparoEnemigo.py    # Enemy projectile (stub)
│   │   ├── SpriteExtended.py    # Base sprite with collision support
│   │   └── ScoreBar.py          # Health bar UI component
│   ├── manager/                 # Game systems
│   │   ├── LevelManager.py      # Game states (title, playing, game over)
│   │   ├── ComponentManager.py  # Entity factory and lifecycle
│   │   ├── ColisionManager.py   # Collision detection (AABB)
│   │   ├── LandScapeManager.py  # Scrolling starfield background
│   │   ├── LevelState.py        # Base level state
│   │   └── SoundManager.py      # Audio initialization
│   ├── level/
│   │   └── Level1.py            # Level 1: enemy spawning and logic
│   └── util/
│       ├── Constants.py         # Movement and routine type enums
│       ├── ImageUtil.py         # Sprite sheet loading and image utilities
│       └── SoundUtil.py         # Sound file loading
├── resources/
│   ├── imx/                     # Image assets (backgrounds, sprites)
│   ├── sounds/                  # Audio files (music, SFX)
│   └── fonts/                   # Font files
├── test/
│   └── __test__.py              # Early prototype (single-file version)
└── requirements.txt
```

## Architecture

The game follows a **Manager pattern** with clear separation of concerns:

```
main/__init__.py  (Game Loop)
        |
        +-- LevelManager      (Game state machine: title → play → game over)
        |       |
        |       +-- Level1    (Level logic: enemy spawning, entity updates)
        |       +-- NaveHeroe (Player entity)
        |
        +-- ComponentManager  (Entity factory + lifecycle management)
        |       |
        |       +-- ColisionManager   (AABB collision detection)
        |       +-- LandScapeManager  (Scrolling background)
        |       +-- SoundManager      (Audio mixer)
        |
        +-- Entities
                +-- NaveHeroe / NaveEnemiga  (Ships)
                +-- DisparoHeroe             (Projectiles)
```

### Key Design Patterns
- **Factory Pattern**: `ComponentManager` creates all game entities
- **Component Pattern**: Sprites implement `colision()` callbacks
- **State Pattern**: `LevelManager` handles game states
- **Sprite Sheets**: All graphics loaded from atlas files (`1945.bmp`, `spaceship_sprites.png`)

## Requirements

- Python 3.7+
- Pygame 2.x

## Installation & Running

```bash
# Clone the repository
git clone https://github.com/EdlamOsonar/blue-sky-battlefield.git
cd blue-sky-battlefield/BlueSkyBattlefield

# Install dependencies
pip install -r requirements.txt

# Run the game
cd main
python __init__.py
```

## Development History

The game was developed incrementally between March–November 2014, with the codebase progressively refactored from a single-file prototype into a modular architecture:

| Milestone | Description |
|-----------|-------------|
| Initial commit | Basic sprite loading and rendering |
| `class Nave` | Base ship class with sprite animation |
| Movement | Player ship keyboard controls |
| Module refactor | Split into component/manager/level packages |
| Shooting | Player laser projectiles |
| Collision detection | AABB hit detection system |
| Background scroll | Parallax starfield scrolling |
| Score system | Points per enemy destroyed |
| Audio | Background music + sound effects |
| Level Manager | Game state machine |
| Enemy movement | Multiple AI movement patterns |
| Game states | Title screen, gameplay, game over |
| Score bar | Visual health indicator |
| New assets | Updated ship and enemy graphics |

## Technical Notes

- **Window**: 640×480 pixels, 30 FPS
- **Language**: Python 3 (originally developed in Python 2, migrated to Python 3)
- **Sprites**: 9-frame animation for player ship (idle + 8 directional states)
- **Collision**: Axis-Aligned Bounding Box (AABB) via `pygame.sprite.collide_rect()`
- **Audio**: OGG/WAV files via `pygame.mixer`
- **Assets**: Sprite atlas technique using `SpriteSheet` class

## Author

Fernando (famalde@gmail.com)  
Original development: 2014
