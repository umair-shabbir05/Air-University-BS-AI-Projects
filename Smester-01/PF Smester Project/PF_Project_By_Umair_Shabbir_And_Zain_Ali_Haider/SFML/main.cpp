/*
    TETRIS GAME
    PF THEORY AND LAB PROJECT

    INSTRUCTORS : MAM HINA RASHID AND SIR ADIL SHERAZ
    MADE BY : UMAIR SHABBIR 2502027
    and Zai Ali Haider 2502035

*/

#define _CRT_SECURE_NO_WARNINGS

//  SFML LIBRARIES 
#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>

//  STANDARD LIBRARIES 
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>

// GAME CONSTANTS

// Size of the Tetris grid
const int GRID_COLS = 10;
const int GRID_ROWS = 20;
const int TILE_SIZE = 30;

// Window size calculations
const int SIDE_PANEL_WIDTH = 220;
const int WINDOW_WIDTH = GRID_COLS * TILE_SIZE + SIDE_PANEL_WIDTH + 100;
const int WINDOW_HEIGHT = GRID_ROWS * TILE_SIZE;

// Falling speed settings
int baseDropIntervalMs = 700;
const int LEVEL_DROP_DECREMENT = 60;
const int MIN_DROP_INTERVAL = 100;

// Scoring system
const int SCORE_LINE_1 = 10;
const int SCORE_LINE_2 = 30;
const int SCORE_LINE_3 = 60;
const int SCORE_LINE_4 = 100;

// High score file handling
const char HIGH_SCORES_FILE[] = "highscores.txt";
const int HIGH_SCORES_COUNT = 10;

// On-screen button sizes
const int BUTTON_SIZE = 44;
const int BUTTON_PADDING = 10;

// Font path
const char FONT_PATH[] = "assets/OpenSans-Regular.ttf";

//  SCREEN STATES 

// Used to control which screen is shown
enum ScreenState {
    SCREEN_WELCOME,
    SCREEN_MENU,
    SCREEN_INSTRUCTIONS,
    SCREEN_GAME,
    SCREEN_HIGHSCORES,
    SCREEN_PAUSE
};

ScreenState state = SCREEN_WELCOME;

//  GAME VARIABLES 

// Main grid storing locked blocks
int grid[GRID_ROWS][GRID_COLS];

// Colors for each block type
sf::Color blockColors[8];

// Current falling piece data
int currentType = 0;
int currentRotation = 0;
int currentRow = 0;
int currentCol = 3;

// Next piece preview
int nextType = 0;

// Score and level data
int score = 0;
int linesCleared = 0;
int levelNum = 1;

// Timer for automatic piece dropping
sf::Clock dropClock;
int dropIntervalMs = baseDropIntervalMs;

// Flags
int gameOverFlag = 0;
int pausedFlag = 0;

// High score storage
int highscores[HIGH_SCORES_COUNT];

// Font used in the game
sf::Font gameFont;

// Mouse state tracking
int mouseWasDown = 0;

