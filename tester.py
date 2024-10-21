import curses
from curses import wrapper
import random
import time

tab_sentence = ['Le bruit des vagues qui s\'échouent sur le rivage me rappelle à quel point la nature est à la fois puissante et apaisante.', 'Chaque matin est une nouvelle chance de faire un pas vers ses objectifs, même si ce pas semble parfois minuscule ou insignifiant.', 'La beauté d\'un coucher de soleil réside dans sa simplicité et son éphémère, nous rappelant de profiter de chaque instant.', 'Les livres ont ce pouvoir magique de nous transporter vers des mondes inconnus et de nous faire rêver, peu importe où nous nous trouvons.', 'Le silence d\'une forêt au petit matin est un véritable refuge pour l\'esprit, loin du tumulte incessant de la vie quotidienne.', 'L\'amitié sincère ne nécessite pas de grandes démonstrations ; ce sont souvent les petits gestes qui prouvent la force des liens.', 'Prendre le temps d\'admirer la beauté du monde qui nous entoure est une manière simple mais efficace de se reconnecter à soi-même.', 'Chaque échec porte en lui une leçon précieuse, qu\'il est souvent difficile de percevoir sur le moment, mais qui devient évidente avec le recul.', 'Le rire partagé entre amis est l\'une des plus grandes sources de bonheur, car il réchauffe le cœur et illumine les journées grises.', 'La technologie moderne nous rapproche des gens à distance, mais il est important de ne pas oublier les moments partagés en personne.', 'Les étoiles qui brillent dans le ciel nocturne nous rappellent à quel point l\'univers est vaste et mystérieux, invitant à la réflexion.', 'Chaque instant passé avec nos proches est précieux, car le temps file à toute allure, et les souvenirs deviennent rapidement des trésors inestimables.', 'L\'eau d\'un ruisseau qui coule paisiblement invite à la méditation, offrant un moment de calme pour apaiser l\'esprit et revitaliser l\'âme.', 'La créativité s\'épanouit souvent dans les moments de calme, lorsque l\'esprit est libre de vagabonder et de s\'inspirer de tout ce qui l\'entoure.', 'Même les plus petits actes de gentillesse peuvent avoir un impact immense, souvent bien au-delà de ce que l\'on pourrait imaginer à première vue.']

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    lb_intro(stdscr)
    while True:
        lb_tester(stdscr)
        stdscr.addstr(2, 0, 'Good completed ! Press any key...')
        key = stdscr.getkey()
        if ord(key) == 10:
            break
def lb_intro(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Welcome to the WPM typing test !', curses.color_pair(2))
    stdscr.addstr(1, 0, 'Press any key to begin...', curses.color_pair(2))
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

        if ord(key) == 10 or len(user_text) == len(test_text) - 1:
            stdscr.nodelay(False)
            break
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(user_text) > 0:
                user_text.pop()
        else:
            user_text.append(key)
def lb_display_handler(stdscr, test, user, wpm=0):
    stdscr.addstr(test, curses.color_pair(2))
    for i, char in enumerate(user):
        color = curses.color_pair(1)
        if char != test[i]:
            color = curses.color_pair(3)
        stdscr.addstr(0, i, char, color)
        stdscr.addstr(1, 0, f'WPM : {wpm}')

wrapper(main)