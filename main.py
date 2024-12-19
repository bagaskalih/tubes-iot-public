from flask import Flask, request, render_template
from supabase import create_client

supabase_url = "https://sbbybeiuhpupwdsytcpx.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNiYnliZWl1aHB1cHdkc3l0Y3B4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQ1NjM2NTAsImV4cCI6MjA1MDEzOTY1MH0.yoIIcexQLnM78olPY58HWRLRvhG8_EYcGiPCyrfMZYs"
supabase = create_client(supabase_url, supabase_key)
table_name = 'test2'

# Flask app initialization
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    """Fetch data from Supabase."""
    response = supabase.table(table_name).select('*').execute()
    # convert into json
    data = response.data
    return {"data": data}, 200

@app.route('/', methods=['GET'])
def view_data():
    """Render HTML page that shows the data from the Supabase database."""
    # Get the data from the /data endpoint
    response = supabase.table(table_name).select('*').execute()
    data = response.data
    return render_template('index.html', data=data)

if __name__ == "__main__":
    # Start the Flask server
    app.run()