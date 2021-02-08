# Rock Paper Scissors Game
An automated user vs. system rock-paper-scissors game.

(Attribution: this README file is based on that provided by Professor Rossetti for the "My First Python App" exercise)

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this remote repository (https://github.com/sondejste/my-first-python-app) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-game
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-first-game":

```sh
conda create -n my-first-game python=3.8
conda activate my-first-game
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="Your Name"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the game script:

```py
python app/game.py
