# 🔐 Password & PIN Generator

A secure, user-friendly web application for generating strong passwords and numeric PINs.

## Features

- **Password Generation**: Create secure passwords with customizable options
  - Include/exclude numbers
  - Include/exclude special characters
  - Adjustable length (4-32 characters)
- **PIN Generation**: Generate numeric PINs (4-10 digits)
- **Password Strength Indicator**: Real-time visual feedback on password strength
- **Copy to Clipboard**: One-click copying of generated passwords
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Clean, intuitive interface built with Bootstrap

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rajdangui/password-generator.git
cd password-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:8080
```

## Deployment

The application is configured for deployment on Heroku or similar platforms using Gunicorn.

The `Procfile` is already configured:
```
web: gunicorn app:app
```

## Usage

1. **Choose Type**: Select between Password or PIN generation
2. **Set Length**: Specify the desired length
3. **Configure Options**: For passwords, choose whether to include numbers and special characters
4. **Generate**: Click the generate button to create your secure password or PIN
5. **Copy**: Use the copy button to easily copy the generated value to your clipboard

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Server**: Gunicorn (for production deployment)

## Security

The application uses Python's built-in random module for generating passwords and PINs. All generation happens server-side to ensure consistency and security.

## License

This project is open source and available for educational purposes.
