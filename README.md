# [Hariom Prasad - Portfolio](https://hariomprasad.dev/)

A modern, responsive portfolio website showcasing expertise in Pharmacoinformatics and Data Analytics.

## 🌟 Features

- **Responsive Design**: Fully responsive layout that works on all devices
- **Modern UI/UX**: Contemporary design with smooth animations and transitions
- **Interactive Elements**: Engaging user interactions and hover effects
- **Skills Showcase**: Visual representation of technical skills with progress bars
- **Project Portfolio**: Detailed project cards with categories and tags
- **Contact Form**: Functional contact form with backend support
- **SEO Optimized**: Meta tags and semantic HTML for better search engine visibility

## 🚀 Technologies Used

### Frontend
- HTML5
- CSS3 (with CSS Grid and Flexbox)
- JavaScript (ES6+)
- Google Fonts (Playfair Display, Work Sans)
- Font Awesome Icons

### Backend (Optional)
- Python 3.x
- Flask
- Flask-CORS
- SMTP for email notifications

## 📁 Project Structure

```
portfolio/
├── index.html          # Main HTML file
├── styles.css          # Stylesheet
├── script.js           # JavaScript functionality
├── app.py             # Python backend (optional)
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
```

## 🛠️ Setup Instructions

### Static Website (No Backend)

1. Clone or download the repository
2. Open `index.html` in your web browser
3. That's it! The website is ready to use

### With Python Backend

1. Install Python 3.x if not already installed
2. Install dependencies:
   ```bash
   pip install flask flask-cors
   ```

3. Configure email settings in `app.py`:
   ```python
   SMTP_SERVER = 'smtp.gmail.com'
   SMTP_PORT = 587
   SENDER_EMAIL = 'your-email@example.com'
   SENDER_PASSWORD = 'your-app-password'
   RECIPIENT_EMAIL = 'your-email@example.com'
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

5. Update the contact form submission in `script.js` to use the API:
   ```javascript
   fetch('http://localhost:5000/api/contact', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify(formData)
   });
   ```

## 🌐 Deployment Options

### 1. GitHub Pages (Static Only)
1. Create a GitHub repository
2. Push your files
3. Go to Settings > Pages
4. Select main branch and save
5. Your site will be live at `https://yourusername.github.io/repository-name`

### 2. Netlify (Static Only)
1. Create account at netlify.com
2. Drag and drop your project folder
3. Site is instantly deployed with HTTPS

### 3. Vercel (Static + Serverless Functions)
1. Create account at vercel.com
2. Import your GitHub repository
3. Automatic deployments on every push

### 4. Heroku (Full Stack with Backend)
1. Create a `Procfile`:
   ```
   web: python app.py
   ```
2. Create `requirements.txt`:
   ```
   Flask==2.3.0
   Flask-CORS==4.0.0
   gunicorn==21.2.0
   ```
3. Deploy to Heroku:
   ```bash
   heroku create your-portfolio-name
   git push heroku main
   ```

### 5. Custom Domain Setup

#### Using cPanel (Shared Hosting)
1. Upload files via FTP to `public_html` directory
2. Ensure `index.html` is in the root directory
3. Your site will be accessible at `yourdomain.com`

#### Using VPS (Digital Ocean, AWS, etc.)
1. Install web server (Nginx or Apache)
2. Configure virtual host
3. Upload files to web directory
4. Set up SSL certificate (Let's Encrypt)

Example Nginx configuration:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    root /var/www/portfolio;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

## 📝 Customization Guide

### Update Personal Information

1. **Contact Details** (in `index.html`):
   - Update email, phone, and location in the contact section
   - Replace placeholder social media links

2. **Skills** (in `index.html`):
   - Modify skill categories and progress percentages
   - Add or remove skills as needed

3. **Projects** (in `index.html`):
   - Update project descriptions and categories
   - Add your actual project links
   - Replace placeholder project tags

4. **Colors** (in `styles.css`):
   - Modify CSS variables in `:root` section
   - Change primary, secondary, and accent colors

5. **Images**:
   - Replace the profile initials with an actual photo
   - Add project screenshots in the project cards

### Adding New Sections

1. Add HTML structure in `index.html`
2. Style the section in `styles.css`
3. Add navigation link in the navbar
4. Update JavaScript for scroll animations in `script.js`

## 🎨 Color Scheme

The portfolio uses a sophisticated dark theme with gradient accents:

- **Primary**: #1a1a2e (Dark Blue)
- **Secondary**: #16213e (Navy)
- **Accent**: #0f3460 (Deep Blue)
- **Highlight**: #e94560 (Pink Red)
- **Gradients**: Purple to Pink (#667eea → #764ba2 → #f093fb)

## 📱 Responsive Breakpoints

- Desktop: > 1024px
- Tablet: 768px - 1024px
- Mobile: < 768px
- Small Mobile: < 480px

## 🔒 Security Considerations

### For Production Deployment:

1. **Environment Variables**: Never commit sensitive data (API keys, passwords)
2. **HTTPS**: Always use SSL certificate for production
3. **Form Validation**: Implement server-side validation
4. **Rate Limiting**: Add rate limiting to prevent spam
5. **CORS**: Configure proper CORS policies
6. **Input Sanitization**: Sanitize all user inputs

## 📧 Contact Form Setup

### Using FormSpree (Easiest)
1. Sign up at formspree.io
2. Create a form endpoint
3. Update form action in HTML:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

### Using EmailJS (No Backend)
1. Sign up at emailjs.com
2. Add EmailJS SDK to your HTML
3. Configure email service
4. Update JavaScript to use EmailJS

### Using Google Forms (Alternative)
1. Create a Google Form
2. Embed it in your contact section
3. Receive submissions in Google Sheets

## 🎯 SEO Optimization

Add these meta tags to `<head>` in `index.html`:

```html
<meta name="description" content="Hariom Prasad - Pharmacoinformatics Specialist & Data Analytics">
<meta name="keywords" content="Pharmacoinformatics, Data Analytics, Machine Learning, Drug Discovery, Bioinformatics">
<meta name="author" content="Hariom Prasad">

<!-- Open Graph -->
<meta property="og:title" content="Hariom Prasad | Portfolio">
<meta property="og:description" content="Pharmacoinformatics & Data Analytics Specialist">
<meta property="og:type" content="website">
<meta property="og:url" content="https://yourdomain.com">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Hariom Prasad | Portfolio">
<meta name="twitter:description" content="Pharmacoinformatics & Data Analytics Specialist">
```

## 📊 Analytics Integration

### Google Analytics
```html
<!-- Add before closing </head> tag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_GA_ID');
</script>
```

## 🐛 Troubleshooting

### Contact Form Not Working
- Check if backend server is running
- Verify CORS settings
- Check browser console for errors
- Ensure correct API endpoints

### Animations Not Playing
- Clear browser cache
- Check JavaScript console for errors
- Verify CSS animation browser support

### Responsive Issues
- Test on actual devices
- Use browser developer tools
- Check viewport meta tag

## 📚 Resources

- [Google Fonts](https://fonts.google.com/)
- [Font Awesome Icons](https://fontawesome.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS Tricks](https://css-tricks.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 📄 License

This portfolio template is free to use for personal and commercial projects.

## 🤝 Contributing

Feel free to fork this repository and customize it for your own use!

## 📞 Support

For questions or issues:
- Email: phariom.niper2024@gmail.com
- LinkedIn: [Hariom Prasad](https://www.linkedin.com/in/phariom2024niper/)
- GitHub: [Hariom Prasad](https://github.com/hariompr143/)

---

**Built with ❤️ by Hariom Prasad**

Last Updated: January 2026
