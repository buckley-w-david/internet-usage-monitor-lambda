# Internet Usage Monitor - AWS Lambda Deployment

Deployment based on [this article](https://hackernoon.com/running-selenium-and-headless-chrome-on-aws-lambda-layers-python-3-6-bd810503c6c3), with changes to the configuration inspired by [this post](http://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python/).

 * serverless-chrome(headless-chromium): v1.0.0-55
 * ChromeDriver: v2.42
 * Selenium for Python: v3.14.1


## Prerequisits
 * Serverless Framework

## Setup

### The Selenium Lambda Layers

Initialize selenium, headless chrome, and the chrome driver
```bash
 $ pip3.6 install -t seleniumLayer/selenium/python/lib/python3.6/site-packages selenium==3.14.1
 $ mkdir -p seleniumLayer/chromedriver
 $ cd seleniumLayer/chromedriver
 $ wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip
 $ unzip chromedriver_linux64.zip
 $ wget https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip
 $ unzip stable-headless-chromium-amazonlinux-2017-03.zip
 $ rm chromedriver_linux64.zip stable-headless-chromium-amazonlinux-2017-03.zip
 $ cd ../..
```

Deploy the Selenium Layers
```bash
 $ sls deploy
```

---

### The Lambda Function

Download the internet usage monitoring package
```bash
 $ cd lambda
 $ git clone https://github.com/buckley-w-david/internet-usage-monitor.git
```

Install the serverless-package-external plugin
```bash
 $ npm i serverless-package-external --save-dev
```

Deploy the package
```bash
 $ sls deploy
```

Next you'll need to configure the environment variables on the lambda function with the credentials needed to run the application.

The required variables are:
 * XPLORNET_USERNAME
 * XPLORNET_PASSWORD
 * EMAIL_SERVER
 * EMAIL_USERNAME
 * EMAIL_PASSWORD
 * EMAIL_SENDER
 * EMAIL_RECIPIENTS
