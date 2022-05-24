import signal

class SignalHandler:
    KEEP_ALIVE = True
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        print("Exiting gracefully")
        self.KEEP_ALIVE = False
