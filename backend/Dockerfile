# This image comes with the nvidia drivers and all the pip packages needed preinstalled
FROM binary141/ubuntu2204.nvidia:pip
CMD nvidia-smi

# ENV DEBIAN_FRONTEND=noninteractive
ENV remoteImageURL="https://coder.binary141.com/pics/"
ENV imageSaveLocation="/opt/stableDiffusion/"
# You need to sign up for a huggingface account and generate a token by going to huggingface.co/settings/tokens
ENV huggingFaceToken=""
ENV imageWidth="512"
ENV imageHeight="512"
ENV iterations="25"

# COPY requirements.txt ./

ENV imageWidth=512
ENV imageHeight=512

COPY server.py .
COPY stableDiffusion2.py .


EXPOSE 6969

CMD ["python3", "./server.py"]

