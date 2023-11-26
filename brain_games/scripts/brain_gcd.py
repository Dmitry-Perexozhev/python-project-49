#!/usr/bin/env python3
from brain_games.games.game_gcd import game_gcd
from brain_games.engine import welcome_user, engine


def main():
    welcome_user()
    engine(game_gcd)


if __name__ == '__main__':
    main()
