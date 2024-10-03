# Parallel Data Search with Hadoop (Keyword Detection in Large E-books)
## Project Overview
This project involves the development of a distributed system using the Hadoop ecosystem to perform keyword detection across large e-book datasets. The system leverages the power of Hadoop's MapReduce and distributed storage (HDFS) to process and analyze text data in parallel, ensuring fast and efficient search results even with large data volumes.

The implementation is carried out using Docker to create a multi-container environment simulating a Hadoop cluster, with one master node and two worker nodes. The project follows a practical approach to Big Data processing using open-source tools.

## Objectives
The primary objective is to design and implement a distributed system that efficiently searches for specific keywords within a large collection of e-books stored in HDFS. The system supports:

**- Keyword detection across multiple documents**
**-Parallel processing using the MapReduce paradigm**
**-Easy scalability and fault tolerance through Hadoop**

## Technologies Used
**-Hadoop (MapReduce, HDFS)**
**-Docker (for containerized environment setup)**
**-Python (Mapper and Reducer scripts)**
**-Git Bash / PowerShell (command-line interfaces)**
**-Project Architecture**
The project follows a distributed architecture with the following setup:

Docker-based cluster: A Docker environment simulates a Hadoop cluster with one master node (NameNode) and two worker nodes (DataNodes).
HDFS: Distributed storage for e-books (input data).
MapReduce: For parallel processing of the data to find and count occurrences of specific keywords.
