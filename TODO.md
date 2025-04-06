# Ideas

Some ideas to expand the project beyond the basics and make it a bit more insteresting, or at the very least a good learning experience.


## My ideas

Reference:
- https://www.echalk.co.uk/amusements/Games/asteroidsClassic/ateroids.html
- https://youtu.be/BgloG8yt-jA

- [x] Score
    - [ ] Better font, similar to original game
    - [ ] Don't use a font, create a class that writes lines
- [x] Pause
    - [x] Text "paused" at the center
    - [x] Semiopaque overlay
- [x] Ship should not move backwards
- [x] Better looking asteroids (procedural polygons)
    - [ ] Use Simplex noise for more organic shapes
    - [ ] Random rotation while moving
- [x] Debug mode (show colliders)
    - I used this to visualize the player's hitbox (hitcircle actually)
- [ ] Better looking player
    - [ ] Exhaust animation
- [ ] Shots progressive fading towards end of lifetime (also useful for particle effects)
- [x] Inertia
    - [x] Player movement
    - [ ] Player rotation
- [ ] Splash screen with highscore
- [ ] Game over screen and restart
    - "You lost"
- [ ] High scores list
    - Session
    - Persistent storage, Write CSV with top 5 scores and respoective date
- [ ] Sounds
- [ ] Demo GIF/video in README
- [ ] Point collision instead of circle for bullets? Or configurable
- [ ] Put minimum required python version in README
- [ ] Use object pools to reutilize destroyed asteroids/bullets
- [ ] WASM export to make it playable in the browser
- [ ] Multiplayer
    - [ ] Hotseat
    - [ ] Network


## Boot.dev suggested features

- [x] Add a scoring system
- [ ] Implement multiple lives and respawning
- [ ] Add an explosion effect for the asteroids
- [x] Add acceleration to the player movement
- [ ] Make the objects wrap around the screen instead of disappearing
- [ ] Add a background image
    - Maybe some tiny flickering stars as points?
- [ ] Create different weapon types
- [x] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped

"Have fun with it, and make sure to share any improvements you make with us in the Discord community!"
