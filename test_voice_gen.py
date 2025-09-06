#!/usr/bin/env python3
"""
Unit tests for the voice generation tool components.
"""

import unittest
import os
import sys
import json

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config_manager import load_config
from argument_parser import parse_arguments
from voice_generator import VoiceGenerator, VoiceGeneratorError


class TestConfigManager(unittest.TestCase):
    """Test cases for the configuration manager."""
    
    def test_load_config(self):
        """Test that config can be loaded successfully."""
        config = load_config()
        self.assertIn('api', config)
        self.assertIn('defaults', config)
        self.assertIn('audio_settings', config)


class TestVoiceGenerator(unittest.TestCase):
    """Test cases for the voice generator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.config = load_config()
        self.generator = VoiceGenerator(self.config)
    
    def test_create_payload(self):
        """Test that payload is created correctly."""
        payload = self.generator._create_payload("test text", "test-model", "test-voice")
        self.assertEqual(payload['text'], "test text")
        self.assertEqual(payload['model'], "test-model")
        self.assertEqual(payload['timber_weights'][0]['voice_id'], "test-voice")
    
    def test_empty_text_raises_error(self):
        """Test that empty text raises an error."""
        with self.assertRaises(VoiceGeneratorError):
            self.generator.generate_voice("")


if __name__ == '__main__':
    unittest.main()