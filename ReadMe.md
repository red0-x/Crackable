# Crackable

A webapp for evalulating password security by calculating the estimated time needed to crack a password using brute force attacks.

## About

Crackable is a webapp I made during the congressional app challenge '23. 

It was intended to be helpful when understanding password security. 

Crackable helps you by analyzing your passwords and estimating how long it would take to crack them at various hash rates (hashes per second). My webapp gives you clarity on password strength and offers a built-in password generator for making better passwords

## Features

- **Password Strength Analyzer**: Calculate crack time based on password complexity and length
- **Customizable Hash Rates**: Test passwords against different computational speeds
- **Advanced Mode**: Specify custom hash rates for detailed security analysis
- **Password Generator**: Generate secure random passwords with customizable character sets
- **Real-Time Feedback**: Get instant visual feedback on password security
- **Entropy Calculation**: Analyzes character composition (uppercase, lowercase, numbers, symbols)

## Getting Started

### Prerequisites

- Python 3.7+
- pip (flask, getpass, dotenv) 

### Installation

1. **Clone the repository:**
```zsh
git clone https://github.com/red0-x/Crackable.git
cd Crackable
```
2. **Create .env with SECRET_KEY**
3. - I left an .env.example; honestly just rename it to .env if you're running this locally. 
