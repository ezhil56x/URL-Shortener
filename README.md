# URL Shortener

This is a simple URL shortener web application built with Flask and SQLite.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- Shortens long URLs to a shorter and more manageable format.
- Stores the original and shortened URLs in a SQLite database.
- Redirects users to the original URL when they visit the shortened URL.

## Prerequisites

Make sure you have the following prerequisites installed on your local machine

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Flask: Install Flask by running `pip install flask` in your command line or terminal.
- SQLite: SQLite comes bundled with Python by default, so no additional installation is required.

## Installation

1. Clone the repository

   ```shell
    git clone https://github.com/ezhil56x/URL-Shortener.git
   ```

2. Navigate to the cloned repository

   ```shell
    cd URL-Shortener
   ```

3. Run the following command to start the application

   ```shell
    flask run
   ```

   or

   ```shell
    python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000/`

## Usage

1. Enter the URL you want to shorten in the text box and click on the `Shorten` button.
2. The shortened URL will be displayed below the text box.
3. Click on the shortened URL to visit the original URL.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
