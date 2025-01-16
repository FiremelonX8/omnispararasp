import RPi.GPIO as GPIO
import time

# Configurações dos pinos
STEP_PIN = 27  # Pino STEP (GPIO 27)
DIR_PIN = 29   # Pino DIR (GPIO 29)

# Configuração inicial do GPIO
GPIO.setmode(GPIO.BCM)  # Use a numeração BCM dos pinos
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Configuração inicial dos sinais
GPIO.output(DIR_PIN, GPIO.LOW)  # Sentido inicial do motor
GPIO.output(STEP_PIN, GPIO.LOW)

def step_motor(steps, direction, delay):
    """
    Controla o motor de passo.
    
    :param steps: Número de passos
    :param direction: Sentido (True para frente, False para trás)
    :param delay: Tempo entre os passos (em segundos)
    """
    GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
    
