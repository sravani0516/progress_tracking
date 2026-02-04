import os
import requests
from concurrent.futures import ThreadPoolExecutor

# ===== DESKTOP DOWNLOAD FOLDER =====
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
DOWNLOAD_FOLDER = os.path.join(DESKTOP_PATH, "BulkDownloads")

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# ===== DOWNLOAD FUNCTION =====
def download_file(url):
    try:
        filename = url.split("/")[-1]
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)

        print(f"Downloading: {filename}")

        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Failed: {url} → {e}")

# ===== MAIN =====
if __name__ == "__main__":

    file_urls = [
        "http://localhost:8000/file1.txt",
        "http://localhost:8000/file2.png",
        "http://localhost:8000/file3.pdf",
    ]

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_file, file_urls)

    print("\nALL DOWNLOADS COMPLETED")