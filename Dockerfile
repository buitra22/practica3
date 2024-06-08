FROM jenkins/inbound-agent:latest-alpine as agent

FROM alpine:3.20.0

# Instalar herramientas necesarias
RUN apk -U add openjdk11-jre docker git make python3 py3-pip

# Copiar archivos del agente de Jenkins
COPY --from=agent /usr/local/bin/jenkins-agent /usr/local/bin/jenkins-agent
COPY --from=agent /usr/share/jenkins/agent.jar /usr/share/jenkins/agent.jar

# Establecer el directorio de trabajo
RUN mkdir -p /opt/calc
WORKDIR /opt/calc

# Establecer el punto de entrada para el agente de Jenkins
ENTRYPOINT ["/usr/local/bin/jenkins-agent"]
