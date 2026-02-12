def push(kind):
    if kind == "queue_full":
        raise BufferError("QueueFull")
    if kind == "timeout":
        raise TimeoutError("PushTimeout")
    if kind == "invalid":
        raise ValueError("InvalidNotification")
