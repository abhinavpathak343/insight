# People Insights Emailer

A Python-based automation tool that generates personalized team insights for People Managers and sends templated email reports based on structured HR data.

---

## 📌 Features

- 🧠 Processes structured employee performance data using **Pandas**
- 📬 Sends personalized team summaries via **templated HTML emails** using **Jinja2** and **SMTP**
- 📊 Groups team metrics by People Manager
- 🔁 Automates weekly insight delivery with minimal setup

---

## 📂 Project Structure

```
people_insights/
├── data/
│   └── employee_data.csv          # Sample HR dataset
├── templates/
│   └── email_template.html        # Email layout using Jinja2
├── send_insights.py               # Core Python script
├── requirements.txt               # Required libraries
```

---

## ⚙️ Technologies Used

- Python, Pandas, Jinja2
- smtplib (for email delivery)
- CSV (structured data source)

---

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/people-insights-emailer.git
   cd people-insights-emailer
   ```

2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Replace placeholder email credentials in `send_insights.py`  
   ```python
   EMAIL_ADDRESS = 'youremail@gmail.com'
   EMAIL_PASSWORD = 'yourpassword'  # or use environment variables
   ```

4. Run the script  
   ```bash
   python send_insights.py
   ```

---

## ✉️ Example Email Output

Each manager receives a detailed report of their team like this:

```
Subject: Weekly People Insights - Alice

Hello Alice,

Here's a snapshot of your team's performance this week:
- John Doe - Engineering | Score: 4.5 | Projects: 12
- Jane Smith - Engineering | Score: 4.2 | Projects: 10
...
```

---

## ✅ Future Enhancements

- Support for SendGrid or AWS SES
- Integration with real HR systems via REST APIs
- GPT-based summary generation using OpenAI API

---

## 📜 License

MIT License.
