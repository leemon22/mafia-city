# MAFIA CITY

Pequeño programa para sortear el juego de este [tiktok](https://www.tiktok.com/@gemelas_villena/video/7408680601882053921?_r=1&_t=8pJYb7etGe8), así todos pueden jugar, incluido el organizador.

El juego es ideal por si os juntais un montón de gente durante varios días en algún lugar como una casa rural.

## Como funciona

En primer lugar, escribe todos los participantes en un archivo `participantes.txt` en el mismo formato que en el archivo `participantes.example`. Importante, no dejes líneas en blanco dentro del archivo.

En segundo lugar, rellena un archivo `retos.txt` con el mismo formato que `retos.example`. Intenta que los retos sigan el siguiente estilo 'haciendo que te escriba una nota de amor divertida.', ya que luego se formarán frases del tipo 'Mata a Dani haciendo que te escriba una nota de amor divertida.'
Recomiendo poner más de un reto por persona, así no se saben exactamente los retos que hay. Si se ponen retos de menos el programa falla.

Luego, ejecuta en el directorio principal el comando `python generate.py`. Esto generará en el directorio `resultados` los retos que tienen que cumplir los participantes. Por ejemplo, si tú eres Andrés en el archivo participantes, entonces abrirías el archivo `Andrés.txt` generado en el directorio `resultados`. Un ejemplo de resultado es el mencionado anteriormente.

Finalmente recomiendo que cada participante anote su reto y se eliminen del ordenador que los ha generado ejecutando `python clearall.py`. Este comando solo borra los archivos generados en `resultados`. Si quieres borrar el archivo de retos lo borras a mano.

A disfrutar :P
