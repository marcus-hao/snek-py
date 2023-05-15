import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    game_height, game_width = 20, 50
    game_win = curses.newwin(game_height, game_width, 0, 0)
    game_win.keypad(True)
    game_win.border()

    snake_y, snake_x = (game_height // 2), (game_width // 2)
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    food = [random.randint(1, game_height - 2), 
            random.randint(1, game_width - 2)]
    game_win.addch(food[0], food[1], '*')

    score = 0
    direction = curses.KEY_RIGHT

    while True:
        game_win.timeout(100)
        key = game_win.getch()
        new_head = snake[0].copy()
        if key in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
            direction = key
        if direction == curses.KEY_UP:
           new_head[0] -= 1 
        elif direction == curses.KEY_DOWN:
           new_head[0] += 1 
        elif direction == curses.KEY_LEFT:
           new_head[1] -= 1 
        elif direction == curses.KEY_RIGHT:
           new_head[1] += 1 

        snake.insert(0, new_head)
        if (
            snake[0][0] == 0
            or snake[0][0] == game_height - 1
            or snake[0][1] == 0
            or snake[0][1] == game_width - 1
            or snake[0] in snake[1:]
            ):
                break
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                new_food = [random.randint(1, game_height - 2),
                        random.randint(1, game_width - 2)]
                food = new_food if new_food not in snake else None

            game_win.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            game_win.addch(tail[0], tail[1], ' ')

        game_win.addch(snake[0][0], snake[0][1], '#') 
        game_win.addstr(0, game_width // 2 - 3, 'score: {}'.format(score))
    
    stdscr.clear()
    stdscr.addstr(game_height // 2, game_width // 2,
                    'skill issue')
    stdscr.nodelay(0)
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)
