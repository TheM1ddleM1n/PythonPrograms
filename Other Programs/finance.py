import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from collections import defaultdict
import calendar


class FinanceTracker:

    CATEGORIES = [
        "Food & Dining",
        "Transportation",
        "Shopping",
        "Entertainment",
        "Bills & Utilities",
        "Healthcare",
        "Education",
        "Travel",
        "Groceries",
        "Other",
    ]

    def __init__(self):
        self.data_file = Path("finance_data.json")
        self.transactions: List[Dict] = []
        self.budgets: Dict[str, float] = {}
        self.monthly_income: float = 0.0

        self.load_data()

    def load_data(self):
        if self.data_file.exists():
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.transactions = data.get("transactions", [])
                    self.budgets = data.get("budgets", {})
                    self.monthly_income = data.get("monthly_income", 0.0)
            except Exception as e:
                print(f"⚠️ Error loading data: {e}")

    def save_data(self):
        try:
            with open(self.data_file, "w") as f:
                json.dump(
                    {
                        "transactions": self.transactions,
                        "budgets": self.budgets,
                        "monthly_income": self.monthly_income,
                        "last_updated": datetime.now().isoformat(),
                    },
                    f,
                    indent=2,
                )
        except Exception as e:
            print(f"⚠️ Error saving data: {e}")

    def add_transaction(
        self,
        amount: float,
        category: str,
        description: str,
        transaction_type: str = "expense",
        date: Optional[str] = None,
    ):
        if date is None:
            date = datetime.now().isoformat()

        transaction = {
            "id": len(self.transactions) + 1,
            "date": date,
            "type": transaction_type,
            "category": category,
            "amount": abs(amount),
            "description": description,
        }

        self.transactions.append(transaction)
        self.save_data()

        symbol = "💰" if transaction_type == "income" else "💸"
        print(f"\n{symbol} Transaction added: ${amount:.2f} - {description}")

        if transaction_type == "expense":
            self._check_budget_warning(category)

    def _check_budget_warning(self, category: str):
        if category not in self.budgets:
            return

        current_month = datetime.now().strftime("%Y-%m")
        month_spending = sum(
            t["amount"]
            for t in self.transactions
            if t["type"] == "expense"
            and t["category"] == category
            and t["date"].startswith(current_month)
        )

        budget = self.budgets[category]
        percentage = (month_spending / budget) * 100

        if percentage >= 100:
            print(
                f"⚠️ WARNING: Over budget for {category}! (${month_spending:.2f}/${budget:.2f})"
            )
        elif percentage >= 80:
            print(
                f"⚠️ ALERT: {category} at {percentage:.0f}% of budget (${month_spending:.2f}/${budget:.2f})"
            )

    def set_budget(self, category: str, amount: float):
        self.budgets[category] = amount
        self.save_data()
        print(f"✅ Budget set: {category} = ${amount:.2f}/month")

    def set_income(self, amount: float):
        self.monthly_income = amount
        self.save_data()
        print(f"✅ Monthly income set: ${amount:.2f}")

    def view_transactions(self, limit: int = 10, category: Optional[str] = None):
        filtered = self.transactions

        if category:
            filtered = [t for t in filtered if t["category"] == category]

        if not filtered:
            print("\n📊 No transactions found.")
            return

        print("\n📊 RECENT TRANSACTIONS")
        print("=" * 70)

        sorted_transactions = sorted(filtered, key=lambda x: x["date"], reverse=True)
        for transaction in sorted_transactions[:limit]:
            date = datetime.fromisoformat(transaction["date"]).strftime("%Y-%m-%d")
            symbol = "+" if transaction["type"] == "income" else "-"
            amount = transaction["amount"]
            category = transaction["category"]
            desc = transaction["description"]

            print(f"{date} | {symbol}${amount:>8.2f} | {category:<20} | {desc}")

    def monthly_report(self, year: int = None, month: int = None):
        if year is None:
            year = datetime.now().year
        if month is None:
            month = datetime.now().month

        month_str = f"{year}-{month:02d}"
        month_name = calendar.month_name[month]
        month_transactions = [
            t for t in self.transactions if t["date"].startswith(month_str)
        ]

        if not month_transactions:
            print(f"\n📊 No transactions for {month_name} {year}")
            return
        total_income = sum(
            t["amount"] for t in month_transactions if t["type"] == "income"
        )
        total_expenses = sum(
            t["amount"] for t in month_transactions if t["type"] == "expense"
        )
        net = total_income - total_expenses

        category_spending = defaultdict(float)
        for t in month_transactions:
            if t["type"] == "expense":
                category_spending[t["category"]] += t["amount"]

        print(f"\nMONTHLY REPORT - {month_name} {year}")
        print("=" * 70)
        print(f"💰 Total Income:    ${total_income:>10.2f}")
        print(f"💸 Total Expenses:  ${total_expenses:>10.2f}")
        print("-" * 70)
        net_symbol = "+" if net >= 0 else "-"
        net_label = "Net Savings" if net >= 0 else "Net Loss"
        print(f"📈 {net_label}:    {net_symbol}${abs(net):>10.2f}")

        if self.monthly_income > 0:
            savings_rate = (net / self.monthly_income) * 100
            print(f"💰 Savings Rate:    {savings_rate:>9.1f}%")

        print("\n📋 SPENDING BY CATEGORY")
        print("-" * 70)

        sorted_categories = sorted(
            category_spending.items(), key=lambda x: x[1], reverse=True
        )

        for category, amount in sorted_categories:
            percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0

            budget_status = ""
            if category in self.budgets:
                budget = self.budgets[category]
                budget_pct = (amount / budget) * 100
                remaining = budget - amount

                if budget_pct >= 100:
                    budget_status = f" ⚠️ OVER by ${abs(remaining):.2f}"
                elif budget_pct >= 80:
                    budget_status = f" ⚠️ ${remaining:.2f} left"
                else:
                    budget_status = f" ✅ ${remaining:.2f} left"
                    
            bar_length = 20
            filled = int((percentage / 100) * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)

            print(
                f"{category:<20} ${amount:>8.2f} ({percentage:>5.1f}%) [{bar}]{budget_status}"
            )

    def budget_overview(self):
        current_month = datetime.now().strftime("%Y-%m")

        print("\n💰 BUDGET OVERVIEW")
        print("=" * 70)

        if not self.budgets:
            print("No budgets set. Use 'Set Budget' to create budgets.")
            return

        for category, budget in sorted(self.budgets.items()):
            spent = sum(
                t["amount"]
                for t in self.transactions
                if t["type"] == "expense"
                and t["category"] == category
                and t["date"].startswith(current_month)
            )

            remaining = budget - spent
            percentage = (spent / budget) * 100 if budget > 0 else 0
            if percentage >= 100:
                status = "❌ OVER"
            elif percentage >= 80:
                status = "⚠️ WARNING"
            else:
                status = "✅ OK"
            bar_length = 20
            filled = min(int((percentage / 100) * bar_length), bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)

            print(f"{category:<20} ${spent:>8.2f}/${budget:>8.2f} [{bar}] {status}")
            print(f"{'':20} Remaining: ${remaining:>8.2f} ({100 - percentage:.0f}%)")
            print()

    def insights(self):
        if not self.transactions:
            print("\n📊 Not enough data for insights yet.")
            return

        print("\n💡 FINANCIAL INSIGHTS")
        print("=" * 70)
        if self.transactions:
            first_date = min(
                datetime.fromisoformat(t["date"]) for t in self.transactions
            )
            days = (datetime.now() - first_date).days + 1

            total_spent = sum(
                t["amount"] for t in self.transactions if t["type"] == "expense"
            )
            avg_daily = total_spent / days if days > 0 else 0

            print(f"📊 Average daily spending: ${avg_daily:.2f}")

        category_totals = defaultdict(float)
        for t in self.transactions:
            if t["type"] == "expense":
                category_totals[t["category"]] += t["amount"]

        if category_totals:
            top_category = max(category_totals.items(), key=lambda x: x[1])
            print(
                f"🏆 Top spending category: {top_category[0]} (${top_category[1]:.2f})"
            )
        current_month = datetime.now().strftime("%Y-%m")
        last_month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m")

        current_spending = sum(
            t["amount"]
            for t in self.transactions
            if t["type"] == "expense" and t["date"].startswith(current_month)
        )

        last_spending = sum(
            t["amount"]
            for t in self.transactions
            if t["type"] == "expense" and t["date"].startswith(last_month)
        )

        if last_spending > 0:
            change = ((current_spending - last_spending) / last_spending) * 100
            trend = "📈 Increasing" if change > 0 else "📉 Decreasing"
            print(f"\n{trend} spending: {abs(change):.1f}% vs last month")
            
        print("\n💰 RECOMMENDATIONS:")

        if self.monthly_income > 0:
            if current_spending > self.monthly_income:
                print("  ⚠️ You're spending more than you earn this month!")

            savings_rate = (
                (self.monthly_income - current_spending) / self.monthly_income
            ) * 100
            if savings_rate < 20:
                print("  💡 Try to save at least 20% of your income")

        for category, spent in category_totals.items():
            if category in self.budgets:
                if spent > self.budgets[category]:
                    print(f"  ⚠️ Consider reducing {category} spending")


