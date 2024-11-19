from fastapi import FastAPI
import pyfiglet

app = FastAPI()

@app.get("/")
async def root():
    # Define the message
    message = "welcome to genesys info.com"
    
    # Generate the ASCII art version of the message using pyfiglet
    ascii_art = pyfiglet.figlet_format(message)
    
    # Return the ASCII art as part of the response
    return {"message": ascii_art}
