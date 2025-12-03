import os
import re
import json
import markdown
import shutil

CONTENT_DIR = 'content'
PUBLIC_DIR = 'public'
TEMPLATE_PATH = 'templates/layout.html'
HOME_TEMPLATE_PATH = 'templates/home.html'

def ensure_public_dir():
    if not os.path.exists(PUBLIC_DIR):
        os.makedirs(PUBLIC_DIR)
    
    # Copy images directory if it exists
    images_src = os.path.join(CONTENT_DIR, 'images')
    images_dest = os.path.join(PUBLIC_DIR, 'images')
    
    if os.path.exists(images_src):
        if os.path.exists(images_dest):
            shutil.rmtree(images_dest)
        shutil.copytree(images_src, images_dest)

def get_files():
    files = []
    for f in os.listdir(CONTENT_DIR):
        if f.endswith('.md'):
            files.append(f)
    return files

def parse_links(content):
    # Find all [[WikiLink]] occurrences
    # Returns a list of target page names
    regex = r'\[\[(.*?)\]\]'
    matches = re.findall(regex, content)
    return matches

def process_content(content):
    # Convert [[Page Name]] to <a href="Page Name.html">Page Name</a>
    regex = r'\[\[(.*?)\]\]'
    def replace_link(match):
        page_name = match.group(1)
        return f'<a href="{page_name}.html" class="internal-link">{page_name}</a>'
    
    processed = re.sub(regex, replace_link, content)
    return processed

def build_graph(files):
    nodes = []
    links = []
    
    # Create nodes first
    for f in files:
        page_id = os.path.splitext(f)[0]
        nodes.append({"id": page_id})

    # Create links
    for f in files:
        source_id = os.path.splitext(f)[0]
        file_path = os.path.join(CONTENT_DIR, f)
        with open(file_path, 'r') as file:
            content = file.read()
            targets = parse_links(content)
            for target in targets:
                # Only add link if target exists as a node (simple validation)
                if any(n['id'] == target for n in nodes):
                    links.append({"source": source_id, "target": target})
    
    return {"nodes": nodes, "links": links}

def build_site():
    ensure_public_dir()
    files = get_files()
    
    # Build and save graph
    graph_data = build_graph(files)
    with open(os.path.join(PUBLIC_DIR, 'graph.json'), 'w') as f:
        json.dump(graph_data, f, indent=2)
    
    # Load templates
    with open(TEMPLATE_PATH, 'r') as f:
        content_template = f.read()
    
    with open(HOME_TEMPLATE_PATH, 'r') as f:
        home_template = f.read()
    
    # Process each file
    for f in files:
        page_id = os.path.splitext(f)[0]
        input_path = os.path.join(CONTENT_DIR, f)
        
        # Home page uses special template (graph only, no content)
        if page_id == 'Home':
            final_html = home_template
            
            # Write to both Home.html and index.html
            with open(os.path.join(PUBLIC_DIR, 'Home.html'), 'w') as out_file:
                out_file.write(final_html)
            with open(os.path.join(PUBLIC_DIR, 'index.html'), 'w') as out_file:
                out_file.write(final_html)
        else:
            # Content pages use the layout template
            with open(input_path, 'r') as file:
                raw_content = file.read()
                
            # Pre-process links in markdown before conversion
            linked_content = process_content(raw_content)
            
            # Convert to HTML
            html_content = markdown.markdown(linked_content)
            
            # Inject into template using simple string replacement
            final_html = content_template.replace('{title}', page_id)
            final_html = final_html.replace('{content}', html_content)
            final_html = final_html.replace('{current_page_id}', page_id)
            
            # Write to public
            output_filename = f"{page_id}.html"
            with open(os.path.join(PUBLIC_DIR, output_filename), 'w') as out_file:
                out_file.write(final_html)

    print(f"Build complete. Generated {len(files)} pages and graph.json.")

if __name__ == "__main__":
    build_site()
