import random
from pathlib import Path
import string
import math

SCORE_FILE = Path("scores.txt")
ALLOWED_CHARS = string.ascii_letters + string.digits + string.punctuation
DIFFICULTY_NAMES = {10: "Muy fácil", 25: "Fácil", 100: "Media", 500: "Difícil", 1000: "Extremo"}

def get_valid_name(prompt="Ingresa tu nombre: "):
    while True:
        name = input(prompt).strip().upper()
        if not (1 <= len(name) <= 6):
            print("El nombre debe tener entre 1 y 6 caracteres.")
            continue
        if all(c in ALLOWED_CHARS for c in name):
            return name
        else:
            print("Solo se permiten letras, números y caracteres especiales.")

def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"El número debe ser al menos {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"El número debe ser como máximo {max_val}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")

def choose_difficulty():
    print("Elige una dificultad:")
    print("1. Muy fácil (1 - 10)")
    print("2. Fácil (1 - 25)")
    print("3. Media (1 - 100)")
    print("4. Difícil (1 - 500)")
    print("5. Extremo (1 - 1000)")
    choice = get_int_input("Opción (1-5): ", 1, 5)
    limits = [10, 25, 100, 500, 1000]
    return limits[choice - 1]

def hint_distance(secret, guess, limit):
    diff = abs(secret - guess)
    if limit <= 25:
        if diff == 0: return "¡Exacto!"
        elif diff == 1: return "¡Extremadamente caliente!"
        elif diff <= 2: return "Muy caliente"
        elif diff <= 4: return "Caliente"
        elif diff <= 7: return "Tibio"
        elif diff <= 12: return "Frío"
        else: return "¡Congelado!"
    elif limit <= 100:
        if diff == 0: return "¡Exacto!"
        elif diff <= 2: return "¡Extremadamente caliente!"
        elif diff <= 5: return "Muy caliente"
        elif diff <= 10: return "Caliente"
        elif diff <= 20: return "Tibio"
        elif diff <= 40: return "Frío"
        else: return "¡Congelado!"
    elif limit <= 500:
        if diff == 0: return "¡Exacto!"
        elif diff <= 5: return "¡Extremadamente caliente!"
        elif diff <= 15: return "Muy caliente"
        elif diff <= 30: return "Caliente"
        elif diff <= 60: return "Tibio"
        elif diff <= 150: return "Frío"
        else: return "¡Congelado!"
    else:
        if diff == 0: return "¡Exacto!"
        elif diff <= 10: return "¡Extremadamente caliente!"
        elif diff <= 30: return "Muy caliente"
        elif diff <= 60: return "Caliente"
        elif diff <= 120: return "Tibio"
        elif diff <= 250: return "Frío"
        else: return "¡Congelado!"

def calc_score(limit, attempts_used):
    base_score = limit * 50  # escala arcade
    # logaritmo en base 1.5 para suavizar penalización de intentos
    score = int(base_score / math.log(attempts_used + 1, 1.5))
    return max(score, 1)

def load_scores():
    scores = []
    if SCORE_FILE.exists():
        try:
            with SCORE_FILE.open("r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        name, score, diff, attempts = parts
                        scores.append((name, int(score), diff, int(attempts)))
                    else:
                        name, score = parts
                        scores.append((name, int(score), "Desconocida", 0))
        except Exception:
            print("Error al leer el archivo de puntuaciones. Se reiniciará.")
    return scores

def save_scores(scores):
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    with SCORE_FILE.open("w", encoding="utf-8") as f:
        for name, score, diff, attempts in scores:
            f.write(f"{name},{score},{diff},{attempts}\n")

def show_scores():
    scores = load_scores()
    if not scores:
        # jugadores artificiales
        scores = [("PLAYER", 1, "Muy fácil", 5) for _ in range(5)]
    while len(scores) < 5:
        scores.append(("PLAYER", 1, "Muy fácil", 5))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]

    print("\n=== Top puntuaciones ===")
    for i, (name, score, diff, attempts) in enumerate(scores, start=1):
        print(f"{i}. {name} - {score} puntos (Dificultad: {diff}, Intentos: {attempts})")
    print(f"Puntuación máxima posible: 50000")
    for name, score, diff, attempts in scores:
        if score >= 50000 and name != "PLAYER":
            print(f"¡Puntuación máxima alcanzada por {name}!")
    print("-----------------------------\n")

def play_game():
    try:
        limit = choose_difficulty()
        num = random.randint(1, limit)
        max_attempts = get_int_input("¿Cuántos intentos quieres (mínimo 5)? ", 5)
        attempts = 0
        diff_text = DIFFICULTY_NAMES[limit]
        print(f"\nHe elegido un número entre 1 y {limit}. ¡Adivínalo!\n")

        while True:
            guess = get_int_input(f"Intento #{attempts + 1}: ", 1, limit)
            attempts += 1
            if guess == num:
                print(f"¡Correcto! Adivinaste el número {num} en {attempts} intentos.")
                score = calc_score(limit, attempts)
                print(f"Tu puntaje: {score}")
                scores = load_scores()
                # revisar si puntaje máximo
                if score >= 50000:
                    print("¡¡Has alcanzado la puntuación máxima!!")
                    name = get_valid_name()
                    scores = [(name, score, diff_text, attempts)] + [s for s in scores if s[1] != 50000]
                    save_scores(scores)
                else:
                    if len(scores) < 5 or score > min(s[1] for s in scores):
                        name = get_valid_name()
                        scores.append((name, score, diff_text, attempts))
                        save_scores(scores)
                break
            else:
                print(hint_distance(num, guess, limit))
                if attempts >= max_attempts:
                    print(f"\nSe acabaron los intentos. El número era {num}.\n")
                    break
                print(f"Intentos restantes: {max_attempts - attempts}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def hot_cold_game():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar")
        print("2. Ver puntuaciones")
        print("3. Salir")
        choice = get_int_input("Elige una opción: ", 1, 3)
        if choice == 1:
            play_game()
        elif choice == 2:
            show_scores()
        elif choice == 3:
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    hot_cold_game()
print("-----------------------------------------------------------")