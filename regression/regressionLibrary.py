import os
import subprocess

# Definindo o diretório de logs
log_directory = "logs"
screenshot_directory = os.path.join(log_directory, "screenshots")

# Cria os diretórios, se não existirem
os.makedirs(log_directory, exist_ok=True)
os.makedirs(screenshot_directory, exist_ok=True)

# Comando para executar o Robot Framework com a configuração de logs
subprocess.run([
    "robot",
    f"--output {log_directory}/output.xml",
    f"--report {log_directory}/report.html",
    f"--log {log_directory}/log.html",
    f"--variable SCREENSHOT_DIR:{screenshot_directory}",
    "seu_arquivo_de_teste.robot"
])
