# Parallel Data Search with Hadoop (Keyword Detection in Large E-books)
## Project Overview
This project involves the development of a distributed system using the Hadoop ecosystem to perform keyword detection across large e-book datasets. The system leverages the power of Hadoop's MapReduce and distributed storage (HDFS) to process and analyze text data in parallel, ensuring fast and efficient search results even with large data volumes.

The implementation is carried out using Docker to create a multi-container environment simulating a Hadoop cluster, with one master node and two worker nodes. The project follows a practical approach to Big Data processing using open-source tools.

## Objectives
The primary objective is to design and implement a distributed system that efficiently searches for specific keywords within a large collection of e-books stored in HDFS. The system supports:

* **Keyword detection** across multiple documents
* **Parallel processing** using the MapReduce paradigm
* Easy **scalability** and **fault tolerance** through Hadoop

## Technologies Used
* **Hadoop** (MapReduce, HDFS)
* **Docker** (for containerized environment setup)
* **Python** (Mapper and Reducer scripts)
* **Git Bash / PowerShell** (command-line interfaces)

## Project Architecture
The project follows a distributed architecture with the following setup:

* **Docker-based cluster**: A Docker environment simulates a Hadoop cluster with one master node (NameNode) and two worker nodes (DataNodes).
* **HDFS**: Distributed storage for e-books (input data).
* **MapReduce**: For parallel processing of the data to find and count occurrences of specific keywords.

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/anassYinssi/hadoop-keyword-search.git
cd parallel-data-search-hadoop
```
### 2. Docker Environment Setup
Pull the Hadoop cluster image from Docker Hub:

```
docker pull stephanederrode/docker-cluster-hadoop-spark-python:3.2
```
For 16GB RAM, use:

```
docker pull stephanederrode/docker-cluster-hadoop-spark-python-16:3.2
```
For 8GB RAM, use:

```
docker pull stephanederrode/docker-cluster-hadoop-spark-python-8:3.2
```
Create a network for the containers:

```
docker network create --driver=bridge hadoop
```
### 3. Start the Hadoop Cluster

```
docker run -itd --net=hadoop -p 9870:9870 -p 8088:8088 -p 7077:7077 --name hadoop-master --hostname hadoop-master stephanederrode/docker-cluster-hadoop-spark-python-16:3.2
docker run -itd --net=hadoop --name hadoop-slave1 --hostname hadoop-slave1 stephanederrode/docker-cluster-hadoop-spark-python-16:3.2
docker run -itd --net=hadoop --name hadoop-slave2 --hostname hadoop-slave2 stephanederrode/docker-cluster-hadoop-spark-python-16:3.2
```
### 4. Access the Master Node
```
docker exec -it hadoop-master bash
```
### 5. Format HDFS and Start Hadoop
```
/usr/local/hadoop/bin/hdfs namenode -format
./start-hadoop.sh
```
### 6. Upload Data to HDFS
Create an input directory and upload the e-books:

```
hadoop fs -mkdir -p input
hadoop fs -put /path/to/ebooks/* input
```
### 7. Run the MapReduce Job
Ensure the mapper.py and reducer.py scripts are in place. Launch the job:

```
hadoop jar $STREAMINGJAR -files /path/to/mapper.py,/path/to/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input input/* -output output
```
Or, forcing the two clusters during the Reduce phase:
```
hadoop jar $STREAMINGJAR -D mapred.reduce.tasks=2 -files /path/to/mapper.py,/path/to/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input input/* -output output
```
### 8. View the Results
List the output directory:

```
hadoop fs -cat output/part-00000
```
If the second command is run, you will retrieve two output directories:

```
hadoop fs -cat output/part-00000
hadoop fs -cat output/part-00001
```
### Results and Conclusion
This project demonstrates how Hadoop can efficiently process and search large datasets in parallel. The results of the MapReduce job provide valuable insights into the frequency and occurrence of keywords within the dataset, making this approach suitable for large-scale text analysis tasks.

## Commands Cheat Sheet
* **Start Containers**: docker start hadoop-master hadoop-slave1 hadoop-slave2
* **Access NameNode**: docker exec -it hadoop-master bash
* **List HDFS Content**: hadoop fs -ls
* **View Output**: hadoop fs -cat output/part-00000 and (hadoop fs -cat output/part-00001) if there is two outputs
* **Stop Containers**: docker stop hadoop-master hadoop-slave1 hadoop-slave2
