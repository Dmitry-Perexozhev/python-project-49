#!/usr/bin/env python3
from brain_games.games.game_even import game_even
from brain_games.engine import welcome_user, engine


def main():
    welcome_user()
    engine(game_even)


if __name__ == '__main__':
    main()
