from pathlib import Path
import random

# Leemos los nombres de participantes.txt y los guardamos en una lista
participantes = [
    p for p in Path("participantes.txt").read_text().split("\n") if p.strip()
]
print("Participantes:")
for participante in participantes:
    print(f"\t- {participante}")

# Desordenamos la lista de participantes
random.shuffle(participantes)
print("Se ha establecido el nuevo orden secreto para formar mafias")

# Leemos los retos de retos.txt y los guardamos en una lista
retos = [r for r in Path("retos.txt").read_text().split("\n") if r.strip()]

# Desordenamos la lista de retos
random.shuffle(retos)
print("Se han establecido los retos")

# Asignamos el reto que tienen que hacer al siguiente participante en la lista circular a cada uno de los participantes

num_participantes = len(participantes)
print("Repartiendo retos...")

for i in range(num_participantes):
    actual = participantes[i]
    siguiente = participantes[(i + 1) % num_participantes]
    reto = retos[i]
    mensaje = f"Mata a {siguiente} {retos[i]}"

    # Guardamos el mensaje en el archivo resultados/actual.txt
    Path(f"resultados/{actual}.txt").write_text(mensaje)

print("Retos repartidos")
print("Consulta la carpeta de resultados para saber a quién matar y cómo")
print("¡Que empiece el juego!")
