FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip git sudo \
    build-essential cmake ninja-build \
    libcurl4-openssl-dev libssl-dev libevent-dev zlib1g-dev \
    ccache \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/lib/ccache:$PATH"
ENV CCACHE_DIR=/home/ubuntu/.ccache

RUN echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu && \
    chmod 0440 /etc/sudoers.d/ubuntu

COPY . /evaluation
WORKDIR /evaluation
RUN pip install --break-system-packages -e .

WORKDIR /home/ubuntu

RUN git clone --recurse-submodules https://github.com/transmission/transmission.git repo

WORKDIR /home/ubuntu/repo

RUN mkdir -p build && cd build && \
    cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DENABLE_GTK=OFF -DENABLE_QT=OFF -DENABLE_MAC=OFF \
    -DENABLE_TESTS=ON \
    -DCMAKE_CXX_COMPILER_LAUNCHER=ccache \
    -DCMAKE_C_COMPILER_LAUNCHER=ccache ..

RUN chown -R ubuntu:ubuntu /home/ubuntu

RUN git config --system --add safe.directory '*'

ENV REPO_PATH=/home/ubuntu/repo
ENV MCP_TESTING_MODE=1
ENV HOME=/home/ubuntu

CMD ["hud_eval"]