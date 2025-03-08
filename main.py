import logging, sys
import os
import requests

h = [
  logging.FileHandler('./logs/log.log'), 
  logging.StreamHandler(stream=sys.stdout),
]

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s',
  handlers=h,
)

logger = logging.getLogger(__name__)

# Comprobar si estoy en un contenedor Docker o en mi máquina local
AM_I_IN_A_DOCKER_CONTAINER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)

def main():
  r = requests.get('https://cristian-web.vercel.app/')
  logger.info('Hello World!')
  logger.info('Iniciando un ejercicio')
  # time.sleep(5)
  logger.info('Estatus del request: {}'.format(r.status_code))
  logger.info('37')
  logger.info('Terminando un ejercicio')
  logger.info('EStoy en un contenedor Docker: {}'.format(AM_I_IN_A_DOCKER_CONTAINER))


if __name__ == '__main__':
  main()
  