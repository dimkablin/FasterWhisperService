ARG CUDA_IMAGE="12.2.0-devel-ubuntu22.04"
FROM nvidia/cuda:${CUDA_IMAGE}

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git build-essential \
    python3 python3-pip gcc wget \
    ocl-icd-opencl-dev opencl-headers clinfo \
    libclblast-dev libopenblas-dev \
    && mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd && \
    apt-get install libcudnn8 libcudnn8-dev -y && \
    python3 -m pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "speech2text:app_whisper", "--host", "0.0.0.0", "--port", "8000", "--reload"]