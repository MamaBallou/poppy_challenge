"""
This file will be used to calculate the BPM of a song.
The song will be read in from an audio file.
The BPM will be calculated using the BPM algorithm.
The BPM will be rounded to the nearest integer.
This script supports one argument: the path to the mp3 file.
The format of the argument is:
    python MusicBPM.py <file_path>
"""


import sys
# Try to import the librosa library.
try:
    import librosa
except ImportError:
    # If the librosa library is not installed, print an error message.
    print("The librosa library is not installed. Please install it using pip.")
    print("Command: pip install librosa")
    # Exit the program.
    sys.exit()


def get_bpm(file_path):
    """
    This function will calculate the BPM of a song.
    The song will be read in from an audio file.
    The BPM will be calculated using the BPM algorithm.
    The BPM will be rounded to the nearest integer.
    This function supports one argument: the path to the mp3 file.
    The format of the argument is:
        python MusicBPM.py <file_path>
    :param file_path: The path to the mp3 file.
    :return: The BPM of the song.
    """
    # Read in the song.
    y, sr = librosa.load(file_path)
    # Calculate the BPM.
    bpm = librosa.beat.tempo(y=y, sr=sr)
    # Round the BPM to the nearest integer.
    bpm = int(round(bpm[0]))
    # Return the BPM.
    return bpm
    

# Example usage of the function.
if __name__ == '__main__':
    # Get the path to the audio file from the argument.
    file_path = sys.argv[1]
    # Calculate the BPM of the song.
    bpm = get_bpm(file_path)
    # Print the BPM.
    print(bpm)

