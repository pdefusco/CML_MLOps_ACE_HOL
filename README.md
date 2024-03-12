# CML MLOps Workshop

## About Cloudera Workshops

Cloduera Workshops are an initiative by Cloudera Solutions Engineering aimed at familiarizing CDP users with each Data Service. The content consists of a series of guides and exercises to quickly implement sample end-to-end use cases in the realm of Machine Learning, Datawarehousing, Data Engineering, Data Streaming and Operational Database.

The workshop is typically a three to four-hour event organized by Cloudera for CDP customers and prospects, where a small technical team from Cloudera Solutions Engineering provides cloud infrastructure for all participants and guides them through the completion of the labs with the help of presentations and open discussions.

This workshop is dedicated to Cloudera Machine Learning. CML is the CDP Data Service for machine learning and AI commonly in Private and Public Clouds. The content is primarily designed for machine learning engineers, data scientists, and cloud architects. However, little to no code changes are typically required and non-technical stakeholders such as project managers and analysts are encouraged to actively take part.

Workshops are open to all CDP users and customers. If you would like Cloudera to host an event for you and your colleagues please contact your local Cloudera Representative or submit your information [through this portal](https://www.cloudera.com/contact-sales.html). Finally, if you have access to a CDE Virtual Cluster you are welcome to use this guide and go through the same concepts in your own time.

## About the Cloudera Machine Learning (CML) Service

Cloudera Machine Learning (CML) is Cloudera’s platform for machine learning and AI. CML unifies self-service data science and data engineering in a single, portable service as part of an enterprise data cloud for multi-function analytics on data anywhere.

Large scale organizations use CML to build and deploy machine learning and AI capabilities for business at scale, efficiently and securely. CML is built for the agility and power of cloud computing, but can also operate inside your private and secure data center.

## About the Labs

This Hands On Lab is designed to walk you through the Services's main capabilities. Throughout the exercises you will complete a text classification use case and:

1. Use MLFLow Experiments to perform hyperparameter tuning at scale with Spark and PyTorch.
2. Learn about Iceberg's most popular features in the context of MLOps.
3. Use MLFlow Registry and CML APIv2 to build an MLOps pipeline.
4. Collaborate with other team members to maintain the promoted models and MLOps pipeline in a production-like environment.

## Step by Step Instructions

Detailed instructions are provided in the [step_by_step_guides](https://github.com/pdefusco/CML_MLOps_ACE_HOL/tree/main/step_by_step_guides/english) folder.

* [Link to the English Guide](https://github.com/pdefusco/CML_MLOps_ACE_HOL/tree/main/step_by_step_guides/english).

## Other CDP Workshops

CDP Data Services include Cloudera Machine Learning (CML), Cloudera Operational Database (COD), Cloudera Data Flow (CDF) and Cloudera Data Warehouse (CDW). Workshops are available for each of these CDP Data Services.

* [CDE Workshop](https://github.com/pdefusco/CDE119_ACE_WORKSHOP#cde-119-ace-hands-on-lab-workshop): Deploy an Ingestion, Transformation and Reporting pipeline with Spark 3.2. Learn about Iceberg's most popular features and orchestrate pipelines with Airflow. Use the CDE CLI and CDE Spark Submit Migration Tool to interact with CDE Virtual Clusters from your terminal.Finally, build a Python App leveraging the CDE API and monitor multiple CDE Virtual Clusters at the same time.
* [CDF Workshop](https://github.com/cloudera-labs/edge2ai-workshop): Build a full OT to IT workflow for an IoT Predictive Maintenance use case with: Edge Flow Management with MQTT and MiNiFi for data collection; Data Flow management was handled by NiFi and Kafka, and Spark Streaming with Cloudera Data Science Workbench (CDSW) model to process data. The lab also includes content focused on Kudu, Impala and Hue.
* [CDW Workshop](https://github.com/pdefusco/cdw-workshop): As a Big Data Engineer and Analyst for an Aeronautics corporation, build a Data Warehouse & Data Lakehouse to gain an advantage over your competition. Interactively explore data at scale. Create ongoing reports. Finally move to real-time analysis to anticipate engine failures. All using Apache Impala and Iceberg.
