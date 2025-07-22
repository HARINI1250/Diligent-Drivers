# Diligent-Drivers
import pygame
import random
import sys
import tkinter as tk
from tkinter import messagebox
import cv2

def show_tkinter_start():
    def on_start():
        root.destroy()

    root = tk.Tk()
    root.title("Car Race Login")
    root.geometry("400x200")
    tk.Label(root, text="Welcome to the Car Race!", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Start Race", command=on_start, font=("Arial", 12)).pack(pady=10)
    root.mainloop()

def show_opencv_intro():
    cap = cv2.VideoCapture(0)  # use 0 for webcam; replace with 'video.mp4' for video
    if not cap.isOpened():
        print("Webcam not accessible.")
        return

    frame_count = 0
    while frame_count < 100:  # Show ~3 seconds
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (600, 400))
        cv2.imshow("Race Intro - Press Q to Skip", frame)
        frame_count += 1
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Car Race with Login")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

car1_img = pygame.image.load("blue (1).png")
car2_img = pygame.image.load("b (1).png")
car1_img = pygame.transform.scale(car1_img, (100, 60))
car2_img = pygame.transform.scale(car2_img, (100, 60))
car1 = {"number": "", "color": "", "fuel": 100, "x": 50, "y": 150, "odometer": 0}
car2 = {"number": "", "color": "", "fuel": 100, "x": 50, "y": 300, "odometer": 0}
finish_line = 750
winner = None

def get_text_input(prompt, y):
    input_box = pygame.Rect(300, y, 200, 32)
    color_inactive = pygame.Color('gray15')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ""
    done = False
    while not done:
        screen.fill((0, 0, 0))
        txt_surface = font.render(prompt + text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x - 250, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        pygame.display.flip()
        clock.tick(30)
    return text

def get_user_inputs():
    car1["number"] = get_text_input("Enter Car 1 Number: ", 100)
    car1["color"] = get_text_input("Enter Car 1 Color: ", 150)
    car1["fuel"] = int(get_text_input("Enter Car 1 Fuel: ", 200))
    car2["number"] = get_text_input("Enter Car 2 Number: ", 250)
    car2["color"] = get_text_input("Enter Car 2 Color: ", 300)
    car2["fuel"] = int(get_text_input("Enter Car 2 Fuel: ", 350))

def draw_car(car, img):
    screen.blit(img, (car["x"], car["y"]))
    label = font.render(f"{car['number']} ({car['color']})", True, (255, 255, 255))
    screen.blit(label, (car["x"], car["y"] - 25))

def show_winner(car):
    screen.fill((0, 0, 0))
    text = f"Winner: {car['number']} | Odometer: {car['odometer']} | Fuel Left: {int(car['fuel'])}"
    label = font.render(text, True, (0, 255, 0))
    screen.blit(label, (100, 200))
    pygame.display.update()
    pygame.time.wait(5000)
    
def run_race():
    global winner
    running = True
    while running:
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        if not winner:
            for car in [car1, car2]:
                if car["fuel"] > 0:
                    step = random.randint(5, 10)
                    car["x"] += step
                    car["fuel"] -= step * 0.4
                    car["odometer"] += step
                    if car["x"] >= finish_line:
                        winner = car
                        break
        draw_car(car1, car1_img)
        draw_car(car2, car2_img)
        pygame.display.update()
        clock.tick(30)
        if winner:
            pygame.time.wait(1000)
            show_winner(winner)
            running = False
show_tkinter_start()
show_opencv_intro()
get_user_inputs()
run_race()
