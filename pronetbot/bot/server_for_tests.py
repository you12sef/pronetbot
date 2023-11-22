from flask import Flask, request ,render_template,jsonify
from haversine import haversine, Unit


app = Flask(__name__,template_folder="C:\\Users\\Yosef\\OneDrive\\Desktop\\pronetbot\\bot")
    

@app.route("/", methods=["GET","POST"])
def get_location():
    print (request.method)
    if request.method == "GET":
        #return request.args.get("hub.challenge")    
        return render_template("index.html")
    else:
        #location = grt_close_location(request.get_json()) 
        location = request.get_json() 
        print (location)
        return "Done"

@app.route("/optionspostback", methods=["GET"])
def submit():   
    return 'Please close this window to return to the conversation thread.'
   
def grt_close_location(target):
    
    target = (target['lat'],target['lon'])
    locations = {(32.882219, 13.234883):"سوق الجمعة",
             (32.887870, 13.177410):"منيدر",
             (32.853620, 13.242877):"الفرناج",
             (32.822330, 13.321512):"عين وارة",
             (32.758903, 12.743362):"الزاوية"}
    
    list_distance = []
    locations_ = list(locations)
    for i in locations_:
        list_distance.append(haversine(i,target))
        
    minimum_value = min(list_distance)
    if minimum_value > 8:
        return "لا يوجد برج قريب منك"
    get_index =  list_distance.index(minimum_value)
    key = locations_[get_index]
    nearest_distance = locations[key]
    return nearest_distance 
    
    



    
if __name__=='__main__':
    app.run(port=5000)

