#!/usr/bin/env python3
from brain_games.games.game_progression import game_progression
from brain_games.engine import welcome_user, engine


def main():
    welcome_user()
    engine(game_progression)


if __name__ == '__main__':
    main()
