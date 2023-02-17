# Static Site Generator

This is a simple static-site generator implemented in Python. It can take a folder containing Markdown pages and generate a website with support for a homepage, articles, and supporting pages.

## Folder Structure

Here is an example of what your folder structure should look like:

static-site-generator/
│
├── config.yml
├── generate.py
├── pages/
│ ├── about.md
│ ├── article1.md
│ ├── article2.md
│ └── index.md
├── output/
└── templates/
├── base.html
├── article.html
├── about.html
└── index.html


- `config.yml` contains the configuration for the static-site generator.
- `generate.py` is the main script that generates the static website.
- `pages/` is the folder containing the Markdown files that will be used to generate the content of the website.
- `output/` is the folder where the generated website will be saved.
- `templates/` contains the Jinja2 templates that are used to generate the HTML pages from the Markdown content.

## Contributing

If you would like to contribute to the static-site generator, feel free to fork this repository and submit a pull request. Any contributions are greatly appreciated.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.