import base64
import requests

class Solver:
    def __init__(self, question) -> None:
        self.question = question
        
    def solve(self, image_url):
        
        image = requests.get(image_url).content
        encoded_string=  base64.b64encode(image).decode("utf-8")
        
        json_data = {
            'requests': [
                {
                "image": {
                    "content": encoded_string
                },
                    'features': [
                        {
                            'maxResults': 7,
                            'type': 'LABEL_DETECTION',
                        },
                    ],
                },
            ],
        }

        response = requests.post(
            url = 'https://content-vision.googleapis.com/v1/images:annotate?alt=json&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM',
            headers = {            
                'x-origin': 'https://explorer.apis.google.com',
            },
            json = json_data
        )
        
        image = "undefined"
        
        if "Airplane" in response.text or "Aircraft" in response.text:
            image = "airplane"
            
        elif "Bus" in response.text or "Public transport" in response.text:
            image = "bus"
            
        elif "Tire" in response.text or "Wheel" in response.text or "Bycicle" in response.text or "Bycicle tire" in response.text or "Bicycle handlebar" in response.text or 'Bicycle seatpost'in response.text:
            if "Motorcycle" in response.text:
                image = "motorcycle"
            else:
                image = "bycicle"
            
        elif "Display device" in response.text or "Font" in response.text or "Screenshot" in response.text or 'Water' in response.text or  'Boat' in response.text or  'Liquid' in response.text or 'Watercraft' in response.text or 'Naval architecture':
            image = "boat"

        if image == self.question:
            return True
        else:
            return False
