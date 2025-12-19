# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server using Flask
server = Flask(__name__)


@server.get('/')
def homepage():
    return "<html><body><h1>Smart Home Monitoring System</h1></body></html>"


# ------------------ UPDATE SENSOR DATA ------------------
@server.post('/update')
def update_sensors():
    # extract data from form
    light_status = request.form.get('light_status')
    fan_status = request.form.get('fan_status')
    temperature = request.form.get('temperature')
    updated_at = request.form.get('updated_at')

    # create insert query
    query = f"""
    insert into home_status
    values(NULL, '{light_status}', '{fan_status}', '{temperature}', '{updated_at}');
    """

    # execute the query
    executeQuery(query=query)

    return "Smart home sensor data added successfully"


# ------------------ GET CURRENT STATUS ------------------
@server.get('/status')
def get_status():
    # select latest sensor data
    query = """
    select light_status, fan_status, temperature
    from home_status
    order by id desc limit 1;
    """

    # execute select query
    data = executeSelectQuery(query=query)

    return f"Current Smart Home Status : {data}"


# ------------------ RUN SERVER ------------------
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
