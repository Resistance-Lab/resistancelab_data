import requests
from pathlib import Path
import os


def download(url):
    basename = os.path.basename(url)
    directory = os.path.join(os.path.dirname(__file__), '..', '..', 'source_data', 'police-population')

    Path(directory).mkdir(parents=True, exist_ok=True)
    output_file = os.path.join(directory, basename)
    if not Path(output_file).exists():
        r = requests.get(url)
        with open(output_file, 'wb') as f:
            f.write(r.content)
    return os.path.join(directory, basename)


def make_output_directory(subject):
    path = os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_data', 'police-population', subject)
    Path(path).mkdir(parents=True, exist_ok=True)
    return path
