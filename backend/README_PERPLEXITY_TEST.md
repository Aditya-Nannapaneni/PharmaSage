# Perplexity API Test Script

This script allows you to test the Perplexity API directly and save the response to a file for analysis.

## Features

- Tests the Perplexity API with a custom prompt
- Saves the full API response to a JSON file
- Analyzes and logs key information from the response
- Supports both real API calls and mock responses
- Flexible configuration via command-line arguments or .env file

## Prerequisites

- Python 3.6+
- Required Python packages:
  - requests
  - python-dotenv

## Installation

1. Make sure you have Python installed
2. Install required packages:
   ```
   pip install requests python-dotenv
   ```

## Usage

### Basic Usage

```bash
python test_perplexity_api.py
```

This will:
1. Look for a Perplexity API key in the `.env` file
2. If not found, prompt you to enter one
3. Send a default prompt to the API
4. Save the response to a timestamped JSON file

### Command-line Arguments

```bash
python test_perplexity_api.py --api-key YOUR_API_KEY --prompt "Your custom prompt" --output response.json
```

- `--api-key`: Your Perplexity API key (overrides .env file)
- `--prompt`: Custom prompt to send to the API
- `--output`: Custom filename for the response
- `--mock`: Use a mock response instead of calling the API

### Using Environment Variables

Create a `.env` file in the same directory with:

```
PERPLEXITY_API_KEY=your_api_key_here
USE_MOCK_RESPONSES=false  # Set to 'true' to use mock responses
```

## Response File

The response is saved as a JSON file with the following structure:

```json
{
  "id": "response-id",
  "model": "sonar-deep-research",
  "created": 1753779528,
  "usage": {
    "prompt_tokens": 1001,
    "completion_tokens": 2373,
    "total_tokens": 3374,
    "citation_tokens": 8834,
    "num_search_queries": 19,
    "reasoning_tokens": 220303
  },
  "citations": ["https://example.com", ...],
  "search_results": [...],
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "The response content..."
      }
    }
  ]
}
```

## Troubleshooting

- **API Key Issues**: Make sure your API key is valid and has the necessary permissions
- **Network Issues**: Check your internet connection and firewall settings
- **Rate Limiting**: The Perplexity API may have rate limits that could affect testing

## Examples

### Test with a custom prompt

```bash
python test_perplexity_api.py --prompt "Analyze the pharmaceutical company Pfizer and identify their main competitors"
```

### Use mock response for testing

```bash
python test_perplexity_api.py --mock
```

### Save response to a specific file

```bash
python test_perplexity_api.py --output pfizer_analysis.json
```

## Using the Response for Debugging

The saved response file can be used to:

1. Debug parsing issues in the main application
2. Understand the structure of the Perplexity API response
3. Compare responses from different prompts or API versions
4. Develop and test response parsing functions offline

To use a saved response file with the main application, you can modify the `perplexity_client.py` file to load responses from files during development.
