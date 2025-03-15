# VoxVoyage: Interactive Storytelling Powered by Zonos AI  
*Crafting Your Audio Adventures with Every Word* 🚀🎙️

---

## Overview

**VoxVoyage** is an innovative interactive storytelling platform that transforms your written narratives into dynamic, emotionally engaging audio adventures. Leveraging the state-of-the-art **Zonos AI** text-to-speech model, VoxVoyage enables you to create multi-path, immersive stories with personalized voice cloning, emotion control, and cinematic audio quality. Whether you're an indie author, educator, or creative enthusiast, VoxVoyage empowers you to bring your stories to life like never before.

---

## Table of Contents

- [Features](#features)
- [What is Zonos AI?](#what-is-zonos-ai)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
  - [Gradio Interface](#gradio-interface)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
- [Demo & Useful Links](#demo--useful-links)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Interactive Storytelling:**  
  Craft multi-path narratives that adapt dynamically to user choices, ensuring a unique adventure every time.
  
- **Personalized Narration:**  
  Utilize voice cloning to generate lifelike speech that matches your chosen persona or character.

- **Emotion & Tone Control:**  
  Fine-tune the emotional delivery of each narrative segment to create suspense, warmth, or mystery as needed.

- **Cinematic Audio Quality:**  
  Enjoy high-fidelity audio output at native 44kHz, perfect for audiobooks, podcasts, and immersive VR experiences.

- **Cumulative Audio Generation:**  
  Listen to individual audio segments on the fly while building a continuous, complete audio file for the entire story.

- **Multilingual Support:**  
  Reach a global audience with support for multiple languages.

- **User-Friendly Interfaces:**  
  Choose between an interactive Gradio web interface or a command-line interface for testing and development.

---

## What is Zonos AI?

**Zonos AI** is a cutting-edge, open-weight text-to-speech model trained on over 200,000 hours of diverse multilingual speech. Its standout capabilities include:

- **Zero-Shot TTS & Voice Cloning:**  
  Generate expressive, natural speech using minimal reference audio.

- **Audio Prefix Inputs:**  
  Enhance voice matching by capturing nuanced vocal behaviors like whispering.

- **Fine-Grained Control:**  
  Adjust parameters such as speaking rate, pitch, and emotional tone to tailor the audio output.

- **Multilingual Capability:**  
  Produce high-quality speech in languages including English, Japanese, Chinese, French, and German.

*Zonos AI was chosen for VoxVoyage because of its remarkable fidelity and flexibility, making it ideal for creating truly immersive, interactive storytelling experiences.*

---

## How It Works

1. **User Input & Voice Cloning:**  
   - Upload a short voice sample to create a personalized speaker embedding.
   - Adjust parameters like speaking rate and pitch using intuitive controls.

2. **Interactive Narrative Structure:**  
   - The story is defined as a series of interconnected nodes. Each node contains narrative text, an associated emotion, and multiple user choices.
   - Every decision triggers the generation of a new audio segment using Zonos AI.

3. **Audio Processing & Concatenation:**  
   - Each new audio segment is saved as a temporary file for immediate playback.
   - Simultaneously, the new segment is concatenated with previous segments to form a complete, cumulative audio file of the entire story.

4. **User Interfaces:**  
   - **Gradio Interface:** Offers a modern, web-based UI for interactive storytelling.
   - **CLI Interface:** Provides a command-line option for developers to test and debug core functionalities.

---

## Installation

### System Requirements

- **Operating System:** Linux (Ubuntu preferred) or macOS (experimental Windows support available)
- **GPU:** Recommended 6GB+ VRAM (CPU execution is supported but slower)
- **Dependencies:**  
  - **eSpeak NG:** For text phonemization  
    - Ubuntu: `sudo apt install -y espeak-ng`
    - macOS: `brew install espeak-ng`
  - **Python Libraries:** `torch`, `torchaudio`, `gradio`

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/VoxVoyage.git
   cd VoxVoyage
   ```

2. **Install Python Dependencies:**
   ```bash
   pip install -e .
   pip install -e .[compile]
   pip install gradio torch torchaudio
   ```

3. **(Optional) Docker Setup:**
   ```bash
   docker compose up
   ```

---

## Usage

### Gradio Interface

To launch the interactive web interface:
```bash
python your_gradio_interface_script.py
```
- **Start Story:** Upload a voice sample, adjust parameters, and click "Start Story" to begin.
- **Advance Story:** Choose an option from the available radio buttons to generate the next audio segment.
- **Quit Story:** Click "Quit Story" to output the complete, cumulative audio file of your narrative.

### Command-Line Interface (CLI)

For testing and development, run the CLI version:
```bash
python your_cli_script.py
```
- Follow on-screen prompts to upload your voice sample, adjust parameters, and navigate through the story.
- Listen to individual segments or output the full cumulative audio when you quit.

---

## Demo & Useful Links

- **Zonos AI GitHub Repository:** [https://github.com/Zyphra/Zonos](https://github.com/Zyphra/Zonos)
- **Zonos AI Playground:** [https://playground.zyphra.com/audio](https://playground.zyphra.com/audio)
- **Gradio Documentation:** [https://gradio.app/get_started](https://gradio.app/get_started)
- **eSpeak NG:** [http://espeak.sourceforge.net/](http://espeak.sourceforge.net/)

---

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements, bug fixes, or additional features. For major changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

---

## Contact

For questions, ideas, or feedback, feel free to reach out:

- **Email:** [your.email@example.com](mailto:your.email@example.com)
- **GitHub Issues:** [https://github.com/yourusername/VoxVoyage/issues](https://github.com/yourusername/VoxVoyage/issues)

---

Embrace the future of interactive storytelling with **VoxVoyage** – where every word transforms into an unforgettable audio adventure powered by Zonos AI! 🎧📖
