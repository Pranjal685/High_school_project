## Mini McDonald's ATM Machine

An interactive, terminal-based mini food-ordering system inspired by a McDonald's self-service kiosk. It lets a user register or log in by name, browse a menu stored in MySQL, place orders, view their order history, and visualize the day's sales using a bar chart.

### Features
- **Login or registration by name**: If the user does not exist, they are created automatically.
- **Menu from database**: Reads available food items and prices from `food_items`.
- **Place multiple items per session**: Accumulates a running bill and saves each line item to `orders`.
- **Order history**: Displays a user's past orders with dates.
- **Daily sales chart**: Shows a bar chart of today's total sales by item using Matplotlib.
- **Simple input validation**: Rejects numeric-only names and invalid item selections.

### Tech stack
- **Python**: Terminal application
- **MySQL**: Persistent storage
- **mysql-connector-python**: Database driver
- **Matplotlib**: Sales visualization

---

## Getting started

### Prerequisites
- Python 3.9+ installed
- MySQL Server 8.x (or compatible) running locally
- Git (optional but recommended for version control)

### 1) Clone or download the project
If you have not already, place the project somewhere on your machine.

```bash
git clone <your-repo-url> "Final food service"
cd "Final food service"
```

If you are using these sources before publishing to GitHub, simply `cd` into the folder where `main.py` lives.

### 2) Create and activate a virtual environment

```bash
# Windows (PowerShell)
py -m venv .venv
. .venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Set up the database schema
Your MySQL database already exists. Ensure it is named `food_service_atm` (or update the connection in `main.py`). The script will only create missing tables and will seed menu items conditionally to avoid duplicates.

Run it against the existing database (MySQL CLI examples):

```bash
# Option 1: connect to DB, then source script
mysql -u root -p
mysql> USE food_service_atm;
mysql> SOURCE database/schema.sql;

# Option 2: one-liner specifying the DB
mysql -u root -p food_service_atm < database/schema.sql
```

### 5) Configure database credentials (if needed)
By default, `main.py` connects with:

```python
mysql.connector.connect(host="localhost", user="root", password="redhat", database="food_service_atm")
```

If your MySQL username/password differ, edit `connect_db()` in `main.py` accordingly.

### 6) Run the app

```bash
python main.py
```

Follow the prompts to log in or register, place orders, and view order history or today's sales chart.

---

## Usage overview
- **Log in/Register**: Enter your name. New names are registered automatically.
- **Place an order**: Type the menu item number and quantity. Repeat for multiple items. Enter `0` to finish.
- **Bill**: Displays the total cost for this session.
- **Order history**: Shows all your past orders with dates.
- **Sales chart**: Plots a bar chart of today's sales grouped by item.

---

## Project structure
```
Final food service/
├─ main.py                  # Application entry point
├─ requirements.txt         # Python dependencies
├─ database/
│  └─ schema.sql            # MySQL schema + seed data
└─ README.md                # You are here
```

---

## Notes and limitations
- This is a learning project originally built in high school; it focuses on fundamentals rather than production hardening.
- Credentials are stored directly in `main.py`; update them to match your environment.
- The app uses parameterized queries to interact with MySQL, but there is no authentication beyond a name.

### Credits
- Built by: Your Name

---

## How to publish this project to GitHub (step by step)

### Option A: Using GitHub website (simplest)
1. Create a new repository on GitHub: click New → name it (e.g., `mini-mcdonalds-atm`), choose Public or Private, and skip adding README (you already have one).
2. On your computer, open PowerShell in the project folder (`Final food service`).
3. Initialize Git and make the first commit:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: Mini McDonald's ATM Machine"
   ```
4. Add the remote (replace `<YOUR_USERNAME>` and repo name):
   ```powershell
   git remote add origin https://github.com/<YOUR_USERNAME>/mini-mcdonalds-atm.git
   ```
5. Push the code:
   ```powershell
   git branch -M main
   git push -u origin main
   ```

### Option B: Using GitHub CLI (gh)
1. Install GitHub CLI if needed, then authenticate:
   ```powershell
   winget install GitHub.cli
   gh auth login
   ```
2. From the project folder, run:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: Mini McDonald's ATM Machine"
   gh repo create mini-mcdonalds-atm --public --source . --remote origin --push
   ```

That’s it—your project will be on GitHub with this README, a ready-to-run schema, and dependencies file.


