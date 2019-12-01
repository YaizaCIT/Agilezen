pipeline {
   agent any
   stages {
      stage('Build') {
        steps {
         bat 'C:\\Users\\Rony\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe HelloPython.py'
        }
   }
   stage('Deploy') {
     steps {
       echo 'Deploying'
     }
   }
  }
}
