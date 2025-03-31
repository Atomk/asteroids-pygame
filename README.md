# asteroids-pygame

An Asteroids clone made with Pygame.

Second Python project in the [Boot.dev](https://www.boot.dev/) curriculum.

## Setup

#### Linux, WSL, Mac
```sh
cd asteroids-pygame
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Windows (Powershell)
Like above, but instead of the `source` command run `venv\Scripts\Activate.ps1`.

## Run

```sh
python3 main.py
```

## How to play
- `W`, `A`, `S`, `D` = move and steer the spaceship
- `space` = shoot

Game ends when the spaceship collides with an asteroid.
