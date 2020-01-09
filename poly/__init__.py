def has_cuda():
    import subprocess
    proc = subprocess.Popen(["which", "nvcc"], stdout=subprocess.PIPE)
    
    cuda_location = proc.communicate()[0].decode().strip()
    return cuda_location != ""
