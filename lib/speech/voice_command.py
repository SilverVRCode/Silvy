"""
Basic interface for voice command detection
"""

class VoiceCommand:
    def __init__(self, mic):
        self.mic = mic

    def listen(self):
        """
        Capture audio and detect wake word
        Returns: raw audio data or None
        """
        # TODO: integrate with speech recognition library
        return None
