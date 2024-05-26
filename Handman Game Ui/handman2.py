import pygame
from pygame.locals import *
import random
import pandas
from string import ascii_letters

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Hangman")


class Hangman:
    def __init__(self):
        self.load_words()
        self.reset_game()
        self.background_color = (200, 200, 200)
        self.gallow_color = (0, 0, 0)
        self.body_color = (255, 253, 175)
        self.font = pygame.font.SysFont("Courier New", 20)
        self.title_font = pygame.font.SysFont("Courier New", 30, bold=True)
        self.FPS = pygame.time.Clock()

    def load_words(self):
        with open("./words.txt", "r") as file:
            self.words = file.read().split("\n")

    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guessed_word = "*" * len(self.secret_word)
        self.wrong_guesses = []
        self.wrong_guess_count = 0
        self.taking_guess = True

    def _gallow(self):
        pygame.draw.rect(screen, self.gallow_color, pygame.Rect(75, 280, 120, 10))
        pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 10, 240))
        pygame.draw.rect(screen, self.gallow_color, pygame.Rect(128, 40, 80, 10))
        pygame.draw.rect(screen, self.gallow_color, pygame.Rect(205, 40, 10, 30))

    def _man_pieces(self):
        if self.wrong_guess_count >= 1:
            pygame.draw.circle(screen, self.body_color, [210, 85], 20, 0)
        if self.wrong_guess_count >= 2:
            pygame.draw.rect(screen, self.body_color, pygame.Rect(206, 105, 8, 45))
        if self.wrong_guess_count >= 3:
            pygame.draw.line(screen, self.body_color, [183, 149], [200, 107], 6)
        if self.wrong_guess_count >= 4:
            pygame.draw.line(screen, self.body_color, [231, 149], [218, 107], 6)
        if self.wrong_guess_count >= 5:
            pygame.draw.line(screen, self.body_color, [189, 198], [208, 148], 6)
        if self.wrong_guess_count >= 6:
            pygame.draw.line(screen, self.body_color, [224, 198], [210, 148], 6)

    def _right_guess(self, guess_letter):
        index_positions = [index for index, item in enumerate(self.secret_word) if item == guess_letter]
        for i in index_positions:
            self.guessed_word = self.guessed_word[:i] + guess_letter + self.guessed_word[i + 1:]
        screen.fill(pygame.Color(self.background_color), (10, 370, 390, 20))

    def _wrong_guess(self, guess_letter):
        self.wrong_guesses.append(guess_letter)
        self.wrong_guess_count += 1
        screen.fill(self.background_color)  # Clear the screen before drawing
        self._draw_game_elements()
        pygame.display.flip()  # Update the display immediately

    def _guess_taker(self, guess_letter):
        if guess_letter in ascii_letters:
            if guess_letter in self.secret_word and guess_letter not in self.guessed_word:
                self._right_guess(guess_letter)
            elif guess_letter not in self.secret_word and guess_letter not in self.wrong_guesses:
                self._wrong_guess(guess_letter)

    def _message(self):
        if self.guessed_word == self.secret_word:
            self.taking_guess = False
            screen.fill(pygame.Color(0, 128, 0), (40, 218, 320, 30))
            message = self.font.render("YOU WIN!!", True, (255, 255, 255))
            screen.blit(message, (152, 224))
        elif self.wrong_guess_count == 6:
            self.taking_guess = False
            screen.fill(pygame.Color(128, 0, 0), (40, 218, 320, 30))
            message = self.font.render("GAME OVER YOU LOSE!!", True, (255, 255, 255))
            screen.blit(message, (78, 224))
            word = self.font.render(f"Secret word: {self.secret_word}", True, (255, 255, 255))
            screen.blit(word, (10, 300))
        if not self.taking_guess:
            screen.fill(pygame.Color(self.background_color), (35, 460, 390, 20))

    def draw_reset_button(self):
        self.reset_button = pygame.Rect(290, 10, 100, 50)
        pygame.draw.rect(screen, (0, 0, 255), self.reset_button)
        reset_text = self.font.render("Reset", True, (255, 255, 255))
        screen.blit(reset_text, (305, 25))

    def _draw_game_elements(self):
        self._gallow()
        self._man_pieces()
        self.draw_reset_button()
        title = self.title_font.render("Hangman", True, (0, 0, 0))
        screen.blit(title, (140, 10))
        guessed_word = self.font.render(f"Guessed word: {self.guessed_word}", True, (0, 0, 138))
        screen.blit(guessed_word, (10, 370))
        wrong_guesses = self.font.render(f"Wrong guesses: {' '.join(map(str, self.wrong_guesses))}", True, (125, 0, 0))
        screen.blit(wrong_guesses, (10, 420))
        self._message()

    def main(self):
        while True:
            screen.fill(self.background_color)
            self._draw_game_elements()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN and self.taking_guess:
                    self._guess_taker(event.unicode)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.reset_button.collidepoint(event.pos):
                        self.reset_game()

            pygame.display.flip()
            self.FPS.tick(60)


if __name__ == "__main__":
    h = Hangman()
    h.main()
