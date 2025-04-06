# asteroids-pygame

An Asteroids clone made with Pygame.

Uses Python 3.12, not guaranteed to work with previous versions.

This is the second Python project in [Boot.dev](https://www.boot.dev/)'s curriculum.

You can see my additions to the course's main requirements and some other ideas in [TODO.md](./TODO.md)

## Setup

#### Linux, WSL, Mac
```sh
cd asteroids-pygame
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Windows
Like above, but instead of the `source` command run `venv\Scripts\Activate.ps1` in a PowerShell terminal.

## Run

```sh
python3 main.py
```

## How to play
- `W`, `A`, `D` or arrow keys = move and steer the spaceship
- `space` = shoot
- `Esc` or `P` = pause
- `F1` = debug mode (show colliders)

Game ends when the spaceship collides with an asteroid.
