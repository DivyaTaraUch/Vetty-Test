
from flask import Flask, render_template, request
import os

app = Flask(__name__)
FILES_DIR = "files"

@app.route('/')
def display_file():

    filename = request.args.get('filename', 'file1.txt')

    start_line = request.args.get('start_line')
    end_line = request.args.get('end_line')
    
    
    file_path = os.path.join(FILES_DIR, filename)
    
    try:
       
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
           
            if start_line is not None and end_line is not None:
                lines = lines[int(start_line) - 1:int(end_line)]
            
          
            return render_template('file_content.html', filename=filename, lines=lines)
    
    except FileNotFoundError:
        return render_template('error.html', error_message=f"File '{filename}' not found.")
    
    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
