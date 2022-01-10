import pygame

# definir une class qui va s'occuper des animation


class AnimateSprite(pygame.sprite.Sprite):

    # Definir les chose a faire a la creation de l'entité
    def __init__(self, sprite_name, size=(120, 120)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # commencer l'anime a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

        # Definir une methode pour demarré l'animation

    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self, loop=False):

        # verifier si l'animation est active
        if self.animation:

            # passer a l'image suivante
            self.current_image += 1

            # verifier si on atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre lanimation au depart
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # Charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # recuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # bloucler sur chaque image du dossier
    for num in range(1, 14):
        image_path = path + str(num) + ".png"
        pygame.image.load(image_path)
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images


# Definir un dictionnaire qui va contenir toute les images charger de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png, ...]
animations = {
    "gaulois": load_animation_images("gaulois"),
    "player": load_animation_images("player"),
    "attack": load_animation_images("attack")
    # "gaulois_archer": load_animation_images("gaulois_archer"),
}
