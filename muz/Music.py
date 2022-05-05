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


# Now we will make a class "Music" that will load the audio file, calculate the BPM, convert the audio file if not in compatible format and play the music.

class Music:
    """
    This class will load the audio file, calculate the BPM, convert the audio file if not in compatible format and play the music.
    """
    def __init__(self, file_path):
        """
        This function will load the audio file, calculate the BPM, convert the audio file if not in compatible format and play the music.
        :param file_path: The path to the mp3 file.
        """
        self.file_path = file_path
        # Load the audio file.
        self.load_file()

    def load_file(self):
        """
        This function will load the audio file.
        :return: None.
        """
        # Load the audio file.
        self.y, self.sr = librosa.load(self.file_path)

    def get_file_path(self):
        """
        This function will return the file path.
        :return: The file path.
        """
        # Return the file path.
        return self.file_path

    def get_bpm(self):
        """
        This function will calculate the BPM of the song.
        The song will be read in from an audio file.
        The BPM will be calculated using the BPM algorithm.
        The BPM will be rounded to the nearest integer.
        :return: The BPM of the song.
        """
        # Calculate the BPM.
        bpm = librosa.beat.tempo(y=self.y, sr=self.sr)
        # Round the BPM to the nearest integer.
        bpm = int(round(bpm[0]))
        # Return the BPM.
        return bpm

    def play(self):
        """
        This function will play the song.
        :return: None.
        """
        # Play the song.
        librosa.output.play_wav(self.y, self.sr)

    def convert_to_wav(self):
        """
        This function will convert the audio file to a wav file.
        :return: None.
        """
        # Change the file extension to wav.
        self.file_path = self.file_path.replace(".mp3", ".wav")
        # Convert the audio file to a wav file.
        librosa.output.write_wav(self.file_path, self.y, self.sr)


# If the script is run directly, run the main function.
if __name__ == "__main__":
    # Check if the correct number of arguments are given.
    if len(sys.argv) != 2:
        # If not, print an error message.
        print("Please give the path to the audio file.")
        # Exit the program.
        sys.exit()
    
    print("Load Music... ", end="")
    # Create a new Music object.
    music = Music(sys.argv[1])
    print("Done")

    # If the audio file is a MP3 file, convert it to a WAV file.
    if music.get_file_path().endswith(".mp3"):
        print("Convert to WAV... ", end="")
        music.convert_to_wav()
        print("Done")
        print("Load Music... ", end="")
        # Load the audio file.
        music.load_file()
        print("Done")

    print("Calculate BPM... ", end="")
    # Print the BPM.
    print(music.get_bpm())
    # Play the song.
    # music.play()