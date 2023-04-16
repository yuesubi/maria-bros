import pygame
from typing import Union

from .....utils import Vec2
from ...event_manager import EventManager
from ..anchor import Anchor
from ..fit import Fit
from ..widget import Widget


class Frame(Widget):
    """Cadre pour l'IHM, peut contenir des sous éléments."""

    def __init__(
            self,
            position: Vec2,
            anchor: Anchor,
            size: Vec2,
            fit: Fit = Fit.NONE,
            background_color: Union[pygame.Color, None] = None,
            border_color: Union[pygame.Color, None] = None,
            border_width: int = 1,
            children: list[Widget] = list()
        ) -> None:
        """
        Constructeur d'un cadre.
        :param position: La position du cadre.
        :param anchor: L'origine du cadre.
        :param size: La taille du cadre.
        :param fit: L'adaptation au parent. (optionnel)
        :param background_color: La couleur de fond du cadre, si la couleur
            est None, le fond est transparent. (optionnel)
        :param border_color: La couleur du bord du cadre, si la couleur est
            None, le bord est transparent. (optionnel)
        :param border_width: L'épaisseur du bord du cadre. (optionnel)
        :param children: Une liste l'éléments de l'IHM enfants. (optionnel)
        """

        # Initialisation de la classe parent
        super().__init__(
            position, anchor,
            size, fit
        )

        self.background_color: Union[pygame.Color, None] = background_color
        self.border_color: Union[pygame.Color, None] = border_color
        self.border_width: int = border_width

        self._children: list[Widget] = list(children)
        
        # Mettre ce cadre en tant que parent de chaque élément enfant
        for child in self._children:
            child.parent = self
    
    def add_child(self, child: Widget) -> None:
        """
        Ajouter un enfant.
        :param child: L'enfant à ajouter.
        """
        child.parent = self
        self._children.append(child)
    
    def remove_child(self, child: Widget) -> None:
        """
        Retirer un enfant.
        :param child: L'enfant à retirer.
        """
        child.parent = None
        self._children.remove(child)
    
    def process_events(self, event_manager: EventManager) -> None:
        # Appeler la fonction sur tout les enfants
        for child in self._children:
            child.process_events(event_manager)
    
    def update(self, delta_time: float) -> None:
        for child in self._children:
            # Adapter la taille de l'enfant si besoin
            if child.fit == Fit.WIDTH or child.fit == Fit.BOTH:
                child.size.x = self.size.x
            if child.fit == Fit.HEIGHT or child.fit == Fit.BOTH:
                child.size.y = self.size.y

            # Mettre à jour l'enfant
            child.update(delta_time)
    
    def render(self, target: pygame.Surface) -> None:
        # Le rectangle du cadre
        rectangle = pygame.Rect(
            self.global_position(Anchor.NW),
            self.size
        )

        # Dessiner le fond du cadre
        if self.background_color is not None:
            pygame.draw.rect(target, self.background_color, rectangle)
        
        # Dessiner la bordure du cadre
        if self.border_color is not None:
            pygame.draw.rect(
                target, self.border_color,
                rectangle, self.border_width
            )

        # Appeler la fonction sur tout les enfants
        for child in self._children:
            child.render(target)
