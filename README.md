python-learning-website/
├── README.md        <!-- Deployment & hosting instructions -->
├── index.html
├── style.css
├── deploy.sh            <!-- deployment helper -->
├── chapters/
│   ├── chapter1.html
│   ├── chapter2.html
│   ├── chapter3.html
│   ├── chapter4.html
│   └── chapter5.html
└── scripts/
    ├── chapter1_exercise.py
    ├── chapter2_exercise.py
    ├── chapter3_exercise.py
    ├── chapter4_exercise.py
    └── chapter5_exercise.py
├── index.html
├── style.css
├── deploy.sh            <!-- deployment helper -->
├── chapters/
│   ├── chapter1.html
│   ├── chapter2.html
│   ├── chapter3.html
│   ├── chapter4.html
│   └── chapter5.html
└── scripts/
    ├── chapter1_exercise.py
    ├── chapter2_exercise.py
    ├── chapter3_exercise.py
    ├── chapter4_exercise.py
    └── chapter5_exercise.py

<!-- README.md -->
# Python Learning Seminar Website

This project contains a static site for a 5-chapter Python seminar.

## Hosting on GitHub Pages (via Web UI)
1. **Create a GitHub account** at https://github.com, if you don't have one.
2. **Create a new repository** named `python-learning-website` (make it public):
   - Log in, click **+** → **New repository**.
   - Name it **python-learning-website**, add a description if you like, and click **Create repository**.
3. **Upload your files**:
   - In your new repo, click **Add file** → **Upload files**.
   - Drag & drop all the files and folders from your local `python-learning-website` folder (including `index.html`, `style.css`, `chapters/`, `scripts/`, etc.).
   - Scroll down and click **Commit changes**.
4. **Enable GitHub Pages**:
   - In your repo, click **Settings** → **Pages** (in the left sidebar).
   - Under **Source**, choose **Branch: main** and **Folder: / (root)**.
   - Click **Save**. After a minute, your site will be live at:
     `https://<your-username>.github.io/python-learning-website/`