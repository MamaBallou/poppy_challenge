import sys
import io
import subprocess
# Try to import the librosa library.
# Source: https://librosa.org/doc/latest/index.html
try:
    import librosa as lr
except ImportError:
    # If the librosa library is not installed, print an error message.
    print("The librosa library is not installed. Please install it using pip.")
    print("Command: pip install librosa")
    # Exit the program.
    sys.exit()
# Try to import the soundfile library.
# Source: https://pysoundfile.readthedocs.io/en/latest/
try:
    import soundfile as sf
except ImportError:
    # If the soundfile library is not installed, print an error message.
    print("The soundfile library is not installed. Please install it using pip.")
    print("Command: pip install soundfile")
    # Exit the program.
    sys.exit()
# Try to import the numpy library.
# Source: https://numpy.org/
try:
    from numpy import ndarray
except ImportError:
    # If the numpy library is not installed, print an error message.
    print("The numpy library is not installed. Please install it using pip.")
    print("Command: pip install numpy")
    # Exit the program.
    sys.exit()
# Try to import the youtube-dl library.
# Source: https://rg3.github.io/youtube-dl/
try:
    from youtube_dl import YoutubeDL
except ImportError:
    # If the youtube-dl library is not installed, print an error message.
    print("The youtube-dl library is not installed. Please install it using pip.")
    print("Command: pip install youtube-dl")
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
        # If the audio file is a MP3 file, convert it to a WAV file.
        if self.get_file_path().endswith(".mp3"):
            self.convert_to_wav()
        # If the path is a URL
        if self.is_URL():
            # If the path is a YouTube URL, download the video.
            if self.is_YouTube():
                self.dl_YouTube()
            # If the path is not a YouTube URL, print an error message.
            else:
                print("The path is not a YouTube URL.")

        # Load the audio file.
        y, self.sr = sf.read(self.get_file_path())
        self.y = y.T


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
        bpm = lr.beat.tempo(y=self.y, sr=self.sr)
        # While bpm is an ndarray, take the first element.
        while isinstance(bpm, ndarray):
            bpm = bpm[0]
        # Round the BPM to the nearest integer.
        bpm = int(round(bpm))
        # Return the BPM.
        return bpm

    def convert_to_wav(self):
        """
        This function will convert the audio file to a wav file.
        :return: None.
        """
        ini_file_path = self.get_file_path()
        # Change the file extension to wav.
        self.file_path = self.file_path.replace(".mp3", ".wav")
        # Tells the user that the file is being converted.
        print("Converting file...", end="")
        # Convert the audio file to a wav file.
        subprocess.call(["ffmpeg", "-y", "-i", ini_file_path, self.get_file_path()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Tells the user that the file has been converted.
        print(" Done!")

    def is_URL(self):
        """
        This function will check if the path is a URL.
        :return: True if the path is a URL, False if not.
        """
        # If the file path is a URL, return True.
        if self.get_file_path().startswith("http"):
            return True
        # If the file path is not a URL, return False.
        return False

    def is_YouTube(self):
        """
        This function will check if the path is a YouTube URL.
        :return: True if the path is a YouTube URL, False if not.
        """
        # If the file path is a YouTube URL, return True.
        if self.get_file_path().startswith("https://www.youtube.com"):
            return True
        # If the file path is not a YouTube URL, return False.
        return False
    
    def dl_YouTube(self):
        """
        This function will download the YouTube video.
        :return: None.
        """
        # Create a YoutubeDL object.
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'outtmpl': 'music.%(ext)s',
        }
        with YoutubeDL(ydl_opts) as ydl:
            # Download the video.
            ydl.download([self.get_file_path()])
            # Set the file path to the downloaded video.
            self.file_path = "./music.wav"


# If the script is run directly, run the main function.
if __name__ == "__main__":
    # Check if the correct number of arguments are given.
    if len(sys.argv) != 2:
        # If not, print an error message.
        print("Please give the path to the audio file.")
        # Exit the program.
        sys.exit()
    
    # Create a new Music object.
    music = Music(sys.argv[1])

    print("Calculate BPM... ", end="")
    # Print the BPM.
    print(music.get_bpm())
