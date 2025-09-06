#!/usr/bin/env python3
"""
Voice generation tool that converts text to speech using the Minimax AI API.
"""

import sys
import os

# Add the current directory to the Python path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config_manager import load_config
from argument_parser import parse_arguments
from file_operations import read_stdin, save_audio_file
from voice_generator import VoiceGenerator, VoiceGeneratorError


def main():
    """Main entry point for the voice generation tool."""
    try:
        # Load configuration
        config = load_config()
        
        # Parse command line arguments
        args = parse_arguments(config)
        
        # Read text from stdin
        text = read_stdin()
        
        # Initialize voice generator
        generator = VoiceGenerator(config)
        
        # Generate voice
        audio_data = generator.generate_voice(
            text=text,
            model=args.model,
            voice_id=args.voice_id
        )
        
        # Save audio file
        save_audio_file(audio_data, args.output)
        
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    except VoiceGeneratorError as e:
        print(f"Voice generation error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()