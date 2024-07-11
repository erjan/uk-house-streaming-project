# kafka-python==2.0.2
# jsonpatch==1.21
# jsonpointer==2.0
# jsonschema==3.2.0
# requests==2.31.0
# requests-oauthlib==2.0.0


#!/usr/bin/env python

from kafka import KafkaProducer

import time
import logging
import json
import requests

TOPIC = 'company_house'


producer = KafkaProducer(
    bootstrap_servers='splendid-goshawk-5336-us1-kafka.upstash.io:9092',
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username='c3BsZW5kaWQtZ29zaGF3ay01MzM2JDCzi5Tfmu0-6nTKYRO_seo8KHg2wJ4rH0k',
    sasl_plain_password='MmFkOWViYmItMGVjYi00MWI3LTlkNmYtYTYyZmZkMjNjZjA2'
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)


def on_send_success():
    logging.info('GOOD msg sent!')

def on_send_error():
    logging.info('BAD! msg not sent')

if __name__ == '__main__':

    url = "https://stream.companieshouse.gov.uk/"

    # # Parse the command line.
    # parser = ArgumentParser()
    # parser.add_argument('config_file', type=FileType('r'))
    # args = parser.parse_args()

    # # Parse the configuration.
    # config_parser = ConfigParser()
    # config_parser.read_file(args.config_file)
    # config = dict(config_parser['default'])

    # # Set idempotence configuration
    # config['enable.idempotence'] = 'true'

    # # Create Producer instance
    # producer = Producer(config)

    try:
        response=requests.get(
            url=url+"companies",
            headers={
                "Authorization": 'Basic OWU2MTU2NjYtZjY4Ny00MmY2LTliNWItZTlhZmJiOTliYjk0Og==',
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate"
            },
            stream=True
        )

        logging.info("Established connection to Company House UK streaming API")

        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')

                json_line = json.loads(decoded_line)

                # Build empty JSON
                company_profile = {
                    "company_name": None,
                    "company_number": None,
                    "company_status": None,
                    "date_of_creation": None,
                    "postal_code": None,
                    "published_at": None
                }

                try:
                    company_profile['company_name'] = json_line["data"]["company_name"]
                except KeyError:
                    company_profile['company_name'] = "NA"

                try:
                    company_profile['company_number'] = json_line["data"]["company_number"]
                except KeyError:
                    company_profile['company_number'] = "NA"
                
                try:
                    company_profile['company_status'] = json_line["data"]["company_status"]
                except KeyError:
                    company_profile['company_status'] = "NA"

                try:
                    company_profile["date_of_creation"] = json_line["data"]["date_of_creation"]
                except KeyError:
                    company_profile["date_of_creation"] = "NA"

                try:
                    company_profile["postal_code"] = json_line["data"]["registered_office_address"]["postal_code"]
                except KeyError:
                    company_profile["postal_code"] = "NA"

                try:
                    company_profile["published_at"] = json_line["event"]["published_at"]
                except KeyError:
                    company_profile["published_at"] = "NA"

                # Produce data to Kafka topics
                topics = {
                    TOPIC: company_profile,
                }

                # Optional per-message delivery callback
                def delivery_callback(err, msg):
                    if err:
                        logging.info('ERROR: Message failed delivery: {}'.format(err))
                    else:
                        logging.info("Produced event to topic {}: key = {} value = {}".format(
                            msg.topic(), msg.key(), msg.value()))

                # Produce data to Kafka topics
                for topic, message in topics.items():
                    # producer.produce(topic, key=json.dumps(message["company_number"]).encode('utf-8'), value=json.dumps(message).encode('utf-8')).add_callback(on_send_success).add_errback(on_send_error)
                    
                    try:
                        logging.info('sending..')
                        time.sleep(10)
                        producer.send(topic, key=json.dumps(message["company_number"]).encode('utf-8'), value=json.dumps(message).encode('utf-8'))
                    except Exception as e:
                        logging.info(f"tried to send but failed: {e}")

 


                # Block until the messages are sent.

    except Exception as e:
        logging.info(f"an error occurred {e}")



