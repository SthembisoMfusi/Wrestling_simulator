# Wrestling Simulation Project

## Overview

This project is a text-based wrestling simulation game built in Python. It allows you to create a roster of wrestlers, either manually or automatically generated, and then pit them against each other in a single-elimination tournament to determine the ultimate champion.

## Features

*   **Customizable Wrestlers:**
    *   Create wrestlers with unique names, genders, and a variety of stats:
        *   Strength: Determines resistance to damage.
        *   Speed: Influences attack and reaction speed.
        *   Agility: Affects the ability to escape grapples and pins.
        *   Health: The amount of damage a wrestler can take.
        *   Power: Determines the damage dealt by attacks.
        *   Grapple: Influences the success rate of grapple moves.
        *   Stamina: Affects how often a wrestler can use special moves.
    *   Manually input stats for each wrestler or use the auto-creation feature to generate wrestlers with random stats.
    *   Choose from a list of male, female, or other names for auto-created wrestlers.
*   **Roster Management:**
    *   Create, load, and save rosters of wrestlers.
    *   Remove wrestlers from the roster by name or index.
    *   Retrieve wrestlers from the roster by name or index.
    *   Save rosters to files using Python's `pickle` module for later use.
*   **Tournament Simulation:**
    *   Set up single-elimination tournaments with a customizable number of participants (must be a power of 2 and at least 4).
    *   Randomly pairs wrestlers in each round.
    *   Simulates matches between wrestlers, with wrestlers using a variety of moves:
        *   Basic attacks.
        *   Grapple attempts.
        *   Pin attempts (success rate based on opponent's health).
    *   Tracks wrestler health and stamina during matches.
    *   Wrestlers regenerate health and stamina between turns.
    *   Determines the winner of each match and advances them to the next round.
    *   Declares the ultimate tournament champion.
*   **Text-Based Interface:**
    *   Provides a simple, text-based user interface for interacting with the simulation.
    *   Displays match commentary, including actions taken, health/stamina changes, and the match winner.

## Files

*   **`wrestler.py`:** Contains the `Wrestler` class, which represents a single wrestler with their attributes and actions (attacking, grappling, pinning, etc.).
*   **`createRoster.py`:** Contains the `Roster` class, which manages a collection of `Wrestler` objects. It handles creating, removing, retrieving, saving, and loading wrestlers.
*   **`Tournament.py`:** Contains the `Tournament` class, which handles the logic for creating and running tournaments, including pairing wrestlers, simulating matches, and determining the winner.
*   **`main.py`:** (or a similarly named file) The main script that ties everything together. It provides the user interface for creating/loading rosters, setting up tournaments, and running the simulation.
*   **`wrestler_names/`:** A directory that contains text files with lists of male, female, and other wrestler names used for auto-creation.

## How to Run

1. **Prerequisites:** Make sure you have Python 3 installed on your system.
2. **Clone the Repository:**
    ```bash
    git clone <https://github.com/SthembisoMfusi/Wrestling_simulator/>
    ```
3. **Navigate to the Project Directory:**
    ```bash
    cd <Wrestling_simulator>
    ```
4. **Run the Main Script:**
    ```bash
    python main.py
    ```
5. **Follow the Prompts:** The script will guide you through the following steps:
    *   Choose whether to create a new roster or load an existing one from a file.
    *   If creating a new roster:
        *   Specify the number of wrestlers.
        *   Choose between manual, automatic, or a combination of both creation methods.
        *   Provide details for each wrestler (if creating manually).
        *   Optionally, save the newly created roster to a file.
    *   If loading a roster:
        *   Enter the file path of the saved roster.
    *   Specify the number of participants for the tournament (must be a power of 2, at least 4, and not exceed the roster size).
    *   The tournament simulation will then run, and the results will be displayed in the console.

## Future Enhancements

*   **More Complex Move System:** Add a wider variety of moves, including special moves unique to each wrestler.
*   **Tag Team Matches:** Implement the ability to have tag team matches.
*   **Different Match Types:** Introduce different match types, such as ladder matches, cage matches, etc.
*   **Career Mode:** Create a career mode where you manage a wrestler's career over multiple tournaments and potentially years.
*   **GUI:** Develop a graphical user interface (GUI) to make the simulation more visually appealing and interactive.
*   **Improved AI:** Enhance the AI of the wrestlers to make them more strategic in their decision-making during matches.
*   **Statistics Tracking:** Track more detailed statistics about wrestlers and tournaments, such as win/loss records, average match length, etc.

