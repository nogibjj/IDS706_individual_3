# IDS706_individual_3
![CI](https://github.com/nogibjj/IDS706_individual_3/actions/workflows/ci.yml/badge.svg)

## Requirement

For this assignment, you will build a publicly accessible auto-scaling container using AWS Services and Flask. This is an easy way to build and deploy a scaleable web-hosted app and will allow you to apply your Flask knowledge from previous lessons.


## Installation

Download awscli:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Deploy
```bash
docker build -t chatbot:latest .
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 381492212823.dkr.ecr.us-east-1.amazonaws.com/chatbot
docker tag chatbot:latest 381492212823.dkr.ecr.us-east-1.amazonaws.com/chatbot
docker push 381492212823.dkr.ecr.us-east-1.amazonaws.com/chatbot
```

Run locally:
```bash
make install
make run
```

## Flask App

This app is designed to serve as a simple interface for a large language model, specifically utilizing the LLAMA 3B API to respond to customer inquiries. It aims to provide users with a seamless and efficient experience for obtaining accurate and contextually relevant answers to their questions. The app will act as a bridge between the powerful language model capabilities of LLAMA 3B and end-users, ensuring that interactions are intuitive, fast, and user-friendly. This functionality can be extended for various use cases such as customer support, information retrieval, or even interactive Q&A systems, depending on customer needs.

![img](./img/app.png)

## Use of DockerHub

I am using ECR as a replacement for DockerHub.

![ECR](./img/ECR.png)

## AWS Web App

I am using AWS App Runner to seamlessly deploy my container as a publicly accessible endpoint through the AWS Web App.

![Web Runner](./img/runner.png)

You can access the chatbot now at https://mk3zumewm2.us-east-1.awsapprunner.com/

![realchatbot](./img/chatbot.png)

## Video

Here is the video demo to this project.
[![Watch the video](https://img.youtube.com/vi/G56gl9GR-vI/0.jpg)](https://youtu.be/G56gl9GR-vI)