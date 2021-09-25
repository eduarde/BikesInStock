# BikesInStock


Prerequisites:

1. Install python locally ( 3.7.3 ).
2. Create a Lambda function on AWS (choose python). (name to be used in step 7)
3. Create an event rule on AWS EventBridge as trigger.
 Ex of event schedule: cron(0/2 6-23 ? * * *)

Steps:

1. Install a virtualenv lib via:
```
 pip install virtualenv
```

2. Navigate to the root of this project.
3. Create a virtualenv (venv) via command:
```
virtualenv venv
```
4. Activate the virtualenv: 

linux:
```
source venv/bin/activate
```

win:
```
venv/Scripts/activate
```

5. Install requirements.
```
pip install -r requirments.txt
```

6. Prepare the deployment package for aws.
Readme: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

cd myvenv/lib/python3.8/site-packages
zip -r ../../../../my-deployment-package.zip .


7. Deploy and Update: (whenever you do code updates)
zip -g my-deployment-package.zip lambda_function.py
aws lambda update-function-code --function-name BikeCheck --zip-file fileb://my-deployment-package.zip