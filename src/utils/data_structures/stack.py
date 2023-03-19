import typing


T = typing.TypeVar("T")


class Stack(typing.Generic[T]):
    """Classe représentant la structure de données pile."""
    
    def __init__(self) -> None:
        """Constructeur."""
        self._internal_list: list[T] = list()
    
    @property
    def is_empty(self) -> bool:
        """
        Savoir si la pile est vide ou non.
        :return: Vrai si la pile est vide, Faux sinon.
        """
        return len(self._internal_list) == 0
    
    def __len__(self) -> int:
        """
        Récupérer la taille de la pile.
        :return: La taille.
        """
        return len(self._internal_list)

    def push(self, value: T) -> None:
        """
        Empiler une valeur.
        :param value: La valeur à empiler.
        """
        self._internal_list.append(value)
    
    def pop(self) -> T:
        """
        Dépiler une valeur. [!] Lance IndexError si la pile est vide.
        :return: La valeur dépilée.
        """
        return self._internal_list.pop()