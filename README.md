# Start Work Script

This script automates the process of setting up your work environment by launching necessary programs at startup.

## Objectives

- Opens Teams on the second monitor
- Opens Outlook on the second monitor
- Opens Edge on the main monitor
- Starts a YouTube lofi playlist

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Ayoobf/start-work.git
   cd start-work
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source .venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script :
```
python start_work.py
```
> This will automatically make the script run at startup 

## Configuration

Modify the `config/config.yaml` file to customize application paths, window positions, and other settings.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
