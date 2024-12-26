from gtts import gTTS
import os

def text_to_audio(text, output_file='output.mp3'):
    """
    Convert text to speech and save it as an audio file.

    Parameters:
    - text (str): The text to convert to speech.
    - language (str): The language for the speech (default: 'en').
    - output_file (str): The output audio file name (default: 'output.mp3').

    Returns:
    - str: Path to the generated audio file.
    """
    try:
        # Create TTS object
        tts = gTTS(text=text, lang=language)
        
        # Save the audio file
        tts.save(output_file)
        print(f"Audio file saved as {output_file}")
        return output_file
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    user_text = "Hello world"
    language = 'en'
    output_path = text_to_audio(user_text, language)
    
    if output_path:
        # Play the audio file (optional, for Windows)
        os.system(f'start {output_path}')
