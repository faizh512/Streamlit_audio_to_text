# Audio To Text

This Streamlit application converts audio files to text. Users can upload an MP3 audio file, and the app will process the audio to transcribe the spoken content into text. The application uses the `speech_recognition` library for transcription and the `pydub` library to handle audio processing and splitting.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Future Enhancements](#future-enhancements)

## Features

- Upload MP3 audio files for transcription.
- Automatically split long audio files into segments based on silence.
- Convert each audio segment into text using Google Speech Recognition.
- Display the transcribed text in a text area.
- Provide an option to download the transcribed text as a TXT file.

## Installation

To install and run the project on your local machine, follow these steps:
After running the app, use the "Upload your Audio" button to upload an MP3 audio file.
The app will display the uploaded audio and automatically split it into segments based on detected silence.
Each audio segment will be transcribed, and the transcribed text will be compiled into a single output.
You can view the transcribed text in the provided text area.
Click the "Download" button to download the transcribed text as a Transcript.txt file.

1. Clone this repository or download the zip file.
   
   ```bash
   git clone https://github.com/yourusername/audio-to-text.git
## Usage
1. After running the app, use the "Upload your Audio" button to upload an MP3 audio file.
2. The app will display the uploaded audio and automatically split it into segments based on silence.
3. Each audio segment will be transcribed, and the text will be compiled into a single output.
4. You can view the transcribed text in the provided text area.
5. Click the "Download" button to download the transcribed text as a Transcript.txt file.

## Dependencies
The project uses the following Python libraries:

- Streamlit: For creating the web application interface.
- speech_recognition: For converting speech to text.
- pydub: For audio processing and handling.
- pydub.silence: For detecting and splitting audio based on silence.

## Future Enhancements
1. Support for More Audio Formats: Extend support to additional audio formats (e.g., WAV, FLAC).

2. Improved Error Handling: Enhance error handling and user feedback for better user experience.

3. Text Formatting: Implement features to format and clean up the transcribed text for improved readability.

4. Batch Processing: Allow users to process multiple audio files at once.
