# vaccine_slot_booking
Vaccination/Vaccine Slots are getting instantly Booked.
To create a chance for arranging a vaccination slot, use simple automatic python script to make bookings as soon you find a slot available.

# Features
- Constant Periodic Monitoring of the COWIN Site for Slot Availability.
- Information reagarding Centers with Available Slots with their respective Areas.
- Information about Centers with Free/Paid Vaccination.
- Parallel/Concurrent request processing with for Slot Booking.

# Requirements
- Python 3.7

## Usage ##
`python vaccine_booking.py`

## Contributions ##

We welcome contributions of any kind. If you have a bug or an idea, read the 
development guidelines setup.

## Development Guidelines Setup

- pre commit python framework
1. Install pre-commit: `pip install pre-commit`
2. Add pre-commit to requirements.txt
3. Define `.pre-commit-config.yaml` with the hooks.
```
repos:
-   repo: https://github.com/ambv/black
    rev: 21.5b0
    hooks:
    - id: black
      language_version: python3.7
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.9.1
    hooks:
    - id: flake8
```
4. Execute `pre-commit install` to install git hooks in your .git/ directory.
5. Incase you see the below during commit:
```
black....................................................................Failed
- hook id: black
- files were modified by this hook
```
- Hint: `pre-commit autoupdate` often fixes this

