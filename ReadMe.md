# Crackable
A webapp for evalulating password security by calculating the estimated time needed to crack a password using brute force attacks.

<img width="550" height="450" alt="crackable" src="https://github.com/user-attachments/assets/85a26222-dd10-4d58-9021-381739ed0ec0" />



## About

Crackable is a webapp I made during the congressional app challenge '23. 

It was intended to be helpful when understanding password security. 

Crackable helps you by analyzing your passwords and estimating how long it would take to crack them at various hash rates (hashes per second). My webapp gives you clarity on password strength and offers a built-in password generator for making better passwords.

Crack times are modeled against **MD5** — the fastest, most widely deployed (and most insecure) password hash. This is intentionally a worst-case estimate: if a site stores passwords in MD5, these are realistic attack times. Secure hashing algorithms like bcrypt or Argon2 are 10,000–1,000,000× slower, so real secure systems would take far longer to crack.

## Features

- **Password Strength Analyzer**: Calculate crack time based on password complexity and length
- **Customizable Hash Rates**: Test against four MD5 cracking scenarios — Typical Computer (~50 MH/s CPU), Supercomputer (~2.6 TH/s GPU cluster), Cracking Computer (~110 TH/s dedicated rig), Bitcoin Miner (~120 TH/s ASIC estimate)
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
