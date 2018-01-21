FROM ros:kinetic-robot-xenial
ARG ROBOT
ARG IAMROBOT=true
ARG INSTALL_TYPE=full
ENV TERM xterm
ENV ROBOTIC_PATH /var/robotics/
WORKDIR ${ROBOTIC_PATH}/compsys/

RUN apt-get -y update && apt-get install -y git openssh-server sudo

COPY packages/ packages/
COPY update .
RUN ./update

COPY setup/ setup/
RUN ./setup/zsh/install

ENV ROBOT ${ROBOT}
ENV IAMROBOT ${IAMROBOT}
RUN ./setup/config/install

RUN git config --global push.default simple && \
  git config --global url.'https://github.com/'.insteadOf 'git@github.com:' && \
  git config --global credential.helper 'cache --timeout=1800'
WORKDIR ${ROBOTIC_PATH}/${ROBOT}
COPY tmp/${ROBOT} .
RUN INSTALL_TYPE=${INSTALL_TYPE} ./setup.sh
RUN rm -rf /var/lib/apt/lists/*

WORKDIR ${ROBOTIC_PATH}/${ROBOT}/catkin_ws
RUN catkin build && source ../robotrc && build_sitl

COPY scripts/ compsys/scripts/

WORKDIR ${ROBOTIC_PATH}/${ROBOT}
EXPOSE 11345
ENTRYPOINT [ "/bin/zsh" ]
