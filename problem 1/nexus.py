import yaml
import markdown
from pathlib import Path


class nexus:
    def __init__(self,config:str) -> None:
        config= yaml.safe_load(Path(config).read_text())
        self.title = config["title"]
        self.favicon = config["favicon"]
        self.profile = config["profile"]
    
    '''
      # generate html from the markdown
    '''
    def _gen_html(self,content:str):
        return markdown.markdown(content)
    
    '''
     # build the page
    '''
    def gen_page(self,markdown_page:str,html_page:str):
        # replace the {{Content}} with the html
        with open(f"website/pages/{markdown_page}.md", "r") as f:
            markdown_text = f.read()
        # Convert Markdown to HTML
        html = self._gen_html(markdown_text)

        # Read in the appropriate template file
        with open(f"website/template/{html_page}.html", "r") as f:
            template = f.read()
        # add title
        template = template.replace("{{title}}",self.title)
        
        # Replace the placeholder in the template with the generated HTML
        final_html = template.replace("{{Content}}", html)

        # Write out the final HTML to a file
        with open(f"website/my-site/{html_page}.html", "w+") as f:
            f.write(final_html)


Builder = nexus("website/config.yml")

Builder.gen_page("about","about")