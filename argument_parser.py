#!/usr/bin/env python3
"""
Command line argument parsing for the voice generation tool.
"""

import argparse
from typing import Any


def parse_arguments(config: dict) -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Args:
        config: Configuration dictionary containing default values
        
    Returns:
        argparse.Namespace: Parsed arguments
    """
    defaults = config.get('defaults', {})
    
    parser = argparse.ArgumentParser(
        description='Generate voice from text using the Minimax AI API'
    )
    parser.add_argument(
        '--output', '-o',
        default=defaults.get('output_file', 'result.mp3'),
        help=f'Output file name (default: {defaults.get("output_file", "result.mp3")})'
    )
    parser.add_argument(
        '--model', '-m',
        default=defaults.get('model', 'speech-2.5-hd-preview'),
        help=f'Model to use (default: {defaults.get("model", "speech-2.5-hd-preview")})'
    )
    parser.add_argument(
        '--voice-id', '-v',
        dest='voice_id',
        default=defaults.get('voice_id', 'mylxsw_voice_1'),
        help=f'Voice ID to use (default: {defaults.get("voice_id", "mylxsw_voice_1")})'
    )
    
    return parser.parse_args()