//  TETRIS PIECES 
// Each piece has 4 rotations, each rotation is 4x4
int pieces[7][4][16] = {
    /* (UNCHANGED DATA – ONLY SHAPES) */
    {
        {0,0,0,0, 1,1,1,1, 0,0,0,0, 0,0,0,0},
        {0,0,1,0, 0,0,1,0, 0,0,1,0, 0,0,1,0},
        {0,0,0,0, 1,1,1,1, 0,0,0,0, 0,0,0,0},
        {0,0,1,0, 0,0,1,0, 0,0,1,0, 0,0,1,0}
    },
    {
        {0,0,0,0, 0,1,1,0, 0,1,1,0, 0,0,0,0},
        {0,0,0,0, 0,1,1,0, 0,1,1,0, 0,0,0,0},
        {0,0,0,0, 0,1,1,0, 0,1,1,0, 0,0,0,0},
        {0,0,0,0, 0,1,1,0, 0,1,1,0, 0,0,0,0}
    },
    {
        {0,0,0,0, 1,1,1,0, 0,1,0,0, 0,0,0,0},
        {0,0,1,0, 0,1,1,0, 0,0,1,0, 0,0,0,0},
        {0,0,0,0, 0,1,0,0, 1,1,1,0, 0,0,0,0},
        {0,1,0,0, 0,1,1,0, 0,1,0,0, 0,0,0,0}
    },
    {
        {0,0,0,0, 1,1,1,0, 0,0,1,0, 0,0,0,0},
        {0,0,1,0, 0,0,1,0, 0,1,1,0, 0,0,0,0},
        {0,0,0,0, 1,0,0,0, 1,1,1,0, 0,0,0,0},
        {0,1,1,0, 0,1,0,0, 0,1,0,0, 0,0,0,0}
    },
    {
        {0,0,0,0, 1,1,1,0, 1,0,0,0, 0,0,0,0},
        {0,1,1,0, 0,0,1,0, 0,0,1,0, 0,0,0,0},
        {0,0,0,0, 0,0,1,0, 1,1,1,0, 0,0,0,0},
        {0,1,0,0, 0,1,0,0, 0,1,1,0, 0,0,0,0}
    },
    {
        {0,0,0,0, 0,1,1,0, 1,1,0,0, 0,0,0,0},
        {0,1,0,0, 0,1,1,0, 0,0,1,0, 0,0,0,0},
        {0,0,0,0, 0,1,1,0, 1,1,0,0, 0,0,0,0},
        {0,1,0,0, 0,1,1,0, 0,0,1,0, 0,0,0,0}
    },
    {
        {0,0,0,0, 1,1,0,0, 0,1,1,0, 0,0,0,0},
        {0,0,1,0, 0,1,1,0, 0,1,0,0, 0,0,0,0},
        {0,0,0,0, 1,1,0,0, 0,1,1,0, 0,0,0,0},
        {0,0,1,0, 0,1,1,0, 0,1,0,0, 0,0,0,0}
    }
};


// Clears the entire game grid (used when starting new game)
void clearGrid() {
    for (int r = 0; r < GRID_ROWS; ++r)
        for (int c = 0; c < GRID_COLS; ++c)
            grid[r][c] = 0;
}

// Checks if given row and column are inside grid bounds
int insideGrid(int r, int c) {
    return (r >= 0 && r < GRID_ROWS && c >= 0 && c < GRID_COLS);
}

// Checks collision of a piece with walls or existing blocks
int checkCollision(int pType, int rotation, int testRow, int testCol) {
    int* shape = (int*)pieces[pType][rotation];
    for (int pr = 0; pr < 4; ++pr) {
        for (int pc = 0; pc < 4; ++pc) {
            if (!shape[pr * 4 + pc]) continue;
            int gr = testRow + pr;
            int gc = testCol + pc;
            if (!insideGrid(gr, gc)) return 1;
            if (grid[gr][gc] != 0) return 1;
        }
    }
    return 0;
}

// Locks the current falling piece into the grid permanently
void lockPiece() {
    int* shape = (int*)pieces[currentType][currentRotation];
    for (int pr = 0; pr < 4; ++pr)
        for (int pc = 0; pc < 4; ++pc)
            if (shape[pr * 4 + pc])
                grid[currentRow + pr][currentCol + pc] = currentType + 1;
}

// Clears complete horizontal lines and shifts grid down
int clearFullLines() {
    int lines = 0;
    for (int r = GRID_ROWS - 1; r >= 0; --r) {
        int full = 1;
        for (int c = 0; c < GRID_COLS; ++c)
            if (grid[r][c] == 0) full = 0;

        if (full) {
            for (int rr = r; rr > 0; --rr)
                for (int cc = 0; cc < GRID_COLS; ++cc)
                    grid[rr][cc] = grid[rr - 1][cc];
            for (int cc = 0; cc < GRID_COLS; ++cc) grid[0][cc] = 0;
            lines++;
            r++;
        }
    }
    return lines;
}
