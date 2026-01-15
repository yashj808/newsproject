# NewsPulse - A Dynamic News Aggregator

## Description

NewsPulse is a Django-based web application that provides users with the latest news from various sources. It is designed to deliver the most up-to-date articles, with a smart fallback system to ensure that users always see relevant news. The application features a clean, user-friendly interface for browsing headlines from different genres.

## Features

- **Dynamic News Sources**: Users can select from a dropdown menu of news sources (e.g., TechCrunch, BBC News, CNN).
- **Time-Filtered News**: The application prioritizes news published in the last 4 hours.
- **Smart Fallback**: If no news is found for a selected source in the last 4 hours, it automatically displays the latest top headlines from across the US.
- **"Time Since" Display**: Shows how long ago an article was published in a human-readable format (e.g., "2 hours ago").
- **Direct Article Links**: Users can click on a news card's title or image to go directly to the original article page.
- **User-Friendly Interface**: A clean and simple UI built with Bootstrap.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **API**: [News API](https://newsapi.org/)
- **Programming Language**: Python

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

**1. Prerequisites:**

- Python 3.x
- pip (Python package installer)

**2. Clone the Repository:**

```bash
git clone <your-repository-url>
cd newsproject
```

**3. Create a Virtual Environment:**

It is recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

**4. Activate the Virtual Environment:**

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On macOS and Linux:**
  ```bash
  source venv/bin/activate
  ```

**5. Install Dependencies:**

Install all the required packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

**6. Get a News API Key:**

- Go to [https://newsapi.org/](https://newsapi.org/) and register to get a free API key.

**7. Configure the API Key:**

- Open the `newsapp/views.py` file.
- Find the line `newsapi = NewsApiClient(api_key='your_api_key_here')`.
- Replace `'your_api_key_here'` with the API key you obtained.

```python
# newsapp/views.py

def indec(request):
    # ...
    newsapi = NewsApiClient(api_key='YOUR_API_KEY') # <-- PASTE YOUR KEY HERE
    # ...
```
I have replaced the hardcoded API key with 'YOUR_API_KEY'. You will need to edit this file to add your own key.

**8. Run Migrations:**

```bash
python manage.py migrate
```

**9. Run the Development Server:**

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## Usage

- Open your web browser and navigate to `http://127.0.0.1:8000/`.
- Use the dropdown menu to select a news source.
- Click "Get News" to see the latest articles from that source.
- Click on any news card's title or image to read the full article on the original website.
- If no news is found for your selected source in the last 4 hours, you will be shown the latest top headlines from the US.