def main():
    tracker = FinanceTracker()

    print("""
    ╔═══════════════════════════════════════╗
    ║   💰 PERSONAL FINANCE TRACKER 💰     ║
    ║      Manage Your Money Smartly        ║
    ╚═══════════════════════════════════════╝
    """)

    while True:
        print("\n" + "=" * 70)
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Transactions")
        print("4. Set Budget")
        print("5. Set Monthly Income")
        print("6. Monthly Report")
        print("7. Budget Overview")
        print("8. Financial Insights")
        print("9. Exit")
        print("=" * 70)

        choice = input("\nChoose option (1-9): ").strip()

        if choice == "1":
            try:
                amount = float(input("\nAmount: $"))

                print("\nCategories:")
                for i, cat in enumerate(tracker.CATEGORIES, 1):
                    print(f"{i}. {cat}")

                cat_choice = int(input("Select category (1-10): "))
                category = tracker.CATEGORIES[cat_choice - 1]

                description = input("Description: ").strip()

                tracker.add_transaction(amount, category, description, "expense")

            except (ValueError, IndexError):
                print("❌ Invalid input")

        elif choice == "2":
            try:
                amount = float(input("\nAmount: $"))
                description = input("Description: ").strip()

                tracker.add_transaction(amount, "Income", description, "income")

            except ValueError:
                print("❌ Invalid amount")

        elif choice == "3":
            print("\nFilter by category? (Enter to skip)")
            for i, cat in enumerate(tracker.CATEGORIES, 1):
                print(f"{i}. {cat}")

            cat_input = input("Category number (or Enter for all): ").strip()

            category = None
            if cat_input:
                try:
                    category = tracker.CATEGORIES[int(cat_input) - 1]
                except (ValueError, IndexError):
                    pass

            limit = input("Number of transactions (default 10): ").strip()
            limit = int(limit) if limit else 10

            tracker.view_transactions(limit, category)

        elif choice == "4":
            try:
                print("\nCategories:")
                for i, cat in enumerate(tracker.CATEGORIES, 1):
                    print(f"{i}. {cat}")

                cat_choice = int(input("Select category: "))
                category = tracker.CATEGORIES[cat_choice - 1]

                amount = float(input(f"Monthly budget for {category}: $"))

                tracker.set_budget(category, amount)

            except (ValueError, IndexError):
                print("❌ Invalid input")

        elif choice == "5":
            try:
                amount = float(input("\nMonthly income: $"))
                tracker.set_income(amount)
            except ValueError:
                print("❌ Invalid amount")

        elif choice == "6":
            year_input = input("\nYear (Enter for current): ").strip()
            month_input = input("Month (1-12, Enter for current): ").strip()

            year = int(year_input) if year_input else None
            month = int(month_input) if month_input else None

            tracker.monthly_report(year, month)

        elif choice == "7":
            tracker.budget_overview()

        elif choice == "8":
            tracker.insights()

        elif choice == "9":
            print("\n💰 Keep managing your money wisely! Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-9.")


if __name__ == "__main__":
    main()
