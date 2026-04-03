import sys
from pathlib import Path


def analyze_log(log_text: str) -> str:
    log_text = log_text.lower()

    if "cannot find module" in log_text or "npm err" in log_text:
        return "Possible Node.js dependency issue. Check package.json and run npm install."

    if "docker" in log_text and "failed" in log_text:
        return "Possible Docker build problem. Check the Dockerfile and file paths."

    if "terraform" in log_text and "error" in log_text:
        return "Possible Terraform configuration issue. Check syntax, providers, and variable values."

    if "port 3000 is already in use" in log_text or "eaddrinuse" in log_text:
        return "Possible port conflict. Stop the running service or use a different port."

    return "No known issue matched. Review the logs manually."


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer.py <log_file>")
        sys.exit(1)

    log_file = Path(sys.argv[1])

    if not log_file.exists():
        print(f"Error: file not found -> {log_file}")
        sys.exit(1)

    log_data = log_file.read_text(encoding="utf-8", errors="ignore")
    result = analyze_log(log_data)

    print("Analysis Result:")
    print(result)


if __name__ == "__main__": main()

