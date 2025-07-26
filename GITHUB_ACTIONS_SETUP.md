# GitHub Actions Setup Guide

This guide explains how to set up GitHub Actions to run your McGill Seat Checker automatically.

## Prerequisites

1. **Gmail App Password**: You need to generate an app password for your Gmail account
2. **GitHub Repository**: Your code should be pushed to a GitHub repository

## Step 1: Generate Gmail App Password

1. Go to your [Google Account settings](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification** (enable if not already enabled)
3. Go to **App passwords** (under 2-Step Verification)
4. Select "Mail" and "Other (Custom name)"
5. Name it "McGill Seat Checker" or similar
6. Copy the generated 16-character password (e.g., `awdz igdn aqbe qudh`)

## Step 2: Add Secret to GitHub Repository

1. Go to your GitHub repository
2. Click on **Settings** tab
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Name: `GMAIL_APP_PASSWORD`
6. Value: Your Gmail app password (e.g., `awdz igdn aqbe qudh`)
7. Click **Add secret**

## Step 3: Push Your Code

Make sure your updated code is pushed to GitHub:

```bash
git add .
git commit -m "Update to use email notifications instead of Pushover"
git push origin main
```

## Step 4: Test the Workflow

1. Go to your GitHub repository
2. Click on **Actions** tab
3. You should see the "Check Course Availability" workflow
4. Click on it and then click **Run workflow** to test manually

## How It Works

- **Schedule**: The workflow runs every 10 minutes automatically
- **Manual Trigger**: You can also run it manually using the "Run workflow" button
- **Email Notifications**: When courses become available, you'll receive emails at `aidan.kimberley@mail.mcgill.ca`

## Troubleshooting

### Common Issues:

1. **"GMAIL_APP_PASSWORD environment variable not set"**
   - Make sure you've added the secret correctly in GitHub
   - Check that the secret name is exactly `GMAIL_APP_PASSWORD`

2. **Chrome/ChromeDriver issues**
   - The workflow uses a headless Chrome setup with Xvfb
   - This should work automatically on GitHub's Ubuntu runners

3. **Email not sending**
   - Verify your Gmail app password is correct
   - Check that 2-factor authentication is enabled on your Gmail account
   - Ensure the app password has the correct permissions

### Monitoring

- Check the **Actions** tab in your GitHub repository to see workflow runs
- Each run will show logs that you can inspect for any errors
- Successful runs will show "✓" while failed runs will show "✗"

## Security Notes

- The Gmail app password is stored as a GitHub secret and is encrypted
- Never commit the app password directly to your code
- You can revoke the app password at any time from your Google Account settings

## Customization

You can modify the schedule by editing the cron expression in `.github/workflows/course_check.yml`:

- `*/10 * * * *` = Every 10 minutes
- `0 */1 * * *` = Every hour
- `0 9 * * *` = Every day at 9 AM
- `0 9 * * 1-5` = Weekdays at 9 AM 