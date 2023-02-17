import os
import yaml
import markdown
from pathlib import Path

class Nexus:
    def __init__(self, config_file):
        with open(config_file) as f:
            config = yaml.safe_load(f)
        self.title = config["title"]
        self.favicon = config["favicon"]
        self.profile = config["profile"]

    def generate_html(self, content):
        return markdown.markdown(content)

    def get_template(self, template):
        with open(f"website/template/{template}.html") as f:
            return f.read().replace("{{title}}", self.title)

    def generate_blog_list(self, path):
        result = []
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            if os.path.isfile(filepath):
                with open(filepath) as f:
                    markdown_text = f.read()
                variables, content = markdown_text.split("---")[1:]
                config = yaml.safe_load(variables)
                with open("website/template/blog_card.html") as f:
                    card = f.read()
                card = card.replace("{{title}}", config["title"])
                card = card.replace("{{description}}", config["description"])
                card = card.replace("{{page}}", filename.split(".")[0])
                result.append(card)
        return result

    def generate_posts(self):
        path = "website/pages/posts"
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            if os.path.isfile(filepath):
                with open(filepath) as f:
                    markdown_text = f.read()
                content = markdown_text.split("---")[2]
                template = self.get_template("article")
                template = template.replace("{{Content}}", self.generate_html(content))
                with open(f"website/output/posts/{filename.split('.')[0]}.html", "w+") as f:
                    f.write(template)

    def generate_page(self, markdown_page, template):
        with open(f"website/pages/{markdown_page}.md") as f:
            markdown_text = f.read()
        html = self.generate_html(markdown_text)
        final_html = template.replace("{{Content}}", html)
        with open(f"website/output/{markdown_page}.html", "w+") as f:
            f.write(final_html)

builder = Nexus("website/config.yml")
builder.generate_page("home", builder.get_template("home"))
builder.generate_page("about", builder.get_template("about"))
blogs = builder.generate_blog_list("website/pages/posts")
blog_page = builder.get_template("blog").replace("{{Content}}", " ".join(blogs))
with open("website/output/blog.html", "w+") as f:
    f.write(blog_page)
builder.generate_posts()
