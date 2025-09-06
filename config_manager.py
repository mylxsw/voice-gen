#!/usr/bin/env python3
"""
Configuration management for the voice generation tool.
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv


def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables.
    
    Returns:
        Dict[str, Any]: Configuration dictionary
        
    Raises:
        ValueError: If required environment variables are not set
    """
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Validate required environment variables
    required_vars = [
        'VOICE_GEN_API_GROUP_ID', 
        'VOICE_GEN_API_KEY'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Build configuration dictionary
    config = {
        'api': {
            'base_url': os.getenv('VOICE_GEN_API_BASE_URL', 'https://api.minimax.chat/v1/t2a_v2'),
            'group_id': os.getenv('VOICE_GEN_API_GROUP_ID'),
            'api_key': os.getenv('VOICE_GEN_API_KEY')
        },
        'defaults': {
            'output_file': os.getenv('VOICE_GEN_DEFAULT_OUTPUT_FILE', 'result.mp3'),
            'model': os.getenv('VOICE_GEN_DEFAULT_MODEL', 'speech-2.5-hd-preview'),
            'voice_id': os.getenv('VOICE_GEN_DEFAULT_VOICE_ID', 'mylxsw_voice_1')
        },
        'audio_settings': {
            'sample_rate': int(os.getenv('VOICE_GEN_AUDIO_SAMPLE_RATE', '32000')),
            'bitrate': int(os.getenv('VOICE_GEN_AUDIO_BITRATE', '128000')),
            'format': os.getenv('VOICE_GEN_AUDIO_FORMAT', 'mp3')
        }
    }
    
    return config