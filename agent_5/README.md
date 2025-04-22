# Content Creator Analyzer

A simple web application to analyze content creators' social media performance across YouTube and TikTok platforms and provide optimization suggestions.

## Features

- Analyze YouTube and TikTok accounts using only the account names
- View key performance metrics for each platform
- Receive tailored optimization suggestions based on the analysis
- Generate professional presentations of your analysis results

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/content-creator-analyzer.git
cd content-creator-analyzer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set up environment variables for presentation generation:
```bash
export SLIDESGPT_API_KEY=your_api_key_here
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Enter your YouTube channel name and/or TikTok username in the input fields

4. Click "Analyze" to retrieve and analyze your social media statistics

5. Review your performance metrics and optimization suggestions

6. (Optional) Click "Generate Presentation" to create a professional presentation of your analysis results

## Project Structure

- `main.py`: Main application file with Streamlit UI
- `get_info.py`: Module for retrieving and analyzing social media statistics
- `presentation.py`: Module for generating presentations based on the analysis results
- `requirements.txt`: List of required Python packages

## Limitations

- The analysis is based on publicly available data from SocialBlade
- API usage for presentation generation requires a valid API key
- The accuracy of suggestions depends on the quality of available data

## Future Improvements

- Add support for more social media platforms (Instagram, Twitter, etc.)
- Implement more detailed content analysis (video topics, hashtags, etc.)
- Provide historical performance trends and growth predictions
- Enhance presentation customization options

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the web application framework
- [SocialBlade](https://socialblade.com/) for providing social media statistics
- [SlidesGPT](https://slidesgpt.com/) for presentation generation capabilities (Note: Replace with actual API service)