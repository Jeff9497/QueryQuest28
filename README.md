# 🌟 QueryQuest 28 

**QueryQuest28** is a Python-based command-line search engine that empowers you to perform Google searches directly from the terminal. With a touch of magic ✨ and flexibility, QueryQuest lets you search the web effortlessly, offering customizable options for language, region, and the number of results.

## 📚 Table of Contents

- [🌟 Introduction](#-introduction)
- [🎯 Features](#-features)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
  - [🔍 Running with Default Settings](#-running-with-default-settings)
  - [🎨 Customizing Search Options](#-customizing-search-options)
- [🌍 Country Codes](#-country-codes)
- [📦 Required Libraries](#-required-libraries)
- [📄 License](#-license)

## Introduction

Welcome to **QueryQuest28**, your next magical search engine! 🌐 Whether you need quick search results or prefer to fine-tune your search criteria, QueryQuest delivers a seamless experience. Say goodbye to cluttered browsers 🗑️ and let QueryQuest bring you the information you need, right in your terminal.

## 🎯 Features

- **Effortless Searching**: Perform Google searches directly from your terminal. 🖥️
- **Customization**: Choose the language, region, and number of search results. 🛠️
- **Looped Searching**: Keep searching until you find exactly what you're looking for. 🔄
- **Colorful Interface**: Enjoy a visually appealing command-line interface with color-coded prompts and results. 🎨

## ⚙️ Installation

To get started with QueryQuest, you’ll need to install the required libraries. Follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Jeff9497/QueryQuest28.git
   cd QueryQuest28
   ```

2. **Install Required Libraries:**

   You can install the required Python libraries by running:

   ```bash
   pip install googlesearch-python
   pip install colorama
   ```

## 🚀 Usage

Once installed, you can start using QueryQuest by running the following command:

```bash
python3 QueryQuest28.py
```

### 🔍 Running with Default Settings

If you prefer a quick search, QueryQuest offers default settings:
- **Language**: English (`en`) 🇬🇧
- **Region**: Kenya (`ke`) 🇰🇪
- **Number of Results**: 5

Simply run the script and choose the default settings to get started immediately.

### 🎨 Customizing Search Options

If you want more control over your search results, QueryQuest lets you customize:
- **Number of Results**: Specify how many results you'd like to retrieve. 
- **Language Code**: Define the language for your search results (e.g., `en` for English, `fr` for French). 
- **Region Code**: Choose the region from which to fetch results (e.g., `us` for the United States, `ke` for Kenya). 🗺

After running the script, select the option to customize your search settings, and enter the desired parameters.

## 🌍 Country Codes

QueryQuest uses ISO 3166-1 alpha-2 country codes to tailor your search results based on the selected region. Below are a few common examples:

- 🇺🇸 `us`: United States
- 🇰🇪 `ke`: Kenya
- 🇫🇷 `fr`: France
- 🇩🇪 `de`: Germany
- 🇯🇵 `jp`: Japan

For a complete list of country codes, you can refer to the [ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

## 📦 Required Libraries

To run QueryQuest, you’ll need the following Python libraries:

- `googlesearch-python`: A library for performing Google searches. 
- `colorama`: A library to enable colored output in the terminal. 

You can install these libraries using pip:

```bash
pip install googlesearch-python colorama
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**QueryQuest28** was designed with simplicity, flexibility, and a touch of creativity in mind. Whether you're a developer looking to streamline your search workflow or just someone who enjoys a more customized search experience, QueryQuest has got you covered. Happy searching! 🌟
