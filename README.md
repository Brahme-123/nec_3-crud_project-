# CRUD API Project — Quick Start

This project is a small Flask CRUD application. This README explains how to create an `output/` directory, generate a sample image, and view it in your browser.

**Prerequisites:**
- Python 3.8+
- pip

**Install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate   # on Windows use: .venv\\Scripts\\activate
pip install -r requirements.txt
pip install pillow
```

**1) Make sure `output/` exists**

We replaced the previous `output` file with a directory. If you ever need to recreate it manually:

```bash
mkdir output
```

**2) Generate a sample image**

Run the helper script to create a sample `photo.png` inside `output/`:

```bash
python save_image.py
```

You should see:

```
Saved sample image to output/photo.png
```

**3) View the image in the browser**

Start the Flask app:

```bash
python app.py
```

Open this URL in your browser to view the generated image:

```
http://127.0.0.1:5000/output/photo.png
```

Alternatively, copy or move the image into the `static/` folder and reference it from templates:

```bash
cp output/photo.png static/photo.png   # Windows: copy output\\photo.png static\\photo.png
```

Then in an HTML template you can use:

```html
<img src="{{ url_for('static', filename='photo.png') }}" alt="Photo">
```

**4) Notes & Tools**

- `save_image.py` uses Pillow to create an example image.
- `app.py` includes a route `/output/<filename>` that serves files from the `output/` directory.
- If you need to save user-uploaded photos, use `os.makedirs('output', exist_ok=True)` and save files into that folder.

If you'd like, I can update `requirements.txt` to include `Pillow`, or add an upload form and save uploaded images to `output/`.

---
Happy coding! If you want the README in Telugu or more screenshots, tell me which language and I'll update it.
