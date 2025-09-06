#!/usr/bin/env python3
"""
File operations for the voice generation tool.
"""

import sys
from typing import Any


def read_stdin() -> str:
    """
    Read text from standard input.
    
    Returns:
        str: Text read from standard input
        
    Raises:
        SystemExit: If no text is provided via stdin
    """
    text = sys.stdin.read().strip()
    if not text:
        print("Error: No text provided via stdin", file=sys.stderr)
        sys.exit(1)
    return text


def save_audio_file(audio_data: bytes, output_file: str) -> None:
    """
    Save audio data to a file.
    
    Args:
        audio_data: The audio data in binary format
        output_file: The path to the output file
        
    Raises:
        SystemExit: If there's an error saving the file
    """
    try:
        with open(output_file, 'wb') as f:
            f.write(audio_data)
        print(f"Audio saved to {output_file}")
    except IOError as e:
        print(f"Error saving file: {e}", file=sys.stderr)
        sys.exit(1)