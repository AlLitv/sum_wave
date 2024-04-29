
import numpy as np
from types import NoneType
from matplotlib import pyplot as plt

CHANNELS = 1  # моно
SAMPLE_RATE = 44000  # Гц
DURATION = 1  # Секунды
k_factor = 0.63


def read_tone_from_file():
    with open("tone.txt", "r") as file:
        return file.read().split('\n')


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq  # 2pi для преобразования в радианы
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


def main():
    tones = read_tone_from_file()
    mixed_tone = None
    for freq in tones:
        _, tone = generate_sine_wave(int(freq), SAMPLE_RATE, DURATION)
        if type(mixed_tone) == NoneType:
            mixed_tone = tone
        else:
            mixed_tone += tone * k_factor
    normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)
    plt.plot(normalized_tone[:1000])
    plt.show()


if __name__ == "__main__":
    main()
