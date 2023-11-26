#!/usr/bin/env python3
from brain_games.games.game_calc import game_calc
from brain_games.engine import welcome_user, engine


def main():
    welcome_user()
    engine(game_calc)


if __name__ == '__main__':
    main()
