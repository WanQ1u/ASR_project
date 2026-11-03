import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Program started")

try:
    with open("audio.wav", "r") as f:
        data = f.read()

except FileNotFoundError:
    logging.exception("Failed to load audio file")

print("Program finished")