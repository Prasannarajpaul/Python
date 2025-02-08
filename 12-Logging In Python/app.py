import logging

# Logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%M-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} and {b} = {result}")
    return result
def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {b} from {a} = {result}")
    return result
def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} and {b} = {result}")
    return result
def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} by {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by Zero Error")
        return None


add(10, 5)
subtract(15, 10)
multiply(10, 10)
divide(10, 0)
divide(10, 2)