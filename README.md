# 🍴 Culinary Club Blog

A beautiful blog website for a Culinary Club — built with HTML/CSS and deployable via GitHub Pages.

---

## 🚀 Run Locally



```bash
# Clone or download the repo, then:
python server.py
```

Your browser will automatically open to `http://localhost:8080`.

---

## 🌐 Deploy to GitHub Pages (Free Hosting)

1. **Create a GitHub repo** named `culinary-club` (or anything you like).
2. **Push these files** to the repo:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Culinary Club Blog"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/culinary-club.git
   git push -u origin main
   ```
3. **Enable GitHub Pages:**
   - Go to your repo → **Settings** → **Pages**
   - Source: `Deploy from a branch` → `main` → `/ (root)`
   - Click **Save**
4. Your site will be live at:
   `https://YOUR_USERNAME.github.io/culinary-club/`

---

## 📁 File Structure

```
culinary-club/
├── index.html      ← Main blog page (edit this to add posts!)
├── server.py       ← Local dev server
└── README.md       ← This file
```

---

## ✏️ How to Add a Blog Post

Open `index.html` and find the `posts-grid` section. Copy and paste a new `<article class="post-card">` block and update:
- The image URL (use [Unsplash](https://unsplash.com) for free photos)
- The tag (Recipe, Event, Workshop, etc.)
- The date and author
- The title and excerpt
- The "Read More" link

---

## 🎨 Customization Tips

| What you want to change | Where to look in `index.html` |
|---|---|
| Club name | `<div class="nav-logo">` and `<footer>` |
| Hero text | Inside `.hero-text` |
| Colors | `:root` CSS variables at the top |
| Marquee topics | Inside `.marquee-track` |
| About section | Inside `.about-content` |

---

