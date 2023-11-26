#!/usr/bin/env python3
from brain_games.games.game_prime import game_prime
from brain_games.engine import welcome_user, engine


def main():
    welcome_user()
    engine(game_prime)


if __name__ == '__main__':
    main()
