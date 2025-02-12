# GeReco

## Vision & Cognitive Systems Project

**Authors:**  
- **Andre Auletta** - 2107158 - [andrea.auletta@studenti.unipd.it](mailto:andrea.auletta@studenti.unipd.it)  
- **Marco Bernardi** - 2107781 - [marco.bernardi.11@studenti.unipd.it](mailto:marco.bernardi.11@studenti.unipd.it)  
- **Sebastiano Sanson** - 2130917 - [sebastiano.sanson@studenti.unipd.it](mailto:sebastiano.sanson@studenti.unipd.it)  

---

## Project Overview
GeReco (Gesture Recognition) is a project focused on recognizing both dynamic and static gestures using deep learning techniques, including LSTMs and Mediapipe-based models. The system is designed for real-time inference using a standard USB camera.

---

## Directory Structure

### `dynamic-hg/`
Contains the implementation for dynamic gesture recognition using an LSTM-based approach with dimensionality reduction, inspired by [Next-Gen Dynamic Hand Gesture Recognition: MediaPipe, Inception-v3 and LSTM-Based Enhanced Deep Learning Model](https://www.mdpi.com/2079-9292/13/16/3233).

- **`inference.ipynb`**: Notebook for performing real-time inference using a trained model and a USB camera.
- **`training.ipynb`**: Notebook for data preprocessing and training the LSTM model.

### `static-hg/`
Contains the implementation for static gesture recognition using Mediapipe.

- **`inference.py`**: Script for real-time inference of static gestures.
  - Usage: `python inference.py <model-path> <OpenCV-Device-Id>`
- **`training.ipynb`**: Notebook for data preprocessing and training the model.

### `results/`
Stores snapshots of training results and performance metrics.

- **`MIL_results.md`**: (Mediapipe Inception LSTM) Contains logs of training results from multiple runs.
- **`MP_results.md`**: (Mediapipe) Contains logs of training results from multiple runs.

### `paper/`
Contains the source files for the project paper.

### `transformer/`
Directory reserved for Transformer-based experiments (if applicable).

## License
This project is licensed under the [MIT License](LICENSE).

