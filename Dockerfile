FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git sudo \
    curl \
    wget \
    golang-go \
    build-essential \
    ca-certificates \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN go version

RUN GOBIN=/usr/local/bin go install gotest.tools/gotestsum@latest

ENV GOPATH=/home/ubuntu/go
ENV GOCACHE=/home/ubuntu/.cache/go-build
ENV PATH=$PATH:$GOPATH/bin:/usr/local/go/bin

RUN mkdir -p $GOPATH $GOCACHE && \
    chmod -R 777 $GOPATH $GOCACHE

COPY . /evaluation
WORKDIR /evaluation
RUN pip install --break-system-packages -e . --no-cache-dir

RUN git config --system user.email "agent@evaluation.local" && \
    git config --system user.name "Evaluation Agent" && \
    git config --system --add safe.directory '*'

WORKDIR /home/ubuntu
RUN git clone https://github.com/tektoncd/pipeline.git /home/ubuntu/repo

WORKDIR /home/ubuntu/repo
ENV GOFLAGS="-mod=vendor"
RUN go build ./... || true

RUN mkdir -p /evaluation/secure_git && \
    mv /home/ubuntu/repo/.git /evaluation/secure_git/repo.git && \
    chown -R root:root /evaluation/secure_git && \
    chmod -R 700 /evaluation/secure_git

RUN find /home/ubuntu/repo -name ".git" -type d -exec rm -rf {} + 2>/dev/null || true && \
    find /home/ubuntu/repo -name ".git" -type f -delete 2>/dev/null || true

RUN chown -R ubuntu:ubuntu /home/ubuntu/repo && \
    chown -R ubuntu:ubuntu /home/ubuntu/.cache

ENV SECURE_GIT_DIR=/evaluation/secure_git/repo.git
ENV REPO_PATH=/home/ubuntu/repo
ENV HOME=/home/ubuntu
ENV MCP_TESTING_MODE=1

WORKDIR /home/ubuntu
CMD ["hud_eval"]