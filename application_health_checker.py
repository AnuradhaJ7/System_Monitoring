import requests
import logging

# Set up logging
logging.basicConfig(filename='application_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Application URL
APPLICATION_URL = 'http://your-application-url.com'  #here we need to add our app link

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f'Application is up. HTTP Status Code: {response.status_code}')
            print('Application is up.')
        else:
            logging.warning(f'Application might be down. HTTP Status Code: {response.status_code}')
            print('Application might be down.')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error checking application health: {e}')
        print('Application is down.')

def main():
    check_application_health(APPLICATION_URL)

if __name__ == "__main__":
    main()
