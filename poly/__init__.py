def has_cuda():
    import subprocess
    cuda_location = subprocess.run(["which", "nvcc"], capture_output=True)
    return cuda_location == []
