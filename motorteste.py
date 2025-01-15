import RPi.GPIO as GPIO
import time

# Pinos GPIO para controle do motor
DIR_PIN = 27  # Pino de direção
STEP_PIN = 29  # Pino de passo
DELAY = 0.001  # Intervalo entre os passos, ajusta a velocidade

# Configuração dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)


def move_motor(steps, direction):
    """
    Gira o motor pelo número de passos especificado.

    :param steps: Número de passos
    :param direction: Direção do motor (True para um lado, False para o outro)
    """
    # Define a direção
    GPIO.output(DIR_PIN, direction)

    for _ in range(steps):
        # Gera um pulso no pino STEP
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(DELAY)  # Pulso alto
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(DELAY)  # Pulso baixo


try:
    print("Motor girando em sentido horário...")
    move_motor(200, True)  # Gira 200 passos no sentido horário
    time.sleep(1)  # Pausa

    print("Motor girando em sentido anti-horário...")
    move_motor(200, False)  # Gira 200 passos no sentido anti-horário
    time.sleep(1)  # Pausa

except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
finally:
    GPIO.cleanup()
    print("GPIO liberado.")
