# Voice Generator

A command-line tool to generate audio from text using the Minimax AI API.

## Usage

```bash
echo "hello, world" | voice-gen --output result.mp3 --model speech-2.5-hd-preview --voice-id mylxsw_voice_1
```

### Parameters

- `--output`, `-o`: Output file name (default: `result.mp3`)
- `--model`, `-m`: Model to use (default: `speech-2.5-hd-preview`)
- `--voice-id`, `-v`: Voice ID to use (default: `mylxsw_voice_1`)

### Examples

```bash
# Using default parameters
echo "Hello, world" | voice-gen

# Specifying output file
echo "Welcome to our service" | voice-gen --output welcome.mp3

# Using a different model and voice
echo "This is a test" | voice-gen --model speech-2.0 --voice-id another_voice --output test.mp3
```

## Installation

1. Make sure you have Python 3 installed
2. Install the required dependencies:
   ```bash
   pip3 install --break-system-packages -r requirements.txt
   ```
3. Create a `.env` file with your configuration:
   ```bash
   cp .env.example .env
   # Edit .env with your actual API credentials
   ```
4. Make the script executable:
   ```bash
   chmod +x voice-gen
   ```

## Configuration

The tool uses environment variables for configuration. Create a `.env` file in the project root with the following variables:

### Required Variables
- `VOICE_GEN_API_GROUP_ID`: Your API group ID
- `VOICE_GEN_API_KEY`: Your API key

### Optional Variables (with defaults)
- `VOICE_GEN_API_BASE_URL`: The Minimax API base URL (default: `https://api.minimax.chat/v1/t2a_v2`)
- `VOICE_GEN_DEFAULT_OUTPUT_FILE`: Default output filename (default: `result.mp3`)
- `VOICE_GEN_DEFAULT_MODEL`: Default model (default: `speech-2.5-hd-preview`)
- `VOICE_GEN_DEFAULT_VOICE_ID`: Default voice ID (default: `mylxsw_voice_1`)
- `VOICE_GEN_AUDIO_SAMPLE_RATE`: Audio sample rate (default: `32000`)
- `VOICE_GEN_AUDIO_BITRATE`: Audio bitrate (default: `128000`)
- `VOICE_GEN_AUDIO_FORMAT`: Audio format (default: `mp3`)

Example `.env` file:
```env
VOICE_GEN_API_GROUP_ID=your_group_id
VOICE_GEN_API_KEY=your_api_key
```

## Code Structure

The refactored code follows software engineering best practices with a modular design:

- `voice_gen.py`: Main entry point
- `voice_generator.py`: Handles communication with the Minimax AI API
- `argument_parser.py`: Handles command-line argument parsing
- `file_operations.py`: Handles file I/O operations
- `config_manager.py`: Manages configuration loading from environment variables
- `.env`: Environment variables configuration file
- `test_voice_gen.py`: Unit tests for the components

## How It Works

The script reads text from standard input and sends it to the Minimax AI API to generate speech audio. The API returns hex-encoded audio data which is then converted to binary and saved as an MP3 file. API credentials and settings are loaded from environment variables (via `.env` file).