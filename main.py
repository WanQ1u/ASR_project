import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Program started")
logging.info("Loading model")
logging.warning("GPU memory is running low")
logging.error("Model loading failed")

print("Program finished")