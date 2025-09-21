# from src.services.processor import add

# print(add(1, 5))


import argparse

from src.billing_tool.billing import apply_billing


def main():
    pasrser = argparse.ArgumentParser(description="Automate tenant billing")
    pasrser.add_argument("file", help="Path to excel file")
    args = pasrser.parse_args()

    apply_billing(args.file)


if __name__ == "__main__":
    main()
