# Static Site Generator

This is a simple static-site generator implemented in Python. It can take a folder containing Markdown pages and generate a website with support for a homepage, articles, and supporting pages.

## Features

- Generates a static website from Markdown files
- Supports a homepage, articles, and supporting pages
- Allows customization of page layout using templates
- Easily extensible with additional functionality

## Getting Started

To use the static-site generator, follow these steps:

1. Install Python 3.
2. Clone this repository.
3. Run `pip install -r requirements.txt` to install the required dependencies.
4. Put your Markdown files in the `pages` folder.
5. Run `python nexus.py` to generate the static website in the `output` folder.

## Folder Structure

Here is an example of what your folder structure should look like:

- static-site-generator/
  - config.yml
  - nexus.py
  - pages/
    - about.md
    - article.md
    - home.md
    - posts
      - post_1.md
  - output/
  - templates/
    - article.html
    - about.html
    - home.html


- `config.yml` contains the configuration for the static-site generator.
- `nexus.py` is the main script that generates the static website.
- `pages/` is the folder containing the Markdown files that will be used to generate the content of the website.
- `output/` is the folder where the generated website will be saved.
- `templates/` contains the Jinja2 templates that are used to generate the HTML pages from the Markdown content.

## Contributing

If you would like to contribute to the static-site generator, feel free to fork this repository and submit a pull request. Any contributions are greatly appreciated.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.