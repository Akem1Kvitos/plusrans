import os


class SourcesService:
    def __init__(self, views_path: str):
        self.views_path = views_path

    def get_source(self, source: str, filename: str):
        with open(os.path.join(self.views_path, source, filename), 'r') as fs:
            data = fs.read()
        return {
            "mimetype": "application/javascript" if source == "js" else f"text/{source}",
            "data": data
        }
