from flask import Flask
import argparse


parser = argparse.ArgumentParser()


app = Flask(__name__)

@app.route('/')
def main():
    return "ASS"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
