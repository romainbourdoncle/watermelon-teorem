# watermelon-teorem
[Cliquez ici pour voir ce README en français](README_FR.md)

A dynamic viewer developed to accompany the resolution of a math problem that is part of a wider pedagogical projet. The application uses Matplotlib to allow dynamic exploration of area constancy in a circle divided by cutting lines from an interior movable point. 

![app_screenshot](./docs/capture.png)

**Description**
This Python application is part of the CSEN | GT3 initiative aimed at creating a comprehensive database of mathematical problems. It serves as an interactive educational tool to explore a specific geometry problem involving area constancy in a circle divided by cutting lines from an interior movable point. _**To move point P, double-click the desired location**._

Web app: [https://romainbourdoncle.github.io/watermelon-teorem/](https://romainbourdoncle.github.io/watermelon-teorem/) _There are known issues with SVG interactivity on Safari and iPhone. For optimal experience, use Chrome or Firefox on a desktop or laptop_.
## Instructions for Running the python app

**For Windows Users**
If you are using Windows, you can simply download then execute the provided .exe file to run the application.

[Download the App](https://github.com/romainbourdoncle/watermelon-teorem/releases/download/v1.0.0/tracer_cercle4.exe)

**For macOS Users**
If you are using macOS, you need to run the code via the terminal. Please check the file named *tracer_cercle4* in the **src** folder for source code. Here are the steps to do so:
1. Open the terminal and navigate to the folder containing the script.
2. Install required packages:
```
pip install matplotlib pip numpy
```

4. Run the script:
```
python tracer_cercle4.py
```
**Contributing**
This project is part of the larger CSEN | GT3 initiative. Contributions are welcome, especially for educational purposes. For major changes, please open an issue first to discuss what you would like to change.

**License**
This project is licensed under CC BY-NC
