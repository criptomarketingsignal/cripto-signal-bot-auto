import schedule
import time
import subprocess
from datetime import datetime
import pytz

# Zona horaria de Nueva York
ny_tz = pytz.timezone("America/New_York")

def run_prompt(file_name):
    try:
        subprocess.run(["python", file_name], check=True)
        print(f"✅ Ejecutado correctamente: {file_name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando {file_name}: {e}")

def job_prompt_01():
    current_time = datetime.now(ny_tz).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Ejecutando prompt_01...")
    run_prompt("prompt_01.py")

def job_prompt_02():
    current_time = datetime.now(ny_tz).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Ejecutando prompt_02...")
    run_prompt("prompt_02.py")

def job_prompt_03():
    current_time = datetime.now(ny_tz).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Ejecutando prompt_03...")
    run_prompt("prompt_03.py")

# Programación en hora local de Nueva York
schedule.every().day.at("09:50").do(job_prompt_01)
schedule.every().day.at("12:50").do(job_prompt_02)
schedule.every().day.at("20:30").do(job_prompt_03)

print("⏱️ Scheduler activo. Esperando próximas ejecuciones...")

while True:
    schedule.run_pending()
    time.sleep(1)
