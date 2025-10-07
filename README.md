# 🛡️ SilverGuard
**An AI hardware solution for elderly nursing home residents that prevents financial fraud and scams.**

---

## 📘 Overview
SilverGuard is an AI-powered protection system designed to **detect and prevent financial scams targeting elderly individuals**, especially those in **nursing homes or assisted living facilities**.  

The system listens to **phone conversations** and **voice interactions** in real time through a **Raspberry Pi setup**, using machine learning models to detect **scam-related patterns, keywords, or speech tones**.  

When a potential scam is detected, SilverGuard triggers an **instant voice alert** to warn the user — helping prevent financial losses and ensuring peace of mind for families and caregivers.

---

## ⚙️ System Components

| Component | Description |
|------------|--------------|
| **Raspberry Pi 5** | The main microcomputer handling audio input/output and running the AI model. |
| **USB Microphone & Speaker** | Captures voice conversations and outputs real-time audio alerts. |
| **AI Hat / Accelerator** | Enhances on-device computation for faster model inference. |
| **Local Model** | Detects scam-related speech and tags risky phrases using NLP + audio analysis. |
| **Speaker Alert System** | Plays a pre-recorded warning message (e.g. “⚠️ Warning: This conversation may be a scam”). |

---

## 🧠 Core Functionality

1. **Audio Capture**  
   - The microphone continuously listens for incoming conversations or phone calls.  
2. **Voice Processing**  
   - The Raspberry Pi processes the audio input locally using a lightweight model (no cloud dependency).  
3. **Scam Detection**  
   - AI model scans for scam-related keywords, emotional tone, and conversational patterns.  
4. **Alert Trigger**  
   - If a scam is detected, the system sends a command to the speaker to play a warning message.  
5. **Optional Logging** *(under development)*  
   - Conversation snippets and detection confidence scores can be logged for caregiver review.  

---

## 🧩 Tech Stack

- **Hardware:** Raspberry Pi 5, AI Hat (Coral TPU or equivalent), USB Microphone & Speaker  
- **Languages:** Python  
- **Libraries:**  (MAY BE UPDATED)
  - `speech_recognition` – Audio transcription  
  - `transformers` / `torch` – NLP model for scam detection  
  - `pyaudio` – Real-time audio streaming  
  - `gtts` or pre-recorded MP3s – Voice alert generation  
- **Model:** Custom fine-tuned transformer model for scam keyword detection  

---

## 🚧 Current Development Stage

- ✅ System design and hardware setup  
- ✅ Basic audio capture and output working (in progress)
- 🧩 Building the scam detection model and keyword tagging pipeline  
- 🧠 Integrating detection with real-time audio stream  
- 🔊 Testing voice alert trigger on scam detection  
