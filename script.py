import requests

# Your GitHub username
username = "niladrigithub"

# Fetch list of repositories
response = requests.get(f"https://api.github.com/users/{username}/repos")
repos = response.json()

# Initialize dictionary to store language counts
language_counts = {}

# Iterate through each repository to get languages used
for repo in repos:
    repo_name = repo["name"]
    languages_url = repo["languages_url"]
    languages_response = requests.get(languages_url)
    languages_data = languages_response.json()
    
    # Update language counts
    for language, bytes_count in languages_data.items():
        if language in language_counts:
            language_counts[language] += bytes_count
        else:
            language_counts[language] = bytes_count

# Generate README content
readme_content = """# GitHub Repository Summary

An automated analysis tool that generates a summary of programming languages used across GitHub repositories.

## Overview

This repository contains a variety of projects and code snippets showcasing my programming skills and interests.

## Languages Used

Below is a list of programming languages used across my GitHub repositories:\n"""

for language, bytes_count in sorted(language_counts.items(), key=lambda x: x[1], reverse=True):
    readme_content += f"- {language}: {bytes_count} bytes\n"

readme_content += "\n## Projects\n\n(Include your project highlights here)"

# Write content to README file
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README.md file generated successfully!")
