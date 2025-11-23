from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Roomers – Access to Healthcare in Colombia</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                line-height: 1.6;
                background: #f9f9f9;
                color: #333;
            }
            header {
                background: #00695c;
                color: white;
                padding: 20px;
                text-align: center;
            }
            header h1 {
                margin: 0;
                font-size: 2.2em;
            }
            header p {
                margin: 5px 0 0;
                font-size: 1.2em;
            }
            section {
                padding: 40px 20px;
                max-width: 900px;
                margin: auto;
            }
            section h2 {
                color: #00695c;
                margin-bottom: 10px;
            }
            .panel {
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }
            footer {
                background: #004d40;
                color: white;
                text-align: center;
                padding: 20px;
            }
            footer a {
                color: #ffcc80;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Roomers</h1>
            <p>Your gateway to healthcare access in Colombia</p>
        </header>

        <section>
            <div class="panel">
                <h2>Why Colombia?</h2>
                <p>Colombia has one of Latin America’s most dynamic healthcare systems, serving over 50 million people. 
                With universal coverage and a growing demand for innovative pharma and medtech solutions, the country offers 
                unique opportunities for global companies.</p>
            </div>

            <div class="panel">
                <h2>Our Role</h2>
                <p>Roomers provides direct pathways into Colombia’s healthcare ecosystem:</p>
                <ul>
                    <li>Regulatory guidance for pharma & medtech companies</li>
                    <li>Market entry strategies tailored to compliance</li>
                    <li>Partnerships with hospitals, clinics, and distributors</li>
                    <li>Support for clinical trials and innovation adoption</li>
                </ul>
            </div>

            <div class="panel">
                <h2>Benefits of Working With Us</h2>
                <ul>
                    <li><strong>Local Expertise:</strong> Deep understanding of Colombian healthcare regulations and culture</li>
                    <li><strong>Trusted Network:</strong> Connections with key stakeholders across the system</li>
                    <li><strong>Growth Opportunities:</strong> Access to a rapidly expanding market</li>
                    <li><strong>Compliance Ready:</strong> Audit-proof documentation and processes for smooth entry</li>
                </ul>
            </div>
        </section>

        <footer>
            <p>Let’s build healthcare access together.</p>
            <p>Contact us: <a href="mailto:contact@roomers.com">contact@roomers.com</a> | Phone: +57 XXX XXX XXXX</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)