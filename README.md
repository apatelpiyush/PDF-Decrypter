
# 🔐 PDF Modifier: Encrypt & Decrypt Password-Protected PDFs

A user-friendly **Tkinter-based GUI** tool written in **Python** that allows you to:
- 🔓 Decrypt password-protected PDF files
- 🔒 Encrypt normal PDF files with a custom password
- 📁 Browse and select PDF files easily
- ⚠️ Handle wrong passwords, missing files, and invalid inputs gracefully

---

## 📦 Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 📂 File Browser               | Select your target PDF using a file dialog                                 |
| 🔑 Manual Password Entry      | Input your encryption or decryption password manually                      |
| 🔓 Decrypt PDFs               | Remove encryption from PDF if password is correct                          |
| 🔒 Encrypt PDFs               | Add password protection to normal PDFs with customizable restrictions      |
| ⚠️ Error Handling             | Gracefully handles incorrect passwords, missing files, or unsupported PDFs |
| 🧼 GUI with Tkinter           | Built with a clean and functional GUI using Tkinter                        |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or above
- `pikepdf` (install using pip)
- `tkinter` (included with most Python installations)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/apatelpiyush/pdf_en-or-decrypter.git
cd pdf_en-or-decrypter
```

2. Install dependencies:

```bash
pip install pikepdf
```

---

## 🖥️ How to Use

1. Run the Python script:

```bash
python pdf_modifier.py
```

2. In the GUI:
   - Click **Browse** to select a PDF file
   - Choose **Encrypt** or **Decrypt** from the dropdown
   - Enter a password in the text box
   - Click the corresponding button to process the PDF

---

## 📁 Output Behavior

- Encrypted files overwrite the original with restricted permissions (no print/extract)
- Decrypted files overwrite the original and remove encryption

> ⚠️ Always keep a backup if needed

---

## 🛠️ File Structure

```
pdf_en-or-decrypter/
├── pdf_modifier.py
├── README.md
└── LICENSE.txt
```

---

## ✍️ Author

Created by Piyush A Patel

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
