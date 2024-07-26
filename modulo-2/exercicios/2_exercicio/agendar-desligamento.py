import os

'''os.system('sudo shutdown -h now')''' # Para desligar o computador imediatamente
'''os.system('sudo shutdown -r now')''' # Para reiniciar o computador imediatamente

os.system('sudo shutdown -h 60') # Agendamento o desligamento para 1h
os.system('shutdown -c') # Cancela o agendamento

os.system('sudo shutdown -h 90') # Agendamento o desligamento para 1h30min
os.system('shutdown -c') 