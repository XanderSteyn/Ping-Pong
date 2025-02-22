import pygame
import random

pygame.init()

ScreenWidth, ScreenHeight = 800, 600
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Ping Pong")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (153, 101, 21)
RETRO = (0, 0, 0)
RETRO_OPACITY = 128

Font = pygame.font.SysFont("Arial", 50, bold = True)
MiniFont = pygame.font.SysFont("Arial", 30)

PaddleWidth, PaddleHeight = 15, 100
PlayerX, PlayerY = 50, ScreenHeight // 2 - PaddleHeight // 2
EnemyX, EnemyY = ScreenWidth - 50 - PaddleWidth, ScreenHeight // 2 - PaddleHeight // 2

BallWidth = 15
BallX, BallY = ScreenWidth // 2 - BallWidth // 2, ScreenHeight // 2 - BallWidth // 2
BallDX, BallDY = random.choice([1, -1]) * 5, random.choice([1, -1]) * 5

pygame.mixer.init()
HitSFX = pygame.mixer.Sound("SFX/Return.mp3")
EdgeSFX = pygame.mixer.Sound("SFX/Send.mp3")
LoseSFX = pygame.mixer.Sound("SFX/You Lose.mp3")

Background = pygame.image.load("Sprites/Background.png")

BallImage = pygame.image.load("Sprites/Ball.png")
BallImage = pygame.transform.scale(BallImage, (BallWidth, BallWidth))

Clock = pygame.time.Clock()

def ActiveGame():
    global BallX, BallY, BallDX, BallDY, PlayerY, EnemyY
    GameRunning = True
    Paused = False

    RetroOverlay = pygame.Surface((ScreenWidth, ScreenHeight))
    RetroOverlay.fill(RETRO)
    RetroOverlay.set_alpha(RETRO_OPACITY)

    while GameRunning:
        Screen.blit(pygame.transform.scale(Background, (ScreenWidth, ScreenHeight)), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    Paused = not Paused

        if Paused:
            Screen.blit(RetroOverlay, (0, 0))

            PausedText = Font.render("PAUSED", True, RED)
            Screen.blit(PausedText, (ScreenWidth // 2 - PausedText.get_width() // 2, ScreenHeight // 2 - 50))
            pygame.display.flip()
            continue

        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_UP] and PlayerY > 0:
            PlayerY -= 7
        if Keys[pygame.K_DOWN] and PlayerY < ScreenHeight - PaddleHeight:
            PlayerY += 7

        BallX += BallDX
        BallY += BallDY

        if BallY <= 0 or BallY >= ScreenHeight - BallWidth:
            BallDY = -BallDY
            EdgeSFX.play()

        if BallX <= PlayerX + PaddleWidth and PlayerY < BallY < PlayerY + PaddleHeight:
            BallDX = -BallDX
            BallDY += random.choice([-1, 0, 1])
            BallDY = max(-5, min(5, BallDY))
            HitSFX.play()

        if BallDX > 0:
            if EnemyY + PaddleHeight // 2 < BallY:
                EnemyY += 5
            elif EnemyY + PaddleHeight // 2 > BallY:
                EnemyY -= 5

        if BallX <= 0:
            GameOverScreen()
            return

        if BallX >= EnemyX - BallWidth and EnemyY < BallY < EnemyY + PaddleHeight:
            BallDX = -BallDX
            BallDY += random.choice([-1, 0, 1])
            BallDY = max(-5, min(5, BallDY))
            HitSFX.play()

        pygame.draw.rect(Screen, BROWN, (PlayerX, PlayerY, PaddleWidth, PaddleHeight))
        pygame.draw.rect(Screen, BROWN, (EnemyX, EnemyY, PaddleWidth, PaddleHeight))
        Screen.blit(BallImage, (BallX, BallY))

        pygame.display.flip()
        Clock.tick(60)

def GameOverScreen():
    LoseSFX.play()
    Retry = False
    FadeIn = True

    while not Retry:
        Screen.fill((0, 0, 128))

        for i in range(0, ScreenHeight, 2):
            pygame.draw.line(Screen, (135, 206, 250), (0, i), (ScreenWidth, i))

        GameOverText = Font.render("GAME OVER", True, RED)
        TextRect = GameOverText.get_rect(center=(ScreenWidth // 2, ScreenHeight // 3))
        Screen.blit(GameOverText, TextRect)

        RetryText = MiniFont.render("Press R to Restart", True, WHITE)
        RetryTextRect = RetryText.get_rect(center=(ScreenWidth // 2, ScreenHeight // 2 + 100))
        Screen.blit(RetryText, RetryTextRect)

        if FadeIn:
            Alpha = max(0, GameOverText.get_alpha() - 5)
            GameOverText.set_alpha(Alpha)
            if Alpha == 0:
                FadeIn = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Retry = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    RestartGame()
                    ActiveGame()
                    return
                if event.key == pygame.K_ESCAPE:
                    Retry = True

        pygame.display.flip()
        Clock.tick(60)

def RestartGame():
    global BallX, BallY, BallDX, BallDY, PlayerY, EnemyY

    BallX, BallY = ScreenWidth // 2 - BallWidth // 2, ScreenHeight // 2 - BallWidth // 2
    BallDX, BallDY = 5, random.choice([1, -1]) * 5
    PlayerY = ScreenHeight // 2 - PaddleHeight // 2
    EnemyY = ScreenHeight // 2 - PaddleHeight // 2

ActiveGame()
pygame.quit()