
from controller.play import play, cv2
import cv2
from numpy import zeros, uint8


class Menu():
    def __init__(self) -> None:
        self.exit = False
        while not self.exit:
            self.generate_image()
            cv2.waitKey(0)
    
    def callback(self, event, x, y, flags, params):
        if event == 0:
            if x >= 150 and x <= 345 and y >= 150 and y <= 200:
                self.generate_image(1)
            elif x >= 185 and x <= 300 and y >= 265 and y <= 315:
                self.generate_image(2)
            else:
                self.generate_image(0)
        elif event == 1:
            if x >= 150 and x <= 345 and y >= 150 and y <= 200:
                play()
            elif x >= 185 and x <= 300 and y >= 265 and y <= 315:
                self.exit = True
                cv2.destroyAllWindows()

    def generate_image(self, hover: int = 0):
        img = zeros([400, 520, 3], uint8)
        img[::] = (56, 22, 25)
        cv2.putText(img,
                    "Termo",
                    [150, 75],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255, 255, 255),
                    4)
        cv2.putText(img,
                    "Novo Jogo",
                    [165, 185],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2)
        cv2.putText(img,
                    "Sair",
                    [210, 300],
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2)
        if hover == 1:
            cv2.rectangle(img, [150, 200], [345, 150],
                        (0, 0, 250), 4)
        else:
            cv2.rectangle(img, [150, 200], [345, 150],
                        (250, 250, 250), 4)
        if hover == 2:
            cv2.rectangle(img, [185, 315], [300, 265],
                        (0, 0, 250), 4)
        else:
            cv2.rectangle(img, [185, 315], [300, 265],
                        (250, 250, 250), 4)
        cv2.imshow("Termo", img)
        cv2.setMouseCallback('Termo', self.callback)
        

Menu().generate_image()