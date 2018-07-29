# pylint: skip-file
from app import app
import views

app.run(port=5000, host='0.0.0.0', threaded=False)
