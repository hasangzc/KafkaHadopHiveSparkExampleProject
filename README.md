# KafkaHadopHiveSparkExampleProject
Get data. Submit a Kafka topic. Get it with Spark from Topic. Save to HDFS and Apache Hive!

## Project Steps;
- Get data from https://trends.google.com/trends/trendingsearches/daily?geo= web site 

About Data:
  Get today's Google trending search results.
  
  Features;
    
    - title: Search title
    
    - subtitle: subtitle about search
    
    - source: source of search
    
    - time_published
    
    - searches: Number of search about this title
    

Apache Kafka, Apache Spark, Hadoop, Apache Hive, python3 are used in this project.

Therefore, these technologies must be installed on your system. Simply for this;

* I installed Ubuntu virtual machine on my machine. You can use UTM or Orecla VM for this, depending on your system.
* Install python3 your system.

* From https://kafka.apache.org/downloads website you can download Kafka your system. But You must have Java installed on your system. If not, install Java first.

* Install Hadoop your system from https://hadoop.apache.org/releases.html website. After this you have to add your env variables in .bashrc file on Linux.
* Add your configs in hadoop-env.sh  
* Edit core-site.xml and hdfs-site.xml files.

* Install Apache Hıve from https://hive.apache.org/downloads.html
* Add env variables to .bashrc file
* Edit hive-env.sh and hive-site.xml

* Install Spark from https://spark.apache.org/downloads.html website. For Spark, Scala must be installed on the system. 
* Add env variables to .bashrc file


## Run Code

* Terminal 1: -- Zookeeper
```bin/zookeeper-server-start.sh config/zookeeper.properties```

* Terminal2: -- Kafka Broker
```bin/kafka-server-start.sh config/server.properties```

