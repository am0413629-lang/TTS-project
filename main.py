name: TTS Bot Factory
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run script
        run: python main.py
      - name: Upload result
        uses: actions/upload-artifact@v4
        with:
          name: output-audio
          path: output.mp3
