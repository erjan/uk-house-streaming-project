# uk-house-streaming-project

based on the tutorial https://arbenkqiku.github.io/create-end-to-end-kafka-streaming-pipeline


![Screenshot_86](https://github.com/user-attachments/assets/e2376caf-95da-4227-816e-5d129e836a01)


This is my replication of the pipeline from above, I used ec2 vs gcp and upstash vs confluent to make it more challenging.

Basic steps:

1.obtain api key on uk house service information website
2.test the api key and make sure it works with basic requests.get()
3.dockerize app and  write python code to produce to any kafka-service provider - confluent, upstash etc
4.consume from kafka cluster to data orchestrator - mage.ai
5.obtain bigquery service account auth key
5.do basic transform on data and send pandas dataframe to bigquery using the serv acc auth key
6.write DBT jobs to do transform and send back to prod dataset in bigquery

Mage screen:

![Screenshot_85](https://github.com/user-attachments/assets/61a7782c-2cbb-498d-a4bb-35a40bd134d7)


Docker producing data:

![Screenshot_87](https://github.com/user-attachments/assets/3328ca67-396f-416a-ad3b-793e86ec5bcc)


Bigquery:

![Screenshot_88](https://github.com/user-attachments/assets/b305e999-64ad-4f83-8f83-d8c42fab71c8)


DBT:

![Screenshot_89](https://github.com/user-attachments/assets/4155dc5f-dd25-432f-a78d-8d388e38289f)


dbt jobs:

![Screenshot_90](https://github.com/user-attachments/assets/4d28a508-be08-45f8-9525-b707cf0225be)

dbt prod scheduled runs:

![Screenshot_91](https://github.com/user-attachments/assets/ea313416-f7b7-4c7d-9e0f-52b912b7f88f)


tech stack: dbt, docker, bigquery, ec2, kafka , python, mage
