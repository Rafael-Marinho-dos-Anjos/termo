
from controller.window import generate_image, get_coordinates, cv2
from model.words import new_word, verify_word, fix_letters


class GameControl():
    def __init__(self, scale: float = 0.4) -> None:
        self.right_word = new_word()
        self.submits = [
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]
            ]
        self.filling = [None, None, None, None, None]
        self.selected = 0
        self.chance = 0
        self.game_over = False
        self.scale = scale
        self.last_image = None

    def submit(self):
        if None in self.filling:
            return
        if not verify_word("".join(self.filling)):
            print("Palavra desconhecida!")
        else:
            self.submits[self.chance] = self.filling
            if "".join(self.submits[self.chance]) == fix_letters(self.right_word) or self.chance == 5:
                self.game_over = True
            self.chance += 1
        self.filling = [None, None, None, None, None]
        self.selected = 0

        
    def generate_image(self):
        image = generate_image(
            self.submits,
            self.filling,
            self.right_word,
            self.selected,
            self.scale
        )
        self.last_image = image
        return image

    def navigate_to(self, index: int):
        if index in range(5):
            self.selected = index
    
    def navigate_left(self):
        if self.selected > 0:
            self.selected -= 1
    
    def navigate_right(self):
        if self.selected < 5:
            self.selected += 1

    def clicked_cell(self, x, y):
        for i in range(5):
            coord = get_coordinates(i, 6, self.last_image)
            side = int(150 * self.scale)
            if x < coord[0] or x > coord[0] + side:
                continue

            if y < coord[1] or y > coord[1] + side:
                continue

            return i

        return -1
    
    def fill_cell(self, letter):
        self.filling[self.selected] = letter
        if self.selected < 4:
            self.selected += 1
    
    def erease_cell(self):
        if self.filling[self.selected] is not None and self.selected == 4:
            self.filling[self.selected] = None
            return
        if self.filling[self.selected] is None and self.selected > 0:
            self.filling[self.selected-1] = None
        else:
            self.filling[self.selected] = None
        if self.selected > 0:
            self.selected -= 1
