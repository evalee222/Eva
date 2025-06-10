import argparse
import csv
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Item:
    name: str
    price: float
    cost: float
    note: str = ""
    profit: float = field(init=False)
    margin: float = field(init=False)

    def __post_init__(self):
        self.calculate()

    def calculate(self):
        self.profit = self.price - self.cost
        self.margin = (self.profit / self.price * 100) if self.price else 0


def read_items_from_csv(path: str) -> List[Item]:
    items = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(Item(
                name=row.get('name', ''),
                price=float(row.get('price', 0) or 0),
                cost=float(row.get('cost', 0) or 0),
                note=row.get('note', '')
            ))
    return items


def interactive_input() -> List[Item]:
    items = []
    print("Enter items. Leave name empty to finish.")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            price = float(input("Price: "))
            cost = float(input("Cost: "))
        except ValueError:
            print("Invalid number, try again.")
            continue
        note = input("Note (optional): ").strip()
        items.append(Item(name=name, price=price, cost=cost, note=note))
    return items


def print_report(items: List[Item]):
    print("\n--- Report ---")
    header = f"{'Name':<20}{'Price':>10}{'Cost':>10}{'Profit':>10}{'Margin%':>10}"
    print(header)
    print('-' * len(header))
    total_price = total_cost = total_profit = 0
    for it in items:
        total_price += it.price
        total_cost += it.cost
        total_profit += it.profit
        print(f"{it.name:<20}{it.price:>10.2f}{it.cost:>10.2f}{it.profit:>10.2f}{it.margin:>10.0f}%")
    avg_margin = (total_profit / total_price * 100) if total_price else 0
    print('-' * len(header))
    print(f"{'TOTAL':<20}{total_price:>10.2f}{total_cost:>10.2f}{total_profit:>10.2f}{avg_margin:>10.0f}%")


def export_csv(items: List[Item], path: str):
    fieldnames = ['name', 'price', 'cost', 'profit', 'margin', 'note']
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for it in items:
            writer.writerow({
                'name': it.name,
                'price': it.price,
                'cost': it.cost,
                'profit': it.profit,
                'margin': it.margin,
                'note': it.note,
            })
    print(f"Exported to {path}")


def main():
    parser = argparse.ArgumentParser(description="Simple profit calculator")
    parser.add_argument('--csv', help='Input CSV with columns name,price,cost,note')
    parser.add_argument('--export', help='Export results to CSV')
    args = parser.parse_args()

    items: List[Item]
    if args.csv:
        items = read_items_from_csv(args.csv)
    else:
        items = interactive_input()

    if not items:
        print("No items provided.")
        return

    print_report(items)

    if args.export:
        export_csv(items, args.export)

if __name__ == '__main__':
    main()
