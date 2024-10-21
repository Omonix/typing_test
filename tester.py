import curses
from curses import wrapper
import random
import time

tab_sentence = [
    "The sun dipped below the horizon, casting long shadows across the landscape, as the evening sky turned bright orange.",
    "The children ran through the park, laughing and chasing each other, their joy echoing through the cool autumn air.",
    "In the heart of the bustling city, an old bookstore stood, offering refuge to those seeking quiet solitude.",
    "The artist sketched quickly, capturing the fleeting expressions on the faces of the people passing by the busy street.",
    "The chef carefully plated the dish, arranging each ingredient with precision, before serving it to the eagerly waiting customers.",
    "Despite the challenges, the team worked together, determined to meet their deadline and deliver a successful final product.",
    "The dog wagged its tail excitedly, jumping up to greet its owner, who had just returned home from work.",
    "In the forest, the leaves rustled softly in the wind, creating a peaceful soundtrack to the hikers' journey.",
    "The young scientist carefully mixed the chemicals in the lab, observing the reactions with great curiosity and anticipation.",
    "At the beach, the waves crashed against the shore, their rhythmic sound calming the tourists who gathered to watch.",
    "The baker rose early every morning to prepare fresh bread, filling the entire neighborhood with the aroma of warmth.",
    "As the rain poured down, the streetlights reflected in puddles, creating a beautiful mosaic of shimmering lights.",
    "The crowd erupted in cheers as the athlete crossed the finish line, setting a new record for the event.",
    "Underneath the starry sky, the couple danced together, their movements slow and graceful, lost in the moment's magic.",
    "The detective examined the crime scene carefully, searching for clues that might help solve the mysterious case at hand.",
    "The writer sat at her desk, staring at the blank page, struggling to find the right words for her story.",
    "In the bustling marketplace, merchants called out to potential buyers, showcasing their goods and haggling over prices enthusiastically.",
    "The cat curled up on the windowsill, basking in the warm sunlight streaming through the glass on a cold day.",
    "The hikers reached the mountain's peak, exhausted but exhilarated, as they gazed out over the expansive valley below.",
    "The teacher patiently explained the complex concept, using examples to ensure that every student understood the lesson clearly.",
    "The actor rehearsed his lines backstage, pacing nervously as he prepared for his big debut in the upcoming play.",
    "The ship sailed across the calm waters, its sails billowing in the wind as the crew prepared for docking.",
    "The scientist analyzed the data carefully, hoping to uncover the solution to the problem that had eluded them for months.",
    "The farmer tended to his crops, carefully watering each row to ensure a bountiful harvest for the upcoming season.",
    "As the plane ascended into the sky, passengers settled into their seats, excited for the journey ahead of them.",
    "The photographer captured the vibrant colors of the sunset, framing the moment perfectly in her lens for future memories.",
    "In the bustling restaurant, waiters moved quickly between tables, balancing trays filled with steaming dishes and taking new orders.",
    "The musician tuned her guitar backstage, preparing to perform for the eager crowd gathered in the intimate concert venue.",
    "At the museum, visitors marveled at the intricate artwork on display, each piece telling a unique story of history.",
    "The gardener knelt beside the flowerbed, carefully planting new seeds, hopeful for the vibrant blooms that would follow soon."
  ]

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    lb_intro(stdscr)
    while True:
        lb_tester(stdscr)
        stdscr.addstr(3, 0, 'Good completed ! Press any key...', curses.color_pair(4))
        key = stdscr.getkey()
        if ord(key) == 10:
            break
def lb_intro(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Welcome to the WPM typing test !', curses.color_pair(2))
    stdscr.addstr(1, 0, 'Press any key to begin...', curses.color_pair(4))
    stdscr.refresh()
    stdscr.getkey()
def lb_tester(stdscr):
    test_text = tab_sentence[random.randint(0, 14)]
    user_text = []
    wpm = 0
    timer = time.time()
    stdscr.nodelay(True)
    
    while True:
        wpm = round(len(user_text) * 60 / (max(time.time() - timer, 1)) / 6)

        stdscr.clear()
        lb_display_handler(stdscr, test_text, user_text, wpm)
        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except:
            continue
        if key not in ('KEY_LEFT', 'KEY_RIGHT', 'KEY_UP', 'KEY_DOWN') and ord(key) == 10 or len(user_text) == len(test_text) - 1:
            stdscr.nodelay(False)
            break
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(user_text) > 0:
                user_text.pop()
        elif key not in ('KEY_LEFT', 'KEY_RIGHT', 'KEY_UP', 'KEY_DOWN'):
            user_text.append(key)
def lb_display_handler(stdscr, test, user, wpm=0):
    stdscr.addstr(test, curses.color_pair(2))
    for i, char in enumerate(user):
        color = curses.color_pair(1)
        if char != test[i]:
            color = curses.color_pair(3)
        stdscr.addstr(0, i, char, color)
        stdscr.addstr(2, 2, f'WPM : {wpm}', curses.color_pair(5))

wrapper(main)