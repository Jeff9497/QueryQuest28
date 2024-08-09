# QueryQuest28

**QueryQuest28** is a Python-based command-line search engine that empowers users to perform Google searches directly from the terminal. With a touch of magic and flexibility, QueryQuest lets you search the web effortlessly, offering customizable options for language, region, and the number of results.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Running with Default Settings](#running-with-default-settings)
  - [Customizing Search Options](#customizing-search-options)
- [Country Codes](#country-codes)
- [License](#license)

## Introduction

Welcome to **QueryQuest28**, your next magical search engine! Whether you need quick search results or prefer to fine-tune your search criteria, QueryQuest delivers a seamless experience. Say goodbye to cluttered browsers and let QueryQuest bring you the information you need, right in your terminal.

## Features

- **Effortless Searching**: Perform Google searches directly from your terminal.
- **Customization**: Choose the language, region, and number of search results.
- **Looped Searching**: Keep searching until you find exactly what you're looking for.
- **Colorful Interface**: Enjoy a visually appealing command-line interface with color-coded prompts and results.

## Installation

To install QueryQuest, simply clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/QueryQuest.git
cd QueryQuest28
pip install -r requirements.txt
```

## Usage

Once installed, you can start using QueryQuest by running the following command:

```bash
python3 QueryQuest28.py
```

### Running with Default Settings

If you prefer a quick search, QueryQuest offers default settings:
- **Language**: English (`en`)
- **Region**: Kenya (`ke`)
- **Number of Results**: 5

Simply run the script and choose the default settings to get started immediately.

### Customizing Search Options

If you want more control over your search results, QueryQuest lets you customize:
- **Number of Results**: Specify how many results you'd like to retrieve.
- **Language Code**: Define the language for your search results (e.g., `en` for English, `fr` for French).
- **Region Code**: Choose the region from which to fetch results (e.g., `us` for the United States, `ke` for Kenya).

After running the script, select the option to customize your search settings, and enter the desired parameters.

## Country Codes

QueryQuest uses ISO 3166-1 alpha-2 country codes to tailor your search results based on the selected region. Below are a few common examples:

- `us`: United States
- `ke`: Kenya
- `fr`: France
- `de`: Germany
- `jp`: Japan

For a complete list of country codes, you can refer to the [ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**QueryQuest** was designed with simplicity, flexibility, and a touch of creativity in mind. Whether you're a developer looking to streamline your search workflow or just someone who enjoys a more customized search experience, QueryQuest has got you covered. Happy searching!
