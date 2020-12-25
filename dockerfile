#Use existing docker image as a base
FROM pytorch/pytorch:latest

#Download and install dependencies
RUN export python=python3
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools

#RUN pip install torch===1.7.0+cu110 torchvision===0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install gym
RUN pip install box2d
RUN pip install wandb
RUN pip install argparse


# Container start command
CMD ["sh"]


#command to build new image:
#sudo docker build -t peterpirogtf/dqn_naf:latest .

#How to push docker image to hub

#login by:
# docker login
# docker push peterpirogtf/dqn_naf:latest
#https://stackoverflow.com/questions/41984399/denied-requested-access-to-the-resource-is-denied-docker