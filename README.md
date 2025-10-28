# Sustainable Stock Watcher

## Project Description and Goals
This project fetches data on green energy stocks using the Alpha Vantage API, processes it with Pandas for analysis, and generates reports. It uses DVC for data versioning and Git for code versioning to ensure reproducible financial insights.

Goals:
- Monitor sustainable stocks (e.g., TSLA, FSLR) for trends like price changes and volatility.
- Provide automated, versioned workflows for reliable analysis.
- Demonstrate best practices in data pipelines and reproducibility.

## Prerequisites
- Python 3.x
- Git installed
- An Alpha Vantage API key (free tier sufficient)

## Setup Instructions
1. Clone the repository:
git clone https://github.com/adi-kaden/sustainable-stock-watcher.git
cd sustainable-stock-watcher

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
text3. Install dependencies:
pip install requests pandas dvc python-dotenv  # Add more if needed, e.g., matplotlib
text4. Set up DVC:
dvc init
dvc remote add -d local ./dvc_cache  # For local storage; customize if using cloud
text## How to Get an Alpha Vantage API Key
1. Sign up at https://www.alphavantage.co/support/#api-key.
2. Copy your free API key.
3. Create a `.env` file in the project root:
ALPHA_VANTAGE_API_KEY=your_api_key_here
text(This file is ignored by .gitignore for security.)

## How to Run the DVC Pipeline
1. Pull any versioned data (if applicable):
dvc pull
text2. Run the pipeline:
dvc repro
textThis automates:
- Fetching data via `python stock-watcher.py fetch` (or your mode).
- Processing with Pandas.
- Generating reports in `reports/`.

If params change (e.g., in params.yaml), DVC will rerun affected stages.

## Example Output
After running `dvc repro`, check `reports/analysis_report.csv` for a sample report. It might include columns like:
- Date
- Ticker
- Closing Price
- 7-Day Moving Average
- Volatility

Example snippet (from a CSV):
Date,Ticker,Close,Moving_Avg,Volatility
2023-10-01,TSLA,250.00,245.00,5.2
2023-10-02,TSLA,252.00,246.50,4.8
text## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork and submit pull requests. For issues, open a GitHub issue.

## Acknowledgments
- Alpha Vantage for the API.
- DVC for data versioning.