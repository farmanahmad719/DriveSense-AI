import numpy as np
import wave


# Audio settings
sample_rate = 44100
duration = 3        # seconds

frequency1 = 800
frequency2 = 1200


# Time array
t = np.linspace(
    0,
    duration,
    int(sample_rate * duration),
    False
)


# Create siren effect
wave1 = np.sin(2 * np.pi * frequency1 * t)
wave2 = np.sin(2 * np.pi * frequency2 * t)


# Mix both tones
alarm = wave1 + wave2


# Normalize volume
alarm = alarm / np.max(np.abs(alarm))


# Convert to 16-bit audio
audio = np.int16(alarm * 32767)


# Save file
with wave.open("assets/alarm.wav", "w") as file:

    file.setnchannels(1)       # Mono
    file.setsampwidth(2)       # 16-bit
    file.setframerate(sample_rate)

    file.writeframes(
        audio.tobytes()
    )


print("Custom alarm created successfully!")