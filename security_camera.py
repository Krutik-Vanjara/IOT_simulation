class SecurityCamera:
    def __init__(self, motion_detected=False):
        self.motion_detected = motion_detected  # Initially no motion

    def detect_motion(self):
        self.motion_detected = True
        print("Motion detected! Security Camera is recording.")
    
    def reset_motion(self):
        self.motion_detected = False
        print("No motion detected. Camera is idle.")
