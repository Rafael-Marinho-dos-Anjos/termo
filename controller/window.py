
import cv2
from numpy import zeros, uint8
from model.words import fix_letters


def resize_to_scale(image, scale: float) -> None:
    new_size = [image.shape[i] for i in (1, 0)]
    new_size = tuple(map(lambda x: int(x * scale), new_size))
    image = cv2.resize(image, new_size)
    return image


def fill(background, fill_image, x, y):
    background[y:y+fill_image.shape[0], x:x+fill_image.shape[1]] = fill_image


def get_coordinates(column, line, image) -> tuple:
    border = image.shape[1]//36 # 900/25
    element_side = border * 7
    return (border + element_side * column, border + element_side * line)


def get_letter_coordinates(column, line, image) -> tuple:
    border = image.shape[1]//36 # 900/25
    element_side = border * 7
    border_ = int(border * 1.75)
    line += 1
    return (border_ + element_side * column, element_side * line - border)


def generate_image(submits, filling_text, right_word, selected, scale=0.4):
    img = resize_to_scale(zeros([1250, 900, 3], uint8), scale)
    img[::] = (56, 22, 25)

    frame_empty = resize_to_scale(cv2.imread(r"templates\empty_box.bmp"), scale)
    frame_black = resize_to_scale(cv2.imread(r"templates\black_box.bmp"), scale)
    frame_green = resize_to_scale(cv2.imread(r"templates\green_box.bmp"), scale)
    frame_yellow = resize_to_scale(cv2.imread(r"templates\yellow_box.bmp"), scale)
    frame_selected = resize_to_scale(cv2.imread(r"templates\selected_box.bmp"), scale)

    for line, word in enumerate(submits):
        for col, letter in enumerate(word):
            if letter == fix_letters(right_word)[col]:
                fill(img, frame_green, *get_coordinates(col, line, img))
            elif letter is not None and letter in fix_letters(right_word):
                fill(img, frame_yellow, *get_coordinates(col, line, img))
            else:
                fill(img, frame_empty, *get_coordinates(col, line, img))
            
            if letter is not None:
                cv2.putText(img,
                            letter.upper(),
                            get_letter_coordinates(col, line, img),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            scale*4,
                            (255, 255, 255),
                            3)

    for col, letter in enumerate(filling_text):
        if col == selected:
            fill(img, frame_selected, *get_coordinates(col, 6, img))
        else:
            fill(img, frame_black, *get_coordinates(col, 6, img))
        if letter is not None:
            cv2.putText(img,
                        letter.upper(),
                        get_letter_coordinates(col, 6, img),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        scale*4,
                        (255, 255, 255),
                        3)
    
    return img
