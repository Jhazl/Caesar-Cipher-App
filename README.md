# Caesar-Cipher-App
Caesar Cipher App made using PyQt5


## About 
This application is a caesar cipher app made with PyQt5, this caeser cipher application was made as a experimental project to learn GUI programming with PyQt5. The gui consists of two windows you can encrypt and decrypt strings based on the number of shifts. 

<img src="CaesarCipherApp.png" width="600"/>

## How to set up

In order to set up this you will need to install PyQT5 using pip, in order to do this for windows in the command line type the following code:

```
pip install pyqt5
```

For other operating systems search online for the package installation instructions. You will also need python installed and running, you might need to add python to PATH in order to install PyQt5.

[Link to finding out how to add python to PATH](https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows)

### Setting up after installing packages 

To set up after installing packages you need to download the two packages from this repository which are: 

* caesearean_cypher.py
* caeser_cipher_ui.ui

Once installed place them in a folder and in that folder open the python file and edit with IDLE in order to change the line at the top of the file that says 

```python
Ui_MainWindow, QtBaseClass = uic.loadUiType(r"INSERT YOUR ABSOLUTE PATH HERE")
```
To your absolute path

Upon saving and running the file provided you have set up the packages needed the program should work.
