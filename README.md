# weatherapp
The app supports the following features:

1. Read in CSV file, output JSON
2. Responds to GET request with the output in JSON
3. Querying on the data:
   
   a. Limit results to a number http://weather_app:80/query?limit=5
         - By date: http://weather_app:80/query?date=2012-06-04
         - By weather type: http://weather_app:80/query?weather=rain
   
   b. Create multi-query filtering, eg. http://weather_app:80/query?weather=rain&limit=5

Tools Used:
1. Python-based Flask framework
2. Docker for app containerization
3. AWS Beanstalk for hosting the web application
4. GitHub Actions to publish docker images to AWS ECR and DockerHub


Web Link - http://weather-app-env.eba-nmhmcepr.us-east-2.elasticbeanstalk.com/

