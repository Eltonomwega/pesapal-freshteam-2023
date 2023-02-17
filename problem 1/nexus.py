import yaml
import markdown
from pathlib import Path
import os

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
    
    def get_template(self,template:str)->str:
        # Read in the appropriate template file
        with open(f"website/template/{template}.html", "r") as f:
            template = f.read()
        # add title
        return template.replace("{{title}}",self.title)
        
    # get a list of cards  
    def gen_blog_list(self,path:str)->list:
        result = []
        for filename in os.listdir(path):
            filepath = os.path.join(path,filename)
            
            # check if is a file
            if os.path.isfile(filepath):
                with open(f""+filepath,"r") as f:
                    markdown_text = f.read()
                template = markdown_text.split("---")    
                variables = template[1]
                config = yaml.safe_load(variables)
                # build the card
                with open(f"website/template/blog_card.html","r") as f:
                    card = f.read()
                card = card.replace("{{title}}",config["title"])
                card = card.replace("{{description}}",config["description"])
                card = card.replace("{{page}}",filename.split(".")[0])
                result.append(card)
        return result
    
    def gen_posts(self):
        path = "website/pages/posts"
        for filename in os.listdir(path):
            filepath = os.path.join(path,filename)
            if os.path.isfile(filepath):
                with open(f""+filepath,"r") as f:
                    markdown_text = f.read()
                markdown_text = markdown_text.split("---")[2]
                template = self.get_template("article")
                template = template.replace("{{Content}}",self._gen_html(markdown_text))
                with open(f"website/my-site/posts/"+filename.split(".")[0]+".html","w+") as f:
                    f.write(template) 
    '''
     # build the page
    '''
    def gen_page(self,markdown_page:str,template:str):
        
        with open(f"website/pages/{markdown_page}.md", "r") as f:
            markdown_text = f.read()
        # Convert Markdown to HTML
        html = self._gen_html(markdown_text)
        # Replace the placeholder in the template with the generated HTML
        final_html = template.replace("{{Content}}", html)

        # Write out the final HTML to a file
        with open(f"website/my-site/{markdown_page}.html", "w+") as f:
            f.write(final_html)






Builder = nexus("website/config.yml")
# gen the home and about page
Builder.gen_page("home",Builder.get_template("home"))
Builder.gen_page("about",Builder.get_template("about"))

# gen the blog list
blogs = Builder.gen_blog_list("website/pages/posts")
blog_page = Builder.get_template("blog")
blog_page = blog_page.replace("{{Content}}",' '.join(blogs))
with open(f"website/my-site/blog.html","w+") as f:
    f.write(blog_page)

# gen articles
Builder.gen_posts()   
