from pathlib import Path
import markdown


KNOWLEDGE_BASE_PATH = Path("docs/knowledge-base")


def get_knowledge_base_files():
    return sorted(KNOWLEDGE_BASE_PATH.glob("KB-*.md"))

def read_knowledge_base_file(file_path):
    return file_path.read_text(encoding="utf-8")

def render_markdown(content):
    return markdown.markdown(
        content,
        extensions=["extra"]
    )

def parse_knowledge_base_metadata(content):
    lines = content.splitlines()

    title_line = lines[0]

    article_id, title = title_line.split(" — ", 1)

    article_id = article_id.replace("# ", "").strip()
    title = title.strip()

    metadata = {
        "id": article_id,
        "title": title
    }

    for line in lines[1:]:
        if line.startswith("**Category:**"):
            metadata["category"] = line.replace("**Category:**", "").strip()

        elif line.startswith("**System:**"):
            metadata["system"] = line.replace("**System:**", "").strip()

        elif line.startswith("**Audience:**"):
            metadata["audience"] = line.replace("**Audience:**", "").strip()

        elif line.startswith("**Severity:**"):
            metadata["severity"] = line.replace("**Severity:**", "").strip()

        elif line.startswith("**Last Updated:**"):
            metadata["last_updated"] = line.replace("**Last Updated:**", "").strip()

    return metadata

def get_knowledge_base_articles():
    articles = []

    for file in get_knowledge_base_files():
        content = read_knowledge_base_file(file)
        metadata = parse_knowledge_base_metadata(content)

        articles.append(metadata)

    return articles

def get_knowledge_base_article(article_id):
    for file in get_knowledge_base_files():
        content = read_knowledge_base_file(file)
        metadata = parse_knowledge_base_metadata(content)

        if metadata["id"] == article_id:
            return {
                "metadata": metadata,
                "content": content,
                "html": render_markdown(content).replace(
                    f"<h1>{metadata['id']} — {metadata['title']}</h1>",
                    "",
                    1
                )
            }
    return None
