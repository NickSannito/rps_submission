# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

Run the game with a custom user name: 

```sh
PLAYER_NAME="Anything you want your name to be between the quotes!" python game.py
```

General Gameplay: 
Once you've started the game, simply follow the instructions, typing either 'rock', 'paper', or 'scissors' to play against a randomly generated choice from the computer. Capitalization should not matter when you type your play!

## Testing

Run tests:

```sh
pytest
```
