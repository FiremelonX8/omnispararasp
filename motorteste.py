import RPi.GPIO as GPIO
import time

# Pinos GPIO para controle do motor
DIR_PIN = 29  # Pino de direção
STEP_PIN = 27  # Pino de passo
DELAY = 0.001  # Intervalo entre os passos, ajusta a velocidade

# Configuração dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

def move_motor(steps, direction, speed=DELAY):
    """
    Gira o motor pelo número de passos especificado.

    :param steps: Número de passos
    :param direction: Direção do motor (True para um lado, False para o outro)
    :param speed: Velocidade do motor (opcional)
    """
    try:
        # Define a direção
        GPIO.output(DIR_PIN, direction)

        for _ in range(steps):
            # Gera um pulso no pino STEP
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(speed)  # Pulso alto
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(speed)  # Pulso baixo
    except Exception as e:
        print(f"Erro ao mover o motor: {e}")

def stop_motor():
    """
    Para o motor.
    """
    move_motor(0, False)

try:
    print("Motor girando em sentido horário...")
    move_motor(200, True)  # Gira 200 passos no sentido horário
    time.sleep(1)  # Pausa

    print("Motor girando em sentido anti-horário...")
    move_motor(200, False)  # Gira 200 passos no sentido anti-horário
    time.sleep(1)  # Pausa

    print("Parando o motor...")
    stop_motor()

except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
finally:
    GPIO.cleanup()
    print("GPIO liberado.")