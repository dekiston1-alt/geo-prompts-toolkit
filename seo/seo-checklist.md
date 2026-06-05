# SEO Implementation Checklist — Goddess Fuel Wellness

## Completed in This Build

### Technical SEO
- [x] `sitemap.xml` — lists all pages with priority and changefreq
- [x] `robots.txt` — allows all crawlers, points to sitemap
- [x] Open Graph meta tags on landing page (og:title, og:description, og:image, og:url)
- [x] Twitter Card meta tags
- [x] Canonical URLs (set permalink in each blog post front matter)
- [x] Mobile-responsive design (landing page)
- [x] Fast-loading HTML (no render-blocking scripts)

### Structured Data (JSON-LD)
- [x] Product Review schema on landing page
- [x] Organization schema on landing page
- [x] Each blog post front matter includes meta_title and meta_description

### On-Page SEO
- [x] Keyword-rich H1 on landing page
- [x] H2/H3 hierarchy in all blog posts
- [x] Meta descriptions under 160 characters for all pages
- [x] Alt text pattern included (add to images when uploaded)
- [x] Internal linking between blog posts (add manually when posts go live)
- [x] Affiliate disclosure on landing page

---

## Still To Do (Manual Steps)

### Google Analytics Setup
1. Go to analytics.google.com
2. Create a new GA4 property for `dekiston1-alt.github.io/Goddess-fuel`
3. Copy your Measurement ID (format: `G-XXXXXXXXXX`)
4. In `landing-page/index.html`, replace the comment:
   ```
   <!-- GA_TRACKING_CODE_PLACEHOLDER -->
   ```
   With:
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```
5. Add same code to every blog post HTML page

### Google Search Console
1. Go to search.google.com/search-console
2. Add property: `https://dekiston1-alt.github.io/Goddess-fuel/`
3. Verify via HTML tag or DNS record
4. Submit sitemap: `https://dekiston1-alt.github.io/Goddess-fuel/sitemap.xml`

### Pinterest Rich Pins
1. Go to Pinterest Business account settings
2. Enable Rich Pins for your website
3. Validate at: developers.pinterest.com/tools/url-debugger/
4. This will pull your Open Graph data into Pinterest pin previews automatically

### Images
- Add `og-image.jpg` (1200x630px) to `/assets/` folder for social sharing preview
- All images should have descriptive `alt` tags with target keywords
- Compress images to under 100KB each (use squoosh.app)

### Blog Post Pages
When you publish blog posts to GitHub Pages, add to each HTML file:
```html
<!-- Google Analytics -->
<!-- GA_TRACKING_CODE_PLACEHOLDER -->

<!-- Open Graph -->
<meta property="og:title" content="[POST TITLE]" />
<meta property="og:description" content="[META DESCRIPTION]" />
<meta property="og:image" content="https://dekiston1-alt.github.io/Goddess-fuel/assets/[POST-IMAGE].jpg" />
<meta property="og:url" content="https://dekiston1-alt.github.io/Goddess-fuel/blog/[SLUG]/" />
<meta property="og:type" content="article" />

<!-- Article Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[POST TITLE]",
  "description": "[META DESCRIPTION]",
  "author": {"@type": "Person", "name": "Kis"},
  "publisher": {"@type": "Organization", "name": "Goddess Fuel Wellness"},
  "datePublished": "[PUBLISH DATE]",
  "url": "https://dekiston1-alt.github.io/Goddess-fuel/blog/[SLUG]/"
}
</script>
```

---

## Target Keywords by Page

| Page | Primary Keyword | Secondary Keywords |
|------|-----------------|-------------------|
| Home | medicinal garden kit | grow herbs at home, healing garden |
| Blog 1 | medicinal garden kit review | is medicinal garden kit worth it |
| Blog 2 | medicinal herbs grow at home | healing herbs home garden |
| Blog 3 | grow your own medicinal herbs | start medicinal herb garden |
| Blog 4 | best herb garden kit beginners 2026 | herb garden starter kit |
| Blog 5 | benefits of medicinal garden | why grow medicinal herbs at home |

---

## Pinterest SEO Notes
- Pin descriptions are already keyword front-loaded
- Board names include exact-match keywords
- Enable Rich Pins to pull meta descriptions automatically
- Post consistently — Pinterest rewards frequency
- Use all 5 hashtag sets in rotation (see `/content/pinterest/hashtag-sets.md`)
