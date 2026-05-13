# 📱 QR ScanPro

## Professional Memory-Efficient QR Code Generator

QR ScanPro is a professional-grade web utility designed for the skincare and e-commerce industry. It bridges the gap between digital marketing and product transparency by allowing developers and brands to generate high-fidelity, branded QR codes instantly — without ever saving files to a server.

🔗 **Live Demo:** [https://uxzsm6t3merppqnazqmxr2.streamlit.app/](https://uxzsm6t3merppqnazqmxr2.streamlit.app/)  
📁 **GitHub Repo:** [https://github.com/nayabnayyer/QR_Project](https://github.com/nayabnayyer/QR_Project)

---

## ✨ Features

- 🚀 **In-Memory Processing** – Uses `BytesIO` to handle images entirely in RAM (no disk writes)
- 🎨 **Custom Dark-Mode UI** – Professional, skincare-branded interface
- 📥 **Instant PNG Download** – Generate and download QR codes in seconds
- 🧭 **Multi-Page Navigation** – Home, Tech Explanation, and Contact sections
- 🔒 **Secure** – No user data stored on server
- 📱 **Mobile Responsive** – Works seamlessly on all devices

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | Streamlit, Custom CSS |
| **Backend** | Python |
| **QR Generation** | qrcode library |
| **Image Processing** | Pillow (PIL) |
| **Memory Management** | BytesIO (in-memory buffering) |
| **Deployment** | Streamlit Cloud |

---

## 🧠 How It Works

### The Memory Buffer Logic (The Secret Sauce)

Instead of saving images to disk (slow + messy), QR ScanPro:

1. Generates QR code in memory
2. Saves it to a virtual buffer (`BytesIO`)
3. Serves the image directly to the user's browser
4. Never writes a single file to the server

```python

buf = io.BytesIO()
img.save(buf, format="PNG")
byte_im = buf.getvalue()

```
This approach is:

⚡ Faster – No disk I/O latency

🔒 More Secure – No leftover files

🧹 Cleaner – Zero footprint on the server

## 🚀 Installation & Local Setup
```python
# Clone the repository
git clone https://github.com/nayabnayyer/QR_Project.git
cd QR_Project

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🎯 Use Cases
- Skincare Brands – Add QR codes to product packaging linking to ingredients or tutorials

- E-commerce – Generate dynamic QR codes for promotional campaigns

- Events – Create custom QR codes for tickets or registrations

- Personal Portfolios – Link your resume or portfolio with a branded QR code

## 👩‍💻 What I Learned
- In-memory image processing with BytesIO

- Building multi-page Streamlit apps with sidebar navigation

- Custom CSS theming for professional UI

- QR code generation and customization (colors, sizes, borders)

- Deploying to Streamlit Cloud

- Creating a brand-focused utility with a real industry use case

## 🔮 Future Improvements
- Add custom logo overlay on QR codes

- Support for bulk QR generation (CSV upload)

- QR code scanning functionality

- Analytics dashboard (scan tracking)

- Multi-brand theming options

- Export as SVG or PDF

## 📄 License
This project is for educational and portfolio purposes.

## 🤝 Connect With Me
- **LinkedIn:** [linkedin.com/in/nayab-nayyer](https://linkedin.com/in/nayab-nayyer)

- **GitHub:** [github.com/nayabnayyer](https://github.com/nayabnayyer)

Email: nayabnayyer882@gmail.com

"Built for the skincare industry. Powered by Python memory buffering."

— Nayab Nayyer



buf = io.BytesIO()
img.save(buf, format="PNG")
byte_im = buf.getvalue()
