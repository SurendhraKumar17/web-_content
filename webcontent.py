{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "456dc706-d198-4f63-a1a1-fa589efc9760",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "def stream_web_content(url):\n",
    "    \"\"\"\n",
    "    Streams content from a URL in chunks.\n",
    "\n",
    "    Args:\n",
    "        url (str): The URL of the resource to stream.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # 'stream=True' prevents the response content from being downloaded all at once\n",
    "        with requests.get(url, stream=True) as response:\n",
    "            response.raise_for_status()  # Raise an exception for bad status codes\n",
    "            for chunk in response.iter_content(chunk_size=8192):\n",
    "                if chunk:  # Filter out keep-alive new chunks\n",
    "                    print(f\"Received chunk of size {len(chunk)} bytes\")\n",
    "                    # Process the chunk, e.g., write to a local file\n",
    "                    # with open('downloaded_file', 'ab') as f:\n",
    "                    #     f.write(chunk)\n",
    "    except requests.exceptions.RequestException as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "\n",
    "# Example usage (using a large file from GitHub)\n",
    "stream_web_content('https://github.com/git/git/archive/refs/tags/v2.46.0.zip')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cebd0902-0070-4109-bbbf-8c9e8a83d7bb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
