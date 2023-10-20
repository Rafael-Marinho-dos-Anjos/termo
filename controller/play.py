
from controller.game import GameControl, cv2


letters = "abcdefghijklmnopqrstuvwxyz"

def play():
    game = GameControl()

    def mouse_callback(event, x, y, flags, params):
        if event == 1:
            index = game.clicked_cell(x, y)
            if index > -1:
                game.navigate_to(index)
        
        cv2.imshow("Termo", game.generate_image())

    cv2.imshow("Termo", game.generate_image())
    cv2.setMouseCallback('Termo', mouse_callback)

    while not game.game_over:
        key = cv2.waitKey(0)
        if key == 13:
            game.submit()
        
        elif key == 8:
            game.erease_cell()

        elif key == 27:
            game.game_over = True

        elif key == 0:
            game.navigate_left()

        else:
            key = chr(key)
            if key in letters:
                game.fill_cell(key)
        
        cv2.imshow("Termo", game.generate_image())

    print("Palavra correta:", game.right_word)
    cv2.waitKey(0)
