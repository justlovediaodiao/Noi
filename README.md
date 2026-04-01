# Noi - Minimal Note Reminder

A minimal Android app to display notes in the notification bar.

## Features

- Tap app icon to show floating multi-line input dialog
- Press Enter to send content to notification bar
- Tap notification to edit content
- Only one notification is kept in the notification bar

## Tech Stack

- Kotlin
- Android SDK 24+
- No persistent storage required

## Signing Configuration

Configure the following variables in GitHub Repository Secrets:

- `SIGNING_KEY`: Base64 encoded keystore file
- `ALIAS`: Key alias
- `KEY_STORE_PASSWORD`: Keystore password
- `KEY_PASSWORD`: Key password

## Generate Signing Key

```bash
# Generate private key
openssl genrsa -out noi.key 2048

# Create self-signed certificate
openssl req -new -x509 -key noi.key -out noi.crt -days 10000 -subj "/CN=Noi"

# Package into PKCS#12 keystore
openssl pkcs12 -export -in noi.crt -inkey noi.key -out noi.p12 -name noi

# Base64 encode for GitHub Secrets
base64 -i noi.p12
```

## Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions will automatically build and release the APK.
