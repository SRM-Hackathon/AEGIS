FROM ubuntu:16.04

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install openssh-server -y

RUN echo "Port 22222" >> /etc/ssh/sshd_config

RUN apt-get install iptables sudo -y

RUN adduser --disabled-password user1 && adduser user1 sudo

CMD iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222

CMD iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-port 2223

RUN service ssh start 

RUN apt-get install -y git python-virtualenv libssl-dev libffi-dev build-essential libpython-dev python2.7-minimal authbind

RUN sudo apt-get -y install python3-pip,

RUN adduser --disabled-password cowrie

RUN su - cowrie

RUN git clone http://github.com/micheloosterhof/cowrie

RUN cd cowrie

RUN virtualenv cowrie-env

RUN cd cowrie-env

CMD source bin/activate

# CMD pip list
# RUN /bin/bash -c "source bin/activate

CMD pip install --upgrade pip

RUN pip install -U -r requirements.txt

# CMD cd ../cowrie/etc/

RUN ["cp","/cowrie/etc/cowrie.cfg.dist", "/cowrie/etc/cowrie.cfg"]

RUN echo "hostname = testserver5" >> /cowrie/etc/cowrie.cfg

RUN echo "enabled = true" >> /cowrie/etc/cowrie.cfg

# RUN cd ../

# CMD bin/cowrie start

# EXPOSE 2222

# EXPOSE 2223

CMD ["/usr/sbin/sshd", "-D"]

# CMD exec "$@"
