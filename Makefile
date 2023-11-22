
brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	poetry install

lint:
	poetry run flake8 brain_games