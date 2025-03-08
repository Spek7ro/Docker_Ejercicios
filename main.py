import logging, sys
import time
import requests

h = [
  logging.FileHandler('./log.log'), 
  logging.StreamHandler(stream=sys.stdout),
]

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s',
  handlers=h,
)

logger = logging.getLogger(__name__)

def main():
  r = requests.get('https://cristian-web.vercel.app/')
  logger.info('Hello World!')
  logger.info('Iniciando un ejercicio')
  time.sleep(5)
  logger.info(r.text)
  logger.info('37')
  logger.info('Terminando un ejercicio')


if __name__ == '__main__':
  main()