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

tech stack: dbt, docker, bigquery, ec2, kafka , python, mage
