#!/usr/bin/env python3
"""
Project: Modular Python Script Template
Description: Just plug in your def functions and run!
"""

import argparse
import sys
from typing import Optional

# ==========================================
# 🧩 1. PLUG IN YOUR FUNCTIONS HERE (def)
# ==========================================

def my_first_function(name: str, repeat: int = 1) -> None:
    """Tomar prothom function ekhane rakho."""
    for i in range(repeat):
        print(f"[{i+1}] Hello, {name}! This is running from your custom function.")

def my_second_function(number: int) -> int:
    """Ekhane arekta function rakho jeta kichu return kore."""
    result = number * 10
    return result

# ==========================================
# ⚙️ 2. CORE EXECUTION ENGINE (Auto-Handles Flow)
# ==========================================

def parse_arguments() -> argparse.Namespace:
    """Command-line arguments manage kore."""
    parser = argparse.ArgumentParser(
        description="Modular Python Template - Just add functions."
    )
    # Ekhane tumi CLI arguments add korte paro jodi dorkar hoy
    parser.add_argument(
        "--name", 
        type=str, 
        default="Zaman", 
        help="Name parameter for function 1"
    )
    parser.add_argument(
        "--num", 
        type=int, 
        default=5, 
        help="Number parameter for function 2"
    )
    return parser.parse_args()

def main() -> None:
    """Main execution flow - sob ekhane automatic connect thakbe."""
    try:
        args = parse_arguments()
        print("--- 🚀 Script Started Successfully ---")
        
        # ==========================================
        # TOMAR NOTUN FUNCTION GULO EKMANE CALL KORBE
        # ==========================================
        
        result = tomar_notun_function(args.name)
        print(result)
        
        print("--- ✨ Script Finished Successfully ---")
        
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[❌ Error]: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